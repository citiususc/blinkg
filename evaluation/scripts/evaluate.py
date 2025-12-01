import os
import glob
from blinkg.evaluate import match_tables, calculate_prf, get_header_mapping, normalized_levenshtein, calculate_bert, calculate_bert_lex, calculate_levenshtein
from blinkg.utils import clean_values, empty_values, model
from utils import parse_md_table
from rdflib import Graph
import pandas as pd
import numpy as np
from sentence_transformers import util


def find_row_matches(folder_path: str, t2: pd.DataFrame):
    row_pairs = []
    common_cols = []
    row_pairs_column = []

    for md_file in sorted(os.listdir(folder_path)):
        if not md_file.endswith(".md"):
            continue

        print(f"Evaluating {folder_path}/{md_file}")
        exp_md = open(os.path.join(folder_path, md_file), "r", encoding="utf-8").read()
        t1 = parse_md_table(exp_md)

        pairs, cols, pairs_col = match_tables(t1, t2)
        common_cols = cols

        for r2, r1 in pairs:
            row_pairs.append((md_file, r2, r1))

        for r2, r1 in pairs_col:
            row_pairs_column.append((md_file, r2, r1))

    return row_pairs, common_cols, row_pairs_column

def find_row_matches2(folder_path: str, t2: pd.DataFrame):
    """
    For each .md file in folder_path, parse the predicted table (t1)
    and, for each row in t1, find the single best‐matching row in t2
    based on exact matches over the canonical fields.
    Returns a list of triples: (md_filename, gt_row_index, exp_row_index),
    plus the list of common columns.
    """
    row_pairs = []
    common_cols = []
    row_pairs_column = []
    for md_file in sorted(os.listdir(folder_path)):
        if not md_file.endswith(".md"):
            continue

        print(f"Evaluating {folder_path}/{md_file}")
        exp_md = open(os.path.join(folder_path, md_file), "r", encoding="utf-8").read()
        t1 = parse_md_table(exp_md)

        # Map actual headers to our keys, and pick which to compare
        mapping_pred = get_header_mapping(list(t1.columns))
        mapping_gt   = get_header_mapping(list(t2.columns))
        all_keys = ['column', 'ontology_prop', 'entity_class']
        metrics_keys = [k for k in all_keys if k in mapping_pred and k in mapping_gt]

        # Track common columns for downstream processing
        common_cols = [c for c in sorted(set(t1.columns) | set(t2.columns))
                       if c != 'index']

        # Build cost matrix: rows = predicted, cols = ground truth
        n_pred, n_gt = len(t1), len(t2)
        cost_matrix = np.zeros((n_pred, n_gt))
        for i, r1 in enumerate(t1.index):
            for j, r2 in enumerate(t2.index):
                sims = []
                v1_list =  []
                v2_list = []
                for key in metrics_keys:
                    h1, h2 = mapping_pred[key], mapping_gt[key]
                    v1 = t1.at[r1, h1] if h1 in t1.columns else ""
                    v2 = t2.at[r2, h2] if h2 in t2.columns else ""
                    if v1 not in empty_values and v2 not in empty_values:
                        v1_list.append(v1)
                        v2_list.append(v2)
                    #print(f"Comparando {v1} ({r1},{h1}) con {v2} ({r2},{h2})")
                if ", ".join(v1_list) == ", ".join(v2_list):
                    sim = 1.0
                else:
                    levenshtein = normalized_levenshtein(", ".join(v1_list), ", ".join(v2_list))
                    bert = calculate_bert(", ".join(v1_list), ", ".join(v2_list))
                    sim = max(levenshtein, bert)
                sims.append(sim)
                cost_matrix[i, j] = 1.0 - sim

        # For each predicted row, pick its best‐matching GT row
        used_gt = set()
        for i, r1 in enumerate(t1.index):
            # ordena los índices de t2 por menor coste (mayor sim)
            sorted_js = np.argsort(cost_matrix[i])
            # busca el primero no usado
            for j_best in sorted_js:
                if j_best not in used_gt:
                    used_gt.add(j_best)
                    break
            else:
                # si todos ya están usados, toma el mejor disponible
                j_best = sorted_js[0]
            r2 = t2.index[j_best]
            sim = 1.0 - cost_matrix[i, j_best]
            row_pairs.append((md_file, r2, r1))
            print(f"  EXP row '{r1}' → GT row '{r2}' (sim={sim:.4f})")

        used_pred = set()
        for j, r2 in enumerate(t2.index):
            # sort predicted indices by increasing cost (i.e. decreasing sim)
            sorted_i = np.argsort(cost_matrix[:, j])
            # pick the first i not yet used
            for i_best in sorted_i:
                if i_best not in used_pred:
                    used_pred.add(i_best)
                    break
            else:
                # if all used, fallback to best overall
                i_best = sorted_i[0]
            r1 = t1.index[i_best]
            sim = 1.0 - cost_matrix[i_best, j]
            row_pairs_column.append((md_file, r2, r1))
            print(f"  GT row '{r2}' → EXP row '{r1}' (sim={sim:.4f})")

    return row_pairs, common_cols ,row_pairs_column

