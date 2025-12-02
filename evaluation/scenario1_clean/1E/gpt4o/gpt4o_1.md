|CSV Column|Ontology Property|Entity Class|Related Entity Class|Subject Generation|Join|
|:--------:|:---------------:|:----------:|:------------------:|:----------------:|:------------:|
|ID|ex:id|ex:Person||ex:Person/{ID}|student.csv.ID = sport.csv.ID (not applicable)|
|Sport|ex:practises|ex:Person|ex:Sport|ex:Person/{ID} -> ex:Sport/{Sport}|student.csv.Sport = sport.csv.ID|
|Name|ex:fullname|ex:Person||ex:Person/{ID}| |
|ID|ex:sportid|ex:Sport||ex:Sport/{ID}| |
|Name|ex:sportname|ex:Sport||ex:Sport/{ID}| |
