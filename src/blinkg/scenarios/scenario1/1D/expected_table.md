| CSV Column | Ontology Property | Entity Class | Subject Generation | Datatype |
|:----------:|:-----------------:|:------------:|:------------------:|:--------:|
| fname | ex:firstname | ex:Person | http://example.org/person/{fname}_{lname} | xsd:string |
| lname | ex:lastname | ex:Person | http://example.org/person/{fname}_{lname} | xsd:string |
| concat(fname,lname) | ex:fullname | ex:Person | http://example.org/person/{fname}_{lname} | xsd:string |
| amount | ex:owes | ex:Person | http://example.org/person/{fname}_{lname} | xsd:double |
