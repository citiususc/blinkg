|CSV Column|Ontology Property|Entity Class|Related Entity Class|Subject Generation|Join|
|---|---|---|---|---|---|
|Student|ex:fullname |ex:Person |-|ex:Person URI from name (e.g., ex:Venus )|N/A (direct property of Person entity)|
|Sport|ex:sportname |ex:Sport |-|ex:Sport URI from name (e.g., ex:Tennis )|N/A (direct property of Sport entity)|
|N/A|ex:practises |ex:Person |ex:Sport |ex:Person URI (subject)|Join when student_sport.Sport = Sport.sportname to link Person → Sport|
