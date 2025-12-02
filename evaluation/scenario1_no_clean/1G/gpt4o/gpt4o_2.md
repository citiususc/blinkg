| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation     | Join       | Datatype      | Language Annotations |
|------------|------------------|--------------|----------------------|------------------------|----------------------|--------------|----------------------|
| fname      | ex:firstname     | ex:Person    | None                 | Concat(fname, lname)   | None                 | xsd:string   | None                 |
| lname      | ex:lastname      | ex:Person    | None                 | Concat(fname, lname)   | None                 | xsd:string   | None                 |
| amount     | ex:owes          | ex:Person    | None                 | Concat(fname, lname)   | None                 | xsd:double   | None                 |
| fname      | ex:firstname     | ex:Person    | None                 | Concat(fname, lname)   | Match on fname, lname | xsd:string   | None                 |
| lname      | ex:lastname      | ex:Person    | None                 | Concat(fname, lname)   | Match on fname, lname | xsd:string   | None                 |
| city       | ex:cityname      | ex:City      | None                 | city                   | None                 | xsd:langString | None                 |
| None       | ex:lives         | ex:Person    | ex:City              | Concat(fname, lname)   | Match on fname, lname | None         | None                 |
