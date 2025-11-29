"""BLINKG: Benchmark for LLM-Integrated Knowledge Graph Generation"""

from .evaluate import match_tables, calculate_prf
from rdflib import Graph
import pandas as pd

__version__ = "0.1.0"


def evaluate(predictions: pd.DataFrame,
             ground_truth: pd.DataFrame,
             ontology: Graph,
             threshold: float = 0.8):
    """
    Evaluate predictions against ground truth.

    Args:
        predictions: DataFrame with predicted mappings
        ground_truth: DataFrame with expected mappings
        ontology: RDFLib Graph with the ontology
        threshold: Similarity threshold for TP/FP/FN (default: 0.8)

    Returns:
        dict: Metrics per column with format:
            {column_name: {'TP': int, 'FP': int, 'FN': int,
                          'precision': float, 'recall': float, 'f1': float}}
    """
    pairs, common_cols, _ = match_tables(predictions, ground_truth)
    metrics = calculate_prf(predictions, ground_truth, pairs, common_cols, ontology, threshold)
    return metrics
