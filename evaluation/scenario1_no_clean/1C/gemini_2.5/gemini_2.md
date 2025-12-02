| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Student | ex:fullname | ex:Person | - | ex:student_{Student} | - |
| Sport | ex:sportname | ex:Sport | - | ex:sport_{Sport} | - |
| (Student, Sport) | ex:practises | ex:Person | ex:Sport | Subject: ex:student_{Student}<br>Object: ex:sport_{Sport} | Each row in the CSV defines a relationship. |
