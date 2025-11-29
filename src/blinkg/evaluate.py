import Levenshtein
from .utils import *
import numpy as np
from sentence_transformers import util
from rdflib import Graph
import re

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

def match_tables(t1: pd.DataFrame, t2: pd.DataFrame):
    """
    Match rows between prediction (t1) and ground truth (t2) DataFrames.
    Returns: (pairs, common_cols, pairs_column)
      - pairs: list of (r2, r1) tuples for pred→gt matching
      - common_cols: list of common column names
      - pairs_column: list of (r2, r1) tuples for gt→pred matching
    """
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
    pairs = []
    pairs_column = []

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
                candidate_idxs = sims[sims > threshold].index
                for r2 in candidate_idxs:
                    j = t2.index.get_loc(r2)
                    if j not in used_gt:
                        r1 = t1.index[t1[h1] == val][0]
                        matched_val = t2.at[r2, h2]
                        sim_score = sims[r2]
                        i = t1.index.get_loc(r1)
                        pairs.append((r2, r1))
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
            if i in used_pred or j in used_gt:
                cost_matrix[i, j] = 1.0
                continue

            v1_list = []
            v2_list = []
            for key in metrics_keys:
                h1, h2 = mapping_pred[key], mapping_gt[key]
                v1 = t1.at[r1, h1] if h1 in t1.columns else ""
                v2 = t2.at[r2, h2] if h2 in t2.columns else ""
                if v1 and v2 and v1 not in empty_values and v2 not in empty_values:
                    v1_list.append(v1)
                    v2_list.append(v2)

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
        pairs.append((r2, r1))

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
        pairs_column.append((r2, r1))
        print(f"  GT row '{r2}' → EXP row '{r1}' (sim={sim:.4f})")

    return pairs, common_cols, pairs_column


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

def calculate_prf(t1: pd.DataFrame,
                  t2: pd.DataFrame,
                  assigned_pairs: list,
                  common_cols: list,
                  ontology: Graph,
                  threshold: float = 0.8):
    """
    Calculate precision/recall/F1 for each column based on assigned row pairs.
    Returns: dict mapping column -> {'TP': int, 'FP': int, 'FN': int, 'precision': float, 'recall': float, 'f1': float}
    """
    agg = {col: {'TP': 0, 'FP': 0, 'FN': 0} for col in common_cols}

    for col in common_cols:
        # Matched pairs
        for r2, r1 in assigned_pairs:
            if col not in t1.columns or col not in t2.columns:
                continue
            v1, v2 = str(t1.at[r1, col]), str(t2.at[r2, col])
            if v1 in empty_values or v2 in empty_values:
                continue
            sims = [
                calculate_levenshtein(v1, v2),
                calculate_bert(v1, v2),
                calculate_bert_lex(v1, v2, ontology)
            ]
            sim = max(sims)
            if sim >= threshold:
                agg[col]['TP'] += 1
            else:
                agg[col]['FN'] += 1

        # Unmatched predicted rows
        used_r1 = {r1 for _, r1 in assigned_pairs}
        for r1 in t1.index:
            if r1 in used_r1 or col not in t1.columns:
                continue
            v1 = str(t1.at[r1, col])
            if v1 in empty_values:
                continue
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
            if best_sim >= threshold:
                agg[col]['FP'] += 1

    # Calculate P/R/F1 from counts
    for col in agg:
        tp, fp, fn = agg[col]['TP'], agg[col]['FP'], agg[col]['FN']
        agg[col]['precision'] = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        agg[col]['recall'] = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        p, r = agg[col]['precision'], agg[col]['recall']
        agg[col]['f1'] = 2 * p * r / (p + r) if (p + r) > 0 else 0.0

    return agg
