| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| --- | --- | --- | --- | --- | --- |
| ID | ex:id | ex:Person | - | ex:Person/ex:id | - |
| FirstName | ex:firstname | ex:Person | - | ex:Person/ex:firstname | - |
| LastName | ex:lastname | ex:Person | - | ex:Person/ex:lastname | - |
| ID | ex:sportid | ex:Sport | - | ex:Sport/ex:sportid | - |
| Description | ex:sportname | ex:Sport | - | ex:Sport/ex:sportname | - |
| ID_Student | ex:id | ex:Person | - | ex:Person/ex:id | - |
| ID_Sport | ex:sportid | ex:Sport | - | ex:Sport/ex:sportid | - |
| ID_Student, ID_Sport | ex:practises | ex:Person | ex:Sport | ex:Person/ex:id | ex:Person/ex:practises = ex:Sport/ex:sportid |
