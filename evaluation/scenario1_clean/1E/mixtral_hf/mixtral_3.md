| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| --- | --- | --- | --- | --- | --- |
| ID | ex:id | ex:Person | N/A | Use the value directly | N/A |
| Sport | ex:practises | ex:Person | ex:Sport | Use the value to join with sport.csv's ID column to get the corresponding sport name, then map to ex:practises | sport.csv.ID = student.csv.Sport |
| Name | ex:fullname | ex:Person | N/A | Use the value directly | N/A |
| ID | ex:sportid | ex:Sport | N/A | Use the value directly | N/A |
| Name | ex:sportname | ex:Sport | N/A | Use the value directly | N/A |
