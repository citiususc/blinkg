| CSV Column | Ontology Property      | Entity Class | Related Entity Class | Subject Generation       | Join                     | Datatype          | Language Annotations |
|------------|------------------------|--------------|----------------------|--------------------------|------------------------------------|-------------------|----------------------|
| fname      | ex:firstname           | ex:Person    | -                    | ex:{fname}_{lname}       | -                                  | xsd:string       | -                    |
| lname      | ex:lastname            | ex:Person    | -                    | ex:{fname}_{lname}       | -                                  | xsd:string       | -                    |
| amount     | ex:owes                | ex:Person    | -                    | ex:{fname}_{lname}       | -                                  | xsd:double       | -                    |
| city       | ex:lives               | ex:Person    | ex:City              | ex:{fname}_{lname}       | JOIN persons.csv ON fname+lname   | -                | -                    |
| city       | ex:cityname            | ex:City      | -                    | ex:City_{city}           | -                                  | xsd:langString   | @en                  |
