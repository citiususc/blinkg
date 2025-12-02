| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Language Annotations |
|:----------:|:-----------------:|:------------:|:------------------:|:--------:|:---:|:--:|:---:|
| persons.csv fname | ex:firstname | ex:Person || http://example.org/person/{fname}_{lname} | | xsd:string ||
| persons.csv lname | ex:lastname | ex:Person | |http://example.org/person/{fname}_{lname} | | xsd:string ||
| persons.csv concat(fname,lname) | ex:fullname | ex:Person | |http://example.org/person/{fname}_{lname} | | xsd:string ||
| persons.csv concat(fname,lname) | ex:lives | ex:Person | ex:City | http://example.org/person/{fname}_{lname} | | Object Property |
| persons.csv amount | ex:owes | ex:Person | |http://example.org/person/{fname}_{lname} | |xsd:double ||
| lives.csv city | ex:cityname | ex:City || http://example.org/city/{city} | persons.fname==lives.fname and persons.lname==lives.lname | xsd:langString | @en |