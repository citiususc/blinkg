| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| --- | --- | --- | --- | --- | --- |
| ID | ex:id | ex:Person | - | Use ID to generate subject URI (e.g., `<http://example.org/#Person_ID>`) | - |
| FirstName | ex:firstname | ex:Person | - | Use ID to generate subject URI (e.g., `<http://example.org/#Person_ID>`) | - |
| LastName | ex:lastname | ex:Person | - | Use ID to generate subject URI (e.g., `<http://example.org/#Person_ID>`) | - |
| ID | ex:sportid | ex:Sport | - | Use ID to generate subject URI (e.g., `<http://example.org/#Sport_ID>`) | - |
| Description | ex:sportname | ex:Sport | - | Use ID to generate subject URI (e.g., `<http://example.org/#Sport_ID>`) | - |
| ID_Student | ex:id | ex:Person | - | Use ID_Student to generate subject URI (e.g., `<http://example.org/#Person_ID_Student>`) | - |
| ID_Sport | ex:sportid | ex:Sport | - | Use ID to generate subject URI (e.g., `<http://example.org/#Sport_ID_Sport>`) | - |
| - | ex:practises | ex:Person | ex:Sport | Use ID_Student to generate subject URI (e.g., `<http://example.org/#Person_ID_Student>`) and ID_Sport to generate object URI (e.g., `<http://example.org/#Sport_ID_Sport>`) | Join student.csv and sport.csv using student_sport.csv on ID_Student and ID_Sport |
