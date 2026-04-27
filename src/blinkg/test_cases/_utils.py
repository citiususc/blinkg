from typing import Dict, List, Union
import pandas as pd
from pathlib import Path
from rdflib import Graph
from lxml import etree


def parse_md_table(md_text: str) -> pd.DataFrame:
    import re
    # Split into non-empty lines
    lines = [line.strip() for line in md_text.strip().split('\n') if line.strip()]
    # First line is header, rest are data or delimiter
    header = lines[0]
    data_lines = lines[2:]
    # Split each line by '|' into cells
    rows = [line.strip('|').split('|') for line in [header] + data_lines]
    # Create DataFrame from data rows
    df = pd.DataFrame(rows[1:], columns=rows[0])
    # Trim whitespace in column names
    df.columns = df.columns.str.strip()
    # Drop delimiter rows composed only of hyphens
    df = df[~df.apply(lambda row: all(re.fullmatch(r'-+', cell.strip()) for cell in row), axis=1)]
    # Strip whitespace and remove backticks from each cell
    return df.map(lambda x: str(x).replace('`', '').strip())


def load_inputs(test_dir: Path) -> Dict[str, Union[pd.DataFrame, etree._ElementTree]]:
    """
    Load input data files from a test case directory.

    Args:
        test_dir: Path to test case directory

    Returns:
        Dict mapping filename to parsed data:
        - CSV files -> pd.DataFrame
        - XML files -> lxml.etree._ElementTree
    """
    input_data = {}

    # Load CSV files
    for csv_file in test_dir.glob("*.csv"):
        input_data[csv_file.name] = pd.read_csv(csv_file)

    # Load XML files
    for xml_file in test_dir.glob("*.xml"):
        parser = etree.XMLParser(recover=True)
        input_data[xml_file.name] = etree.parse(str(xml_file), parser)

    return input_data


def load_ontology(test_dir: Path, filename: str) -> Graph:
    ontology = Graph()
    ontology_file = test_dir / filename

    if not ontology_file.exists():
        raise FileNotFoundError(f"Ontology file not found: {ontology_file}")

    ontology.parse(ontology_file, format="turtle")
    return ontology


def load_skos(ontology: Graph, test_dir: Path, filename: str) -> None:
    """Merge SKOS file into ontology graph if present."""
    skos_file = test_dir / filename
    if skos_file.exists():
        ontology.parse(skos_file, format="turtle")


def load_ground_truth(test_dir: Path) -> pd.DataFrame:
    expected_table = test_dir / "expected_table.md"

    if not expected_table.exists():
        raise FileNotFoundError(f"Ground truth not found: {expected_table}")

    return parse_md_table(expected_table.read_text(encoding='utf-8'))


def list_test_cases_in(scenario_dir: Path) -> List[str]:
    if not scenario_dir.exists():
        raise FileNotFoundError(f"Scenario directory not found at {scenario_dir}")

    test_cases = []
    for subdir in sorted(scenario_dir.iterdir()):
        if subdir.is_dir() and (subdir / "expected_table.md").exists():
            test_cases.append(subdir.name)

    return test_cases
