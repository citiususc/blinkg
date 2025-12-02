| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| --- | --- | --- | --- | --- | --- |
| ID | ex:id | ex:Person | - | "http://example.org/#Person" + ID | - |
| Sport | ex:practises | ex:Person | ex:Sport | "http://example.org/#Person" + ID | sport.csv.ID = student.csv.Sport |
| Name | ex:fullname | ex:Person | - | "http://example.org/#Person" + ID | - |
| ID | ex:sportid | ex:Sport | - | "http://example.org/#Sport" + ID | - |
| Name | ex:sportname | ex:Sport | - | "http://example.org/#Sport" + ID | - |
