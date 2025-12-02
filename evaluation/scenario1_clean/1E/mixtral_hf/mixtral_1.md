| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| --- | --- | --- | --- | --- | --- |
| ID | ex:id | ex:Person |  | CONCAT("http://example.org/#Person_", ID) |  |
| Sport | ex:sportid (related to ex:practises) | ex:Person | ex:Sport | CONCAT("http://example.org/#Person_", ID) | sport.csv.ID = student.csv.Sport |
| Name | ex:fullname | ex:Person |  | CONCAT("http://example.org/#Person_", ID) |  |
| ID | ex:sportid | ex:Sport |  | CONCAT("http://example.org/#Sport_", ID) |  |
| Name | ex:sportname | ex:Sport |  | CONCAT("http://example.org/#Sport_", ID) |  |
