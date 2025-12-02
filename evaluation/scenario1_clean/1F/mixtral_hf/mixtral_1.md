| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| --- | --- | --- | --- | --- | --- |
| ID | ex:id | ex:Person | - | ex:Person/ex:id | - |
| FirstName | ex:firstname | ex:Person | - | ex:Person/ex:firstname | - |
| LastName | ex:lastname | ex:Person | - | ex:Person/ex:lastname | - |
| ID | ex:sportid | ex:Sport | - | ex:Sport/ex:sportid | - |
| Description | ex:sportname | ex:Sport | - | ex:Sport/ex:sportname | - |
| ID_Student | ex:id | ex:Person | - | ex:Person/ex:id | - |
| ID_Sport | ex:sportid | ex:Sport | - | ex:Sport/ex:sportid | - |
| - | ex:practises | ex:Person | ex:Sport | ex:Person/ex:id | Join on ID_Student (ex:Person/ex:id) and ID_Sport (ex:Sport/ex:sportid) |
| - | ex:fullname | ex:Person | - | ex:Person/ex:fullname | Derived from ex:Person/ex:firstname and ex:Person/ex:lastname |
