| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| :--- | :--- | :--- | :--- | :--- | :--- |
| student.csv: ID | ex:id | ex:Person | | `ex:person/{ID}` | |
| student.csv: Name | ex:fullname | ex:Person | | `ex:person/{ID}` | |
| student.csv: Sport | ex:practises | ex:Person | ex:Sport | `ex:person/{ID}` | student.csv:Sport = sport.csv:ID |
| sport.csv: ID | ex:sportid | ex:Sport | | `ex:sport/{ID}` | |
| sport.csv: Name | ex:sportname | ex:Sport | | `ex:sport/{ID}` | |
