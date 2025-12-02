# BLINKG: Benchmark for LLM-Integrated Knowledge Graph Generation

We present BLINKG, a benchmark for testing the capabilities of automatic solutions for the construction of
knowledge graphs from (semi)structured data. It provides:

- **Realistic scenarios**: A suite of progressively complex use cases, drawn from real-world data integration tasks, that challenge automatic solutions to align source fields with ontology concepts.

- **Standardized evaluation**: Clear metrics and gold-standard mappings to quantify precision, recall and overall mapping quality.

- **Extensible framework**: Standard data formats and evaluation scripts so that researchers can plug in new models, prompts or data sources in minutes.


## Benchmark Resources
We have divided the benchmark en three different scenarios, increasing their complexity. They can be found in the folder `scenarios`:

- Scenario 1: Schema-Aligned Mapping:
The structure and vocabulary of the input data closely match the target ontology. Mapping tasks involve straightforward identification of classes, properties, and entities. This scenario represents low-complexity environments where LLMs can operate with minimal ambiguity.

- Scenario 2: Functional and Partially Aligned Mapping:
Input data includes functional transformations and moderate divergence from the ontology schema. Tasks require interpreting formatting, value normalization, and simple logic operations. It models real-world cases with medium complexity in mapping design.

- Scenario 3: Schema-Distant and High Abstraction Mapping:
Input schemas and ontologies have minimal structural or lexical overlap. Tasks demand abstraction, contextual reasoning, and domain understanding to derive correct mappings. This scenario simulates the most challenging conditions for semantic alignment.

Tested features distributed by each scenario. Scenario 1 is divided in several atomic cases, while Scenarios 2 and 3 represent realistic KG construction scenarios:

| Features/Scenarios         | 1A | 1B | 1C | 1D | 1E | 1F | 1G | 1H | Scenario 2 GTFS | Scenario 3 PPDS |
|:--------------------------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---------------:|:---------------:|
| One data reference         | x  | x  | x  | x  | x  | x  | x  | x  | x               | x               |
| Two or more data references|    | x  | x  | x  | x  | x  | x  | x  | x               | x               |
| Complex object generation  |    |    |    | x  |    | x  | x  |    | x               | x               | 
| Simple subject generation  | x  | x  | x  |    | x  |    |    | x  | x               | x               |
| Complex subject generation |    |    |    | x  |    | x  | x  |    | x               | x               |
| Self join                  |    |    | x  |    |    |    | x  |    | x               | x               |
| Conditional join           |    |    |    |    | x  | x  | x  |    | x               | x               |
| Two or more input sources  |    |    |    |    |    | x  | x  | x  | x               | x               |
| Duplicate entities         |    |    |    | x  |    |    | x  | x  | x               | x               | 
| Datatypes generation       |    |    |    | x  |    |    | x  | x  | x               | x               |
| Language annotations       |    |    |    |    |    |    | x  | x  | x               | x               |
| Transformation Functions   |    |    |    |    |    |    |    |    | x               | x               |
| Distant Schemes            |    |    |    |    |    |    |    |    |                 | x               |

## Benchmark Metrics

### Cell similarity 
To assess the quality of the mappings produced by LLMs, we define a flexible and task-sensitive evaluation metric based on semantic similarity. Instead of relying solely on exact string matches, which often fail to recognize paraphrases or synonymous terms, we compute three complementary similarity scores between predicted and reference values:
- Levenshtein distance (normalized): captures character-level similarity.
- Cosine similarity over raw embeddings: using SBERT or any similar LM to compare textual outputs semantically.
- Cosine similarity over ontology verbalizations: comparing descriptions or labels of ontology elements.

For each cell in a predicted table, the metric selects the maximum similarity among these three and compares it against a threshold τ. If the score exceeds the threshold, the annotation is marked as correct. This allows the metric to be robust across tasks of varying complexity—such as class matching, datatype identification, or join condition specification—while remaining sensitive to lexical variation.

### Row matchting
Before evaluating the predicted tables, each generated row must be aligned with the corresponding gold standard row. Since LLMs may reorder or transform input data, a direct row-by-row comparison is unreliable. To address this, we implement a semantic row matching step.
The primary matching criterion is the Ontology Property, as it usually contains uniquely identifying values per row. We compute similarity using multiple measures (Levenshtein distance, embedding-based cosine similarity, and ontology verbalization similarity) to find the closest match.
If the Ontology Property is ambiguous or insufficiently discriminative (e.g., contains repeated or noisy values), we fall back to a composite key using Entity Class and Data Reference, which we identified empirically as the most informative pair of fields across scenarios.
This step ensures that each predicted row is compared against the most appropriate reference, minimizing false negatives due to misalignment.

## How can I add a different LLM model to the comparison? And how can I create a new scenario?

To replicate the procedure, you can use the script ```hf_inference.py``` from the ```src/executions/hf``` folder. This script allows you to add any model that supports inference in HuggingFace to the comparison. In our comparison, it has been used for the *Llama-3.3-70B-Instruct* and *Mixtral-8x22B-Instruct-v0.1 models*.

In order to use it, you can add the model to the ```MODEL_OPTIONS``` dictionary. 

The recommended procedure is creating a virtual environment and installing Huggingface Hub.

```bash
sudo apt install python3-venv
python3 -m venv .blinkg
source .blinkg/bin/activate
pip install -e .[examples]
```

To run the script, you must pass as arguments the prompt file, the chosen model from the dictionary list, and the name of the output file (if not passed, “output.txt” will be used).

```bash
python3 hf_inference.py prompt.txt -m 0 -o your_output_file.txt
```

With the inference script, the only thing needed to adding a LLM or creating a new scenario is a new prompt. Users can use their own prompt, but one example prompt from Scenario 2 is given in the ```src/execution/example``` folder. This prompt was generated using the script ```promtp_template.py``` from the ```src/execution``` folder. All the input files are in the ```example``` folder.  

The script must be called as follows:

```bash
python3 prompt_template.py -i input_file1 input_file2 -g ontology_file -s skos_file -o output_file
```

It's mandatory to introduce at least one input file and the ontology file. If no output file is provided, prompt.txt will be used.

## How can I use BLINKG as a library

You can use BLINKG as a library in your own code. After installing with:

```bash
pip install git+https://github.com/citiususc/blinkg.git
```

Use the `evaluate()` function to evaluate your mapping predictions against ground truth. See ```examples/lib/main.py``` for a complete working example. 

## Results
Results of our evaluation can be found in folder ```evaluation```.

## Authors

- David Chaves-Fraga (main contact) - david.chaves at usc.es
- Carla Castedo [@carlacastedo]https://github.com/carlacastedo
- Javier Garea Cidre [@javiergarea](https://github.com/javiergarea)


CiTIUS - University of Santiago de Compostela, July 2025 - Present
