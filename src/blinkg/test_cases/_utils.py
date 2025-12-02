from typing import Dict, List
import pandas as pd
from pathlib import Path
from rdflib import Graph


def parse_md_table(md_text: str) -> pd.DataFrame:
    lines = [line.strip() for line in md_text.strip().split('\n') if line.strip()]

    if len(lines) < 2:
        raise ValueError("Markdown table must have at least header and separator rows")

    headers = [h.strip() for h in lines[0].split('|') if h.strip()]

    data = []
    for line in lines[2:]:
        row = [cell.strip() for cell in line.split('|') if cell.strip()]
        if len(row) == len(headers):
            data.append(row)

    return pd.DataFrame(data, columns=headers)


def get_scenarios_base() -> Path:
    module_dir = Path(__file__).parent
    repo_root = module_dir.parent.parent.parent
    scenarios_dir = repo_root / "scenarios"

    if not scenarios_dir.exists():
        raise FileNotFoundError(f"Scenarios directory not found at {scenarios_dir}")

    return scenarios_dir


def load_csv_inputs(test_dir: Path) -> Dict[str, pd.DataFrame]:
    input_data = {}
    for csv_file in test_dir.glob("*.csv"):
        input_data[csv_file.name] = pd.read_csv(csv_file)
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
