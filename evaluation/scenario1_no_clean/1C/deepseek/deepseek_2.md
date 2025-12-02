|CSV Column|Ontology Property|Entity Class|Related Entity Class|Subject Generation|Join|
|---|---|---|---|---|---|
|Student|ex:fullname |ex:Person |-|URI generated from Student (e.g., ex:Venus)|-|
|Sport|ex:sportname |ex:Sport |-|URI generated from Sport (e.g., ex:Tennis)|-|
|Student,Sport|ex:practises |ex:Person |ex:Sport |Subject of ex:Person (from Student)|Match Sport value to ex:sportname of an ex:Sport entity (e.g., ex:Tennis)|
