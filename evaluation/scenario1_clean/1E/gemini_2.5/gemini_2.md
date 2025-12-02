| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| :--- | :--- | :--- | :--- | :--- | :--- |
| student.csv: ID | ex:id | ex:Person | | ex:Person_{ID} | |
| student.csv: Name | ex:fullname | ex:Person | | ex:Person_{ID} | |
| student.csv: Sport | ex:practises | ex:Person | ex:Sport | ex:Person_{ID} | student.csv.Sport == sport.csv.ID |
| sport.csv: ID | ex:sportid | ex:Sport | | ex:Sport_{ID} | |
| sport.csv: Name | ex:sportname | ex:Sport | | ex:Sport_{ID} | |
