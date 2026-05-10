from typing import List
import re
from ..test_case import TestCase
from ..scenarios import SCENARIOS_PATH
from ._utils import (
    load_inputs,
    load_ontology,
    load_skos,
    load_ground_truth,
    list_test_cases_in
)


SCENARIO_REGISTRY = {
    'scenario1': {
        'description': 'Schema-Aligned Mapping',
        'ontology': 'ontology.ttl',
        'skos': None,
        'input_format': 'csv',
    },
    'scenario2': {
        'description': 'GTFS Functional Mapping',
        'ontology': 'ontology_{test_case}.ttl',
        'skos': 'skos_{test_case}.ttl',
        'input_format': 'csv',
    },
    'scenario3': {
        'description': 'Schema-Distant High Abstraction',
        'ontology': 'ontology.ttl',
        'skos': 'skos.ttl',
        'input_format': 'xml',
    },
}


def list_all_test_cases() -> List[str]:
    test_case_ids = []

    for scenario_name in SCENARIO_REGISTRY.keys():
        scenario_path = SCENARIOS_PATH / scenario_name
        try:
            test_cases = list_test_cases_in(scenario_path)
            for test_case in test_cases:
                test_case_ids.append(f"{scenario_name}_{test_case}")
        except FileNotFoundError:
            continue

    return test_case_ids


def load_test_case_from_disk(test_case_id: str) -> TestCase:
    match = re.match(r'(scenario\d+)_(.+)', test_case_id)
    if not match:
        raise ValueError(
            f"Invalid test case ID format: '{test_case_id}'. "
            f"Expected format: 'scenario1_1A', 'scenario2_d1', etc."
        )

    scenario_name = match.group(1)
    test_case = match.group(2)

    if scenario_name not in SCENARIO_REGISTRY:
        raise ValueError(f"Unknown scenario: '{scenario_name}'")

    config = SCENARIO_REGISTRY[scenario_name]
    test_dir = SCENARIOS_PATH / scenario_name / test_case

    if not test_dir.exists():
        raise FileNotFoundError(f"Test case '{test_case_id}' not found at {test_dir}")

    input_data = load_inputs(test_dir, config['input_format'])

    ontology_file = config['ontology'].format(test_case=test_case)
    ontology = load_ontology(test_dir, ontology_file)

    if config['skos']:
        skos_file = config['skos'].format(test_case=test_case)
        load_skos(ontology, test_dir, skos_file)

    ground_truth = load_ground_truth(test_dir)

    description = f"Scenario {scenario_name[-1]}: {config['description']} - Test Case {test_case}"

    return TestCase(
        id=test_case_id,
        description=description,
        input_data=input_data,
        ontology=ontology,
        ground_truth=ground_truth
    )
