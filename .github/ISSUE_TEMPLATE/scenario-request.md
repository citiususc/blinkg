---
name: Scenario request
about: Propose a new scenario for the benchmark
title: "[SCENARIO]"
labels: scenario
assignees: dachafra

---

## 1. Scenario summary

**Scenario name:**  
(e.g., GTFS Shapes with extended quality constraints)

**Short description:**  
(2–3 lines describing the goal and main characteristics of the scenario)

**Intended difficulty / focus:**  
(e.g., high schema distance, complex subject generation, heavy use of functions, multi-source join, etc.)

---

## 2. Ontology / vocabularies

**Ontology(ies) and controlled vocabularies used:**

- URI(s) of ontology/vocab(s):
  - e.g., `http://example.org/ontology/gtfs#`
  - e.g., SKOS vocabularies, authority tables, code lists, etc.

**Ontology characteristics:**

- Number of classes and properties:
- Use of SKOS concepts? (yes/no, brief description)
- Use of constraints / shapes (e.g., SHACL, OWL restrictions)?  
- Links to external vocabularies (e.g., `rdfs:seeAlso`, `owl:equivalentClass`)?  

**Files to attach / reference:**

- [ ] Ontology file(s) (RDF serialization)
- [ ] Documentation / specification (if available)

---

## 3. Input data

**Data formats:**

- [ ] CSV
- [ ] JSON
- [ ] XML
- [ ] SQL / relational dump
- [ ] Other (please specify):

**Description of the input data:**

- Number of files:
- Approx. number of entries per file:
- Main attributes / columns / fields and their role:
- Any preprocessing required (e.g., sampling, anonymisation, normalisation):

**Files to attach / reference:**

- [ ] Example input data (or link to source)
- [ ] Schema descriptions (if applicable, e.g., XSD, JSON Schema, SQL DDL)

---

## 4. Ground truth (gold standard)

**Ground truth format(s) provided (multiple allowed):**

- [ ] Tabular format following the BLINKG standard
- [ ] RML mappings
- [ ] SPARQL-Anything queries

**Details:**

- For **tabular format**:  
  - Briefly describe the structure (columns, meaning, how it aligns with BLINKG tasks: class identification, subject generation, property identification, data references, functions, joins, etc.).  
  - Attach or link the table file(s).

- For **RML mappings**:  
  - Version / dialect used (e.g., RML + RML-FNML).  
  - Files attached or link(s) to the mapping documents.

- For **SPARQL-Anything queries**:  
  - Brief description of how the queries are organised (per file/table, per task, etc.).  
  - Files attached or link(s) to the queries.

---

## 5. Tasks covered

Please indicate which BLINKG tasks are covered by this scenario:

- [ ] Ontology Class Identification
- [ ] Subject Generation (simple)
- [ ] Subject Generation (complex / composite)
- [ ] Ontology Property Identification
- [ ] Data Reference Identification (simple)
- [ ] Data Reference Identification (complex / multi-field)
- [ ] Function / transformation specification (e.g., dates, booleans, enums → SKOS)
- [ ] Joins (single-source)
- [ ] Join conditions (multi-source)
- [ ] Other (please describe):

---

## 6. Evaluation considerations

- Suggested evaluation units (e.g., per column, per field, per table, per mapping rule):  
- Any special considerations (e.g., expected use of language tags, composite keys, out-of-distribution schemas, etc.):  

---

## 7. Additional comments

(Anything else maintainers and users should know: relation to existing scenarios, domain motivations, licensing constraints, etc.)

---

**Checklist before submitting**

- [ ] Ontology/vocab files are available and correctly licensed.  
- [ ] Example input data (or a representative sample) is provided.  
- [ ] Ground truth is provided in at least one accepted format (tabular / RML / SPARQL-Anything).  
- [ ] The scenario and tasks are documented clearly enough for others to reproduce the setup.
