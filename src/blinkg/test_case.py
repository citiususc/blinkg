from dataclasses import dataclass
from typing import List, Dict
import pandas as pd
from rdflib import Graph


@dataclass
class TestCase:
    """
    Benchmark test case for evaluating KG mapping approaches.

    Attributes:
        id: Unique identifier (e.g., 'scenario1_1A')
        description: Human-readable description
        input_data: Source data as DataFrames (filename -> DataFrame)
        ontology: Target ontology (RDF Graph, includes SKOS)
        ground_truth: Expected mappings (DataFrame)
    """
    id: str
    description: str
    input_data: Dict[str, pd.DataFrame]
    ontology: Graph
    ground_truth: pd.DataFrame


def list_test_cases() -> List[str]:
    from .test_cases._loader import list_all_test_cases
    return list_all_test_cases()


def load_test_case(test_case_id: str) -> TestCase:
    from .test_cases._loader import load_test_case_from_disk
    return load_test_case_from_disk(test_case_id)