def eval_levenshtein(t2: pd.DataFrame, row_pairs:list, common_cols: list, folder_path) -> None:
    metrics = []
    for md_file in sorted(os.listdir(folder_path)):
        print(f"Evaluating {folder_path}/{md_file}")
        if not md_file.endswith(".md"):
            continue
        exp_md = open(os.path.join(folder_path, md_file), "r", encoding="utf-8").read()
        t1 = parse_md_table(exp_md)
        for col in common_cols:
            sims = []
            print(f"\nComparing column '{col}' across matched pairs:")
            for file_name, r2, r1 in row_pairs:
                if file_name != md_file:
                    continue
                v1 = t1.at[r1, col] if (r1 in t1.index and col in t1.columns) else ""
                v2 = t2.at[r2, col] if (r2 in t2.index and col in t2.columns) else ""
                if v1 not in empty_values or v2 not in empty_values:
                    v1, v2 = clean_values(v1, v2)
                    sim = normalized_levenshtein(v1, v2)
                    sims.append(sim)
                    print(f"  Pair GT {r2} ('{v2}') vs exp {r1} ('{v1}'): {sim:.4f}")
            mean_sim = sum(sims) / len(sims) if sims else 0.0
            print(f"Mean similarity for column '{col}': {mean_sim:.4f}")
            metrics.append({
                'file': os.path.basename(md_file),
                'column': col,
                'similarity': mean_sim
            })

    # Aggregate across all files
    df = pd.DataFrame(metrics)
    summary = (df
               .groupby("column")["similarity"]
               .mean()
               .reset_index()
               .rename(columns={"similarity": "mean_similarity"}))
    name = folder_path.split("/")[-1] + '_levenshtein.csv'
    output_csv = os.path.join(folder_path, name)
    summary.to_csv(output_csv, index=False)
    print(f"\nSaved aggregated results to {output_csv}")


def eval_bert(ground_truth: pd.DataFrame, row_pairs:list, common_cols: list, folder_path):
    metrics = []
    for md_file in sorted(os.listdir(folder_path)):
        print(f"Evaluating {folder_path}/{md_file}")
        if not md_file.endswith(".md"):
            continue
        exp_md = open(os.path.join(folder_path, md_file), "r", encoding="utf-8").read()
        t1 = parse_md_table(exp_md)
        for col in common_cols:
            sims = []
            print(f"\nComparing column '{col}' across all matched pairs")
            for file_name, r2, r1 in row_pairs:
                if file_name != md_file:
                    continue
                v1 = t1.at[r1, col] if (r1 in t1.index and col in t1.columns) else ""
                v2 = ground_truth.at[r2, col] if (r2 in ground_truth.index and col in ground_truth.columns) else ""
                if v1 not in empty_values or v2 not in empty_values:
                    v1, v2 = clean_values(v1, v2)
                    if v1 == v2:
                        sim = 1.0
                    else:
                        emb1 = model.encode(v1, convert_to_tensor=True)
                        emb2 = model.encode(v2, convert_to_tensor=True)
                        sim = util.pytorch_cos_sim(emb1, emb2).item()
                    print(f"  Pair GT {r2} ('{v2}') vs exp {r1} ('{v1}'): {sim:.4f}")
                    sims.append(sim)
            mean_sim = sum(sims) / len(sims) if sims else 0.0
            print(f"Mean similarity for column '{col}': {mean_sim:.4f}")
            metrics.append({
                'file': os.path.basename(md_file),
                'column': col,
                'similarity': mean_sim
            })

    df_metrics = pd.DataFrame(metrics)
    # Compute mean similarity per column across all files
    df_summary = (
        df_metrics
        .groupby('column')['similarity']
        .mean()
        .reset_index()
    )
    df_summary.rename(columns={'similarity': 'mean_similarity'}, inplace=True)
    # Save results per column
    name = folder_path.split("/")[-1]+'_bert.csv'
    output_csv = os.path.join(folder_path,name)
    df_summary.to_csv(output_csv, index=False)
    print(f'Saved mean column results to {output_csv}')


