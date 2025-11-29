"""
Example of using BLINKG programmatically to evaluate predictions.
"""
from blinkg import evaluate
from rdflib import Graph
import pandas as pd

# Example: Load ground truth
ground_truth = pd.DataFrame({
    "CSV Column": ["id", "name", "age"],
    "Ontology Property": ["schema:identifier", "schema:name", "schema:age"],
    "Entity Class": ["schema:Person", "schema:Person", "schema:Person"],
})

# Example: Your predictions
# This would come from your mapping tool output
predictions = pd.DataFrame({
    "CSV Column": ["id", "name", "age"],
    "Ontology Property": ["schema:identifier", "schema:name", "schema:age"],
    "Entity Class": ["schema:Person", "schema:Person", "schema:Person"],
})

# Load ontology
ontology = Graph()
# ontology.parse("path/to/your/ontology.ttl", format="turtle")
# For this example, we'll use an empty graph
ontology.parse(data="@prefix schema: <http://schema.org/> .", format="turtle")

# Evaluate predictions against ground truth
print("Running BLINKG evaluation...")
metrics = evaluate(predictions, ground_truth, ontology, threshold=0.8)

# Display results
print("\n=== Evaluation Results ===")
for col, m in metrics.items():
    print(f"\n{col}:")
    print(f"  Precision: {m['precision']:.3f}")
    print(f"  Recall:    {m['recall']:.3f}")
    print(f"  F1:        {m['f1']:.3f}")
    print(f"  TP: {m['TP']}, FP: {m['FP']}, FN: {m['FN']}")

print("\nEvaluation complete!")
