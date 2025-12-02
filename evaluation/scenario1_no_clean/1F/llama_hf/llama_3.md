| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| --- | --- | --- | --- | --- | --- |
| ID (student.csv) | ex:id | ex:Person | - | http://example.org/person/{ID} | - |
| FirstName (student.csv) | ex:firstname | ex:Person | - | http://example.org/person/{ID} | - |
| LastName (student.csv) | ex:lastname | ex:Person | - | http://example.org/person/{ID} | - |
| ID (sport.csv) | ex:sportid | ex:Sport | - | http://example.org/sport/{ID} | - |
| Description (sport.csv) | ex:sportname | ex:Sport | - | http://example.org/sport/{ID} | - |
| ID_Student (student_sport.csv) | ex:practises | ex:Person | ex:Sport | http://example.org/person/{ID_Student} | ID_Student = ID (student.csv) |
| ID_Sport (student_sport.csv) | ex:practises | ex:Person | ex:Sport | http://example.org/sport/{ID_Sport} | ID_Sport = ID (sport.csv) |
