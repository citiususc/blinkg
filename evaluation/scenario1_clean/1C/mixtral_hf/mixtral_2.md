| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| --- | --- | --- | --- | --- | --- |
| Student | ex:firstname | ex:Person | - | ex:Person/ex:firstname | - |
| Student | ex:lastname | ex:Person | - | ex:Person/ex:lastname | - |
| Student | ex:fullname | ex:Person | - | ex:Person/ex:fullname | - |
| Sport | ex:sportname | ex:Sport | - | ex:Sport/ex:sportname | - |
| - | ex:practises | ex:Person | ex:Sport | ex:Person/ex:practises | ex:Person/ex:firstname = Student AND ex:Sport/ex:sportname = Sport |
