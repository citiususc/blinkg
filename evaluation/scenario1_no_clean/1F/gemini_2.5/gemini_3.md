| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| :--- | :--- | :--- | :--- | :--- | :--- |
| student.csv.ID | ex:id | ex:Person | - | ex:person/{ID} | - |
| student.csv.FirstName | ex:firstname | ex:Person | - | ex:person/{ID} | - |
| student.csv.LastName | ex:lastname | ex:Person | - | ex:person/{ID} | - |
| sport.csv.ID | ex:sportid | ex:Sport | - | ex:sport/{ID} | - |
| sport.csv.Description | ex:sportname | ex:Sport | - | ex:sport/{ID} | - |
| student_sport.csv | ex:practises | ex:Person | ex:Sport | ex:person/{ID_Student} | student.csv.ID = student_sport.csv.ID_Student AND sport.csv.ID = student_sport.csv.ID_Sport |
