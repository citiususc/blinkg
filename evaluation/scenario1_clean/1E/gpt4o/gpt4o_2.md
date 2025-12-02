|CSV Column|Ontology Property|Entity Class|Related Entity Class|Subject Generation|Join|
|:--------:|:---------------:|:----------:|:------------------:|:----------------:|:------------:|
|ID (student.csv)|ex:id|ex:Person||ex:Person/{ID}||
|Sport|ex:practises|ex:Person|ex:Sport|ex:Person/{ID}|Sport = sport.csv.ID|
|Name|ex:fullname|ex:Person||ex:Person/{ID}||
|ID (sport.csv)|ex:sportid|ex:Sport||ex:Sport/{ID}||
|Name (sport.csv)|ex:sportname|ex:Sport||ex:Sport/{ID}||