def eval_bert_lexical(t2: pd.DataFrame, row_pairs:list, common_cols: list, folder_path):
    metrics = []
    ontology = Graph()
    ontology.parse(os.path.join(folder_path, '../../ontology.ttl'), format='turtle')
    for md_file in sorted(os.listdir(folder_path)):
        print(f"Evaluating {folder_path}/{md_file}")
        if not md_file.endswith(".md"):
            continue
        exp_md = open(os.path.join(folder_path, md_file), "r", encoding="utf-8").read()
        t1 = parse_md_table(exp_md)
        for col in common_cols:
            sims = []
            print(f"\nComparing column '{col}' across all matched pairs")
            for file_name, r2, r1 in row_pairs:
                if file_name != md_file:
                    continue
                v1 = t1.at[r1, col] if (r1 in t1.index and col in t1.columns) else ""
                v2 = t2.at[r2, col] if (r2 in t2.index and col in t2.columns) else ""
                if v1 not in empty_values or v2 not in empty_values:
                    if v1 == v2:
                        sim = 1.0
                    else:
                        sim = calculate_bert_lex(v1, v2, ontology)
                        print(f"  Pair GT {r2} ('{v2}') vs exp {r1} ('{v1}'): {sim:.4f}")
                    sims.append(sim)
            mean_sim = sum(sims) / len(sims) if sims else 0.0
            print(f"Mean similarity for column '{col}': {mean_sim:.4f}")
            metrics.append({
                'file': os.path.basename(md_file),
                'column': col,
                'similarity': mean_sim
            })

    df_metrics = pd.DataFrame(metrics)
    # Compute mean similarity per column across all files
    df_summary = (
        df_metrics
        .groupby('column')['similarity']
        .mean()
        .reset_index()
    )
    df_summary.rename(columns={'similarity': 'mean_similarity'}, inplace=True)
    # Save results per column
    name = folder_path.split("/")[-1] + '_bert_lexical.csv'
    output_csv = os.path.join(folder_path, name)
    df_summary.to_csv(output_csv, index=False)
    print(f'Saved mean column results to {output_csv}')


def eval_max(t2: pd.DataFrame, row_pairs:list, common_cols: list, folder_path, name:str):
    metrics = []
    ontology = Graph()
    ontology.parse(os.path.join(folder_path, '../ontology.ttl'), format='turtle')
    for md_file in sorted(os.listdir(folder_path)):
        print(f"Evaluating {folder_path}/{md_file}")
        pattern = os.path.join(folder_path, f"*{name}.csv")
        existing = glob.glob(pattern)
        if not md_file.endswith(".md") or existing:
            continue
        exp_md = open(os.path.join(folder_path, md_file), "r", encoding="utf-8").read()
        t1 = parse_md_table(exp_md)
        for col in common_cols:
            sims = []
            print(f"\nComparing column '{col}' across all matched pairs")
            for file_name, r2, r1 in row_pairs:
                if file_name != md_file:
                    continue
                v1 = t1.at[r1, col] if (r1 in t1.index and col in t1.columns) else ""
                v2 = t2.at[r2, col] if (r2 in t2.index and col in t2.columns) else ""
                if v1 not in empty_values or v2 not in empty_values:
                    if v1 == v2:
                        sim = 1.0
                    else:
                        aux_sim = [calculate_bert_lex(v1, v2, ontology), calculate_bert(v1, v2),
                                   calculate_levenshtein(v1, v2)]
                        sim = max(aux_sim)
                        print(f"  Pair GT {r2} ('{v2}') vs exp {r1} ('{v1}'): {sim:.4f}")
                    sims.append(sim)
            mean_sim = sum(sims) / len(sims) if sims else 0.0
            print(f"Mean similarity for column '{col}': {mean_sim:.4f}")
            metrics.append({
                'file': os.path.basename(md_file),
                'column': col,
                'similarity': mean_sim
            })

    df_metrics = pd.DataFrame(metrics)
    # Compute mean similarity per column across all files
    df_summary = (
        df_metrics
        .groupby('column')['similarity']
        .mean()
        .reset_index()
    )
    df_summary.rename(columns={'similarity': 'mean_similarity'}, inplace=True)
    # Save results per column
    name = folder_path.split("/")[-1] + name
    output_csv = os.path.join(folder_path, name)
    df_summary.to_csv(output_csv, index=False)
    print(f'Saved mean column results to {output_csv}')

def eval_max_pr_aggregated(t2: pd.DataFrame,
                           row_pairs: list,
                           common_cols: list,
                           folder_path: str,
                           name:str,
                           threshold: float = 0.8):
    """
    Para cada .md en folder_path, compara t1 vs t2 según row_pairs y common_cols,
    acumula TP/FP/FN por columna en todo el experimento, y al final calcula
    precision, recall y F1‐measure con:
        Precision = TP/(TP+FP)
        Recall    = TP/(TP+FN)
        F1        = 2 * Precision * Recall / (Precision+Recall)
    Escribe un CSV con una fila por columna:
      [column, TP, FP, FN, precision, recall, f1]
    """
    # Cargamos la ontología una sola vez
    ontology = Graph()
    ontology.parse(os.path.join(folder_path, '../ontology.ttl'), format='turtle')

    # Inicializamos contadores por columna
    agg = {col: {'TP': 0, 'FP': 0, 'FN': 0} for col in common_cols}

    # Agrupamos row_pairs por archivo para iterar más rápido
    pairs_by_file = {}
    for fn, r2, r1 in row_pairs:
        pairs_by_file.setdefault(fn, []).append((r2, r1))

    # Recorremos todos los md
    for md_file in sorted(os.listdir(folder_path)):
        if not md_file.endswith(".md"):
            continue

        exp_md = open(os.path.join(folder_path, md_file), "r", encoding="utf-8").read()
        t1 = parse_md_table(exp_md)
        assigned = pairs_by_file.get(md_file, [])

        file_agg = calculate_prf(t1, t2, assigned, common_cols, ontology, threshold)

        for col in common_cols:
            agg[col]['TP'] += file_agg[col]['TP']
            agg[col]['FP'] += file_agg[col]['FP']
            agg[col]['FN'] += file_agg[col]['FN']

    # Tras acumular, construimos la tabla de métricas
    rows = []
    for col, counts in agg.items():
        TP, FP, FN = counts['TP'], counts['FP'], counts['FN']
        precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
        recall    = TP / (TP + FN) if (TP + FN) > 0 else 0.0
        f1        = (2 * precision * recall / (precision + recall)
                     if (precision + recall) > 0 else 0.0)
        rows.append({
            'column':    col,
            'TP':        TP,
            'FP':        FP,
            'FN':        FN,
            'precision': precision,
            'recall':    recall,
            'f1':        f1
        })

    df_summary = pd.DataFrame(rows)
    # Guardamos un CSV por experimento
    out_name   = os.path.basename(folder_path) + f"_{threshold:.2f}_{name}.csv"
    output_csv = os.path.join(folder_path, out_name)
    df_summary.to_csv(output_csv, index=False)
    print(f"Saved aggregated metrics (precision/recall/f1) to {output_csv}")

def calculate_metrics(folder_path, ground_truth ):
    row_pairs, common_cols, row_pair_columns = find_row_matches(folder_path, ground_truth)

    ## Calculate p/r/f-measure based on threshold
    #eval_max_pr_aggregated(ground_truth, row_pairs, common_cols, folder_path, "all", 0.9)
    eval_max_pr_aggregated(ground_truth, row_pairs, common_cols, folder_path, "all", 0.8)
    #eval_max_pr_aggregated(ground_truth, row_pairs, common_cols, folder_path, "all", 0.7)
    #eval_max_pr_aggregated(ground_truth, row_pairs, common_cols, folder_path, "all", 0.6)

    ### Evaluation of similarity
    #eval_levenshtein(ground_truth, row_pairs, common_cols, folder_path)
    #eval_bert(ground_truth, row_pairs, common_cols, folder_path)
    #eval_bert_lexical(ground_truth, row_pairs, common_cols, folder_path)
    eval_max(ground_truth, row_pairs, common_cols, folder_path, "_max_all.csv")
    #eval_max(ground_truth, row_pair_columns, common_cols, folder_path, "_max_gt.csv")
