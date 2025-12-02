|CSV Column|Ontology Property|Entity Class|Related Entity Class|Subject Generation|Join
|---|---|---|---|---|---|
|Student|ex:fullname |ex:Person |-|ex:[Student] (e.g. ex:Venus )|N/A (direct property of Person entity)|
|Sport|ex:sportname |ex:Sport |-|ex:[Sport] (e.g. ex:Tennis )|N/A (direct property of Sport entity)|
|-|ex:practises |ex:Person |ex:Sport |ex:[Student] → ex:practises → ex:[Sport]|Match Sport name from CSV with ex:sportname property in Sport entities|
