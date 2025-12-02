|CSV Column|Ontology Property|Entity Class|Related Entity Class|Subject Generation|Join|
|:--------:|:---------------:|:----------:|:------------------:|:----------------:|:------------:|
|student.ID|ex:id |ex:Person ||ex:Person /{ID}||
|student.Sport|ex:practises |ex:Person |ex:Sport |ex:Person /{ID}|student.Sport = sport.ID|
|student.Name|ex:fullname |ex:Person ||ex:Person /{ID}||
|sport.ID|ex:sportid |ex:Sport ||ex:Sport /{ID}||
|sport.Name|ex:sportname |ex:Sport ||ex:Sport /{ID}||
