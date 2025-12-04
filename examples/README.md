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

The script with the example files must be called as it follows:

```bash
python3 prompt_template.py -i routes.csv agency.csv -g ontology_d1.ttl -s skos_d1.ttl
```

## Prompt inference (inference)

This section demonstrates how run a prompt with a LLM from the HuggingFace platform using the ```src/blinkg/execution/hf_inference.py``` script. The folder includes an prompt from Scenario 2 and an example output obtained with the script.

The script in this case must be called as it follow:

```bash
python3 hf_inference.py prompt.txt -m 0
```
(Model identifiers are 0 for *Llama-3.3-70B-Instruct* and 1 for *Mixtral-8x22B-Instruct-v0.1 models*)