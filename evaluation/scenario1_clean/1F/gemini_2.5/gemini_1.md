| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ID | ex:id | ex:Person | | http://example.org/person/{ID} | |
| FirstName | ex:firstname | ex:Person | | http://example.org/person/{ID} | |
| LastName | ex:lastname | ex:Person | | http://example.org/person/{ID} | |
| ID | ex:sportid | ex:Sport | | http://example.org/sport/{ID} | |
| Description | ex:sportname | ex:Sport | | http://example.org/sport/{ID} | |
| ID_Student | ex:practises | ex:Person | ex:Sport | http://example.org/person/{ID_Student} | student.ID == student_sport.ID_Student and sport.ID == student_sport.ID_Sport |
