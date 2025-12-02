| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| --- | --- | --- | --- | --- | --- |
| student.csv - ID | ex:id | ex:Person | - | http://example.org/person/{ID} | - |
| student.csv - Name | ex:fullname | ex:Person | - | http://example.org/person/{ID} | - |
| student.csv - Sport | ex:practises | ex:Person | ex:Sport | http://example.org/person/{ID} | sport.csv - ID |
| sport.csv - ID | ex:sportid | ex:Sport | - | http://example.org/sport/{ID} | - |
| sport.csv - Name | ex:sportname | ex:Sport | - | http://example.org/sport/{ID} | - |
