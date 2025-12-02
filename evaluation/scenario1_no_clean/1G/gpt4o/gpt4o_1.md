| CSV Column       | Ontology Property | Entity Class | Related Entity Class | Subject Generation      | Join  | Datatype       | Language Annotations |
|-----------------|------------------|-------------|----------------------|-------------------------|----------------|---------------|---------------------|
| fname          | ex:firstname      | ex:Person   | None                 | ex:Person_{fname}_{lname} | fname, lname  | xsd:string    | None                |
| lname          | ex:lastname       | ex:Person   | None                 | ex:Person_{fname}_{lname} | fname, lname  | xsd:string    | None                |
| amount         | ex:owes           | ex:Person   | None                 | ex:Person_{fname}_{lname} | fname, lname  | xsd:double    | None                |
| city           | ex:cityname       | ex:City     | None                 | ex:City_{city}           | city          | xsd:langString | None                |
| (fname, lname) | ex:lives          | ex:Person   | ex:City              | ex:Person_{fname}_{lname} | fname, lname  | ObjectProperty | None                |
