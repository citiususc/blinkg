| Data Reference | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation | Join | Datatype | Language Annotations |
|:----------:|:-----------------:|:------------:|:------------------:|:--------:|:---:|:--:|:---:|
| persons.csv fname | ex:firstname | ex:Person | - | http://example.org/person/{fname}_{lname} | - | xsd:string | - |
| persons.csv lname | ex:lastname | ex:Person | - | http://example.org/person/{fname}_{lname} | - | xsd:string | - |
| concat(persons.csv fname, persons.csv lname) | ex:fullname | ex:Person | - | http://example.org/person/{fname}_{lname} | - | xsd:string | - |
| concat(persons.csv fname, persons.csv lname) | ex:lives | ex:Person | ex:City | http://example.org/person/{fname}_{lname} | persons.csv fname = lives.csv fname and persons.csv lname = lives.csv lname | - | - |
| persons.csv amount | ex:owes | ex:Person | - | http://example.org/person/{fname}_{lname} | - | xsd:double | - |
| lives.csv city | ex:cityname | ex:City | - | http://example.org/city/{city} | - | xsd:langString | @en |
