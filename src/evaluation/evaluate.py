import os
import Levenshtein
from utils import *
import numpy as np
from sentence_transformers import util
from rdflib import Graph
import re
import glob
# Patterns to detect canonical fields regardless of exact header text
_field_patterns = {
    #'column': re.compile(r'\bcsv\s*_?\s*column\b|\bcolumn\b', re.IGNORECASE),
    'column': re.compile(r'\bXML\s*_?\s*Path\b|\bPath\b', re.IGNORECASE),
    'ontology_prop': re.compile(r'\bontology\s*_?\s*property\b|\bprop(er)?\b', re.IGNORECASE),
    'entity_class': re.compile(r'\bentity\s*_?\s*class\b|\bclass\b', re.IGNORECASE),
    'related_entity_class': re.compile(
        r'\brelated\s*_?\s*entity\s*_?\s*class\b|\bobject\s*_?\s*property\b',
        re.IGNORECASE
    ),
    'subject_generation': re.compile(
        r'\b(subject\s*_?\s*generation|uri|template)\b',
        re.IGNORECASE
    ),
    'datatype': re.compile(r'\b(datatype|data\s*_?\s*type|dtype)\b', re.IGNORECASE),
    'join_condition': re.compile(
        r'\bjoin\s*_?\s*condition\b|\bjoin\b',
        re.IGNORECASE
    ),
}

def get_header_mapping(headers):
    mapping = {}
    for key, pat in _field_patterns.items():
        for h in headers:
            if pat.search(h):
                mapping[key] = h
                break
    return mapping



def normalized_levenshtein(s1: str, s2: str) -> float:
    """
    Compute normalized Levenshtein similarity in [0,1].
    """
    dist = Levenshtein.distance(s1, s2)
    max_len = max(len(s1), len(s2), 1)
    return 1.0 - dist / max_len

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

        # Header mappings
        mapping_pred = get_header_mapping(list(t1.columns))
        mapping_gt   = get_header_mapping(list(t2.columns))
        all_keys = ['column', 'ontology_prop', 'entity_class']
        metrics_keys = [k for k in all_keys if k in mapping_pred and k in mapping_gt]

        # Common cols
        common_cols = [c for c in sorted(set(t1.columns)|set(t2.columns)) if c != 'index']

        # Prepare used-sets
        used_pred = set()
        used_gt   = set()

        # === 1) FAST-PATH UNIQUE ONTOLOGY_PROP MATCHES ===
        if 'ontology_prop' in metrics_keys:
            h1 = mapping_pred['ontology_prop']
            h2 = mapping_gt['ontology_prop']
            if h1 in t1.columns and h2 in t2.columns:
                threshold = 0.9
                vc1 = t1[h1].value_counts()
                uniques_pred = vc1[vc1 == 1].index
                for val in uniques_pred:
                    sims = t2[h2].apply(lambda v2: max(normalized_levenshtein(val, v2),calculate_bert(val,v2)))
                    # get all candidate ground-truth indices with sim > threshold
                    candidate_idxs = sims[sims > threshold].index
                    # find the first unused candidate
                    for r2 in candidate_idxs:
                        j = t2.index.get_loc(r2)
                        if j not in used_gt:
                            # perform the match
                            r1 = t1.index[t1[h1] == val][0]
                            matched_val = t2.at[r2, h2]
                            sim_score = sims[r2]
                            i = t1.index.get_loc(r1)
                            row_pairs.append((md_file, r2, r1))
                            used_pred.add(i)
                            used_gt.add(j)
                            print(
                                f"  [FAST] matched pred='{val}' ↔ gt='{matched_val}' "
                                f"(sim={sim_score:.3f}) → EXP {r1} ↔ GT {r2}"
                            )
                            break

        # === 2) BUILD FULL COST MATRIX ===
        n_pred, n_gt = len(t1), len(t2)
        cost_matrix = np.zeros((n_pred, n_gt))
        for i, r1 in enumerate(t1.index):
            for j, r2 in enumerate(t2.index):
                # skip pairs already matched
                if i in used_pred or j in used_gt:
                    cost_matrix[i, j] = 1.0  # max cost = skip in next step
                    continue

                # gather values for metrics_keys
                v1_list = []
                v2_list = []
                for key in metrics_keys:
                    h1, h2 = mapping_pred[key], mapping_gt[key]
                    v1 = t1.at[r1, h1] if h1 in t1.columns else ""
                    v2 = t2.at[r2, h2] if h2 in t2.columns else ""
                    if v1 and v2 and v1 not in empty_values and v2 not in empty_values:
                        v1_list.append(v1)
                        v2_list.append(v2)

                # compute similarity
                if ", ".join(v1_list) == ", ".join(v2_list):
                    sim = 1.0
                else:
                    sim_lev = normalized_levenshtein(", ".join(v1_list), ", ".join(v2_list))
                    sim_bert = calculate_bert(", ".join(v1_list), ", ".join(v2_list))
                    sim = max(sim_lev, sim_bert)

                cost_matrix[i, j] = 1.0 - sim

        # === 3) ASSIGN REMAINING PREDICTED ROWS ===
        for i, r1 in enumerate(t1.index):
            if i in used_pred:
                continue
            sorted_js = np.argsort(cost_matrix[i])
            # pick best unused GT row
            for j_best in sorted_js:
                if j_best not in used_gt:
                    used_pred.add(i)
                    used_gt.add(j_best)
                    break
            else:
                j_best = sorted_js[0]
                used_pred.add(i)
                used_gt.add(j_best)

            r2 = t2.index[j_best]
            sim = 1.0 - cost_matrix[i, j_best]

            # Reconstruct the values used for matching
            v1_list, v2_list = [], []
            for key in metrics_keys:
                h1, h2 = mapping_pred[key], mapping_gt[key]
                v1 = t1.at[r1, h1] if h1 in t1.columns else ""
                v2 = t2.at[r2, h2] if h2 in t2.columns else ""
                if v1 and v2 and v1 not in empty_values and v2 not in empty_values:
                    v1_list.append(v1)
                    v2_list.append(v2)
            v1_str = ", ".join(v1_list)
            v2_str = ", ".join(v2_list)

            print(
                f"  EXP row '{r1}' → GT row '{r2}' "
                f"(sim={sim:.4f})\n"
                f"    matched values: pred=\"{v1_str}\"  gt=\"{v2_str}\""
            )
            row_pairs.append((md_file, r2, r1))

        # === 4) ASSIGN REMAINING GT ROWS BACK TO PREDICTED ===
        used_pred2 = set()
        for j, r2 in enumerate(t2.index):
            if j in used_gt:
                continue
            sorted_i = np.argsort(cost_matrix[:, j])
            for i_best in sorted_i:
                if i_best not in used_pred2:
                    used_pred2.add(i_best)
                    break
            else:
                i_best = sorted_i[0]
                used_pred2.add(i_best)

            r1 = t1.index[i_best]
            sim = 1.0 - cost_matrix[i_best, j]
            row_pairs_column.append((md_file, r2, r1))
            print(f"  GT row '{r2}' → EXP row '{r1}' (sim={sim:.4f})")

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
                        v1 = expand_to_full_uri(v1)
                        v2 = expand_to_full_uri(v2)
                        lex_v1, lex_v2 = get_property_lexicalization(v1, ontology), get_property_lexicalization(v2,ontology)
                        if lex_v1 == v1 and lex_v2 == v2:
                            v1, v2 = strip_shared_prefixes(v1, v2)
                        else:
                            v1, v2 = lex_v1, lex_v2
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
    name = folder_path.split("/")[-1] + '_bert_lexical.csv'
    output_csv = os.path.join(folder_path, name)
    df_summary.to_csv(output_csv, index=False)
    print(f'Saved mean column results to {output_csv}')


