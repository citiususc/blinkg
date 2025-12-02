| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Student | `ex:fullname` | `ex:Person` | - | `ex:student_{Student}` | - |
| Sport | `ex:sportname` | `ex:Sport` | - | `ex:sport_{Sport}` | - |
| - | `ex:practises` | `ex:Person` | `ex:Sport` | `ex:student_{Student}` | The entities are in the same row. |
