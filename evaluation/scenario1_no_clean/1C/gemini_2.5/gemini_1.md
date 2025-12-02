| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Student | ex:fullname | ex:Person | - | ex:person_{Student} | - |
| Sport | ex:sportname | ex:Sport | - | ex:sport_{Sport} | - |
| Student, Sport | ex:practises | ex:Person | ex:Sport | - | The relationship is defined by each row, linking the subject `ex:person_{Student}` with the object `ex:sport_{Sport}`. |