def calculate_bert_lex(v1, v2, ontology):
    v1 = expand_to_full_uri(v1)
    v2 = expand_to_full_uri(v2)
    lex_v1, lex_v2 = get_property_lexicalization(v1, ontology), get_property_lexicalization(v2, ontology)
    if lex_v1 == v1 and lex_v2 == v2:
        v1, v2 = strip_shared_prefixes(v1, v2)
    else:
        v1, v2 = lex_v1, lex_v2
    emb1 = model.encode(v1, convert_to_tensor=True)
    emb2 = model.encode(v2, convert_to_tensor=True)
    sim = util.pytorch_cos_sim(emb1, emb2).item()
    return sim

def calculate_bert(v1, v2):
    v1, v2 = clean_values(v1, v2)
    emb1 = model.encode(v1, convert_to_tensor=True)
    emb2 = model.encode(v2, convert_to_tensor=True)
    sim = util.pytorch_cos_sim(emb1, emb2).item()
    return sim

def calculate_levenshtein(v1, v2):
    v1, v2 = clean_values(v1, v2)
    sim = normalized_levenshtein(v1, v2)
    return sim

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

        for col in common_cols:
            # Primer pase: los que fueron emparejados (matched)
            for r2, r1 in assigned:
                if col not in t1.columns or col not in t2.columns:
                    continue
                v1, v2 = str(t1.at[r1, col]), str(t2.at[r2, col])
                if v1 in empty_values or v2 in empty_values:
                    continue
                # calculamos la similitud máxima
                sims = [
                    calculate_levenshtein(v1, v2),
                    calculate_bert(v1, v2),
                    calculate_bert_lex(v1, v2, ontology)
                ]
                sim = max(sims)
                # TP o FN
                if sim >= threshold:
                    agg[col]['TP'] += 1
                else:
                    agg[col]['FN'] += 1

            # Segundo pase: predichos no emparejados → posibles FP
            used_r1 = {r1 for _, r1 in assigned}
            for r1 in t1.index:
                if r1 in used_r1 or col not in t1.columns:
                    continue
                v1 = str(t1.at[r1, col])
                if v1 in empty_values:
                    continue
                # buscamos mejor sim en todo t2
                best_sim = 0.0
                for r2 in t2.index:
                    if col not in t2.columns:
                        continue
                    v2 = str(t2.at[r2, col])
                    if v2 in empty_values:
                        continue
                    sims = [
                        calculate_levenshtein(v1, v2),
                        calculate_bert(v1, v2),
                        calculate_bert_lex(v1, v2, ontology)
                    ]
                    best_sim = max(best_sim, max(sims))
                # si ese mejor sim supera el umbral → FP
                if best_sim >= threshold:
                    agg[col]['FP'] += 1

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