| Data Reference | Ontology Property | Entity Class | Subject Generation | Datatype |
|:----------:|:-----------------:|:------------:|:------------------:|:--------:|
| ious.csv fname | ex:firstname | ex:Person | http://example.org/person/{fname}_{lname} | xsd:string |
| ious.csv lname | ex:lastname | ex:Person | http://example.org/person/{fname}_{lname} | xsd:string |
| concat(ious.csv fname, ious.csv lname) | ex:fullname | ex:Person | http://example.org/person/{fname}_{lname} | xsd:string |
| ious.csv amount | ex:owes | ex:Person | http://example.org/person/{fname}_{lname} | xsd:double |
