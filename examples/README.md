# Usage examples

## Programmatic usage (lib)

This section demonstrates how to use BLINKG as a library for evaluating knowledge graph mappings programmatically.

The example illustrates the core evaluation workflow:
1. Listing available test cases from the benchmark scenarios
2. Loading a specific test case with its input data, ground truth, and ontology
3. Evaluating predicted mappings against gold-standard references using the `evaluate()` function
4. Analyzing results with detailed metrics including precision, recall, F1 scores, and confusion matrix values
