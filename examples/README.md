# Usage examples

## Programmatic usage (lib)

This section demonstrates how to use BLINKG as a library for evaluating knowledge graph mappings programmatically.

The example illustrates the core evaluation workflow:
1. Listing available test cases from the benchmark scenarios
2. Loading a specific test case with its input data, ground truth, and ontology
3. Evaluating predicted mappings against gold-standard references using the `evaluate()` function
4. Analyzing results with detailed metrics including precision, recall, F1 scores, and confusion matrix values


## Prompt generation (prompt)

This section demonstrates how to generate a new prompt using our prompt template script ```src/blinkg/execution/prompt_template.py```. The folder includes two input data files, one ontology file and one skos files from Scenario 2. It also includes a prompt.txt that was generated as output from the script.

The script must be called with the example files as it follows:

```bash
python3 prompt_template.py -i routes.csv agency.csv -g ontology_d1.ttl -s skos_d1.ttl
```

## Prompt inference (inference)
