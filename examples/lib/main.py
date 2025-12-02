"""
Example of using BLINKG programmatically to evaluate predictions.
"""
from blinkg import evaluate, load_test_case, list_test_cases

# List available test cases
test_case_ids = list_test_cases()
print("Available test cases:", test_case_ids)

# Load a benchmark test case
test_case = load_test_case(test_case_ids[0])
print(f"\nLoaded: {test_case.description}")
print(f"Input files: {list(test_case.input_data.keys())}")

# Your predictions (for this example, we use ground truth for perfect score)
predictions = test_case.ground_truth.copy()

# Evaluate predictions against ground truth
print("Running BLINKG evaluation...")
metrics = evaluate(predictions, test_case.ground_truth, test_case.ontology, threshold=0.8)

# Display results
print("\n=== Evaluation Results ===")
for col, m in metrics.items():
    print(f"\n{col}:")
    print(f"  Precision: {m['precision']:.3f}")
    print(f"  Recall:    {m['recall']:.3f}")
    print(f"  F1:        {m['f1']:.3f}")
    print(f"  TP: {m['TP']}, FP: {m['FP']}, FN: {m['FN']}")
