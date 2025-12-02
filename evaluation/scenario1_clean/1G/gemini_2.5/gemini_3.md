| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Language Annotations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| fname | ex:firstname | ex:Person | | `ex:{fname}-{lname}` | | xsd:string | |
| lname | ex:lastname | ex:Person | | `ex:{fname}-{lname}` | | xsd:string | |
| fname, lname | ex:fullname | ex:Person | | `ex:{fname}-{lname}` | | xsd:string | |
| amount | ex:owes | ex:Person | | `ex:{fname}-{lname}` | | xsd:double | |
| city | ex:lives | ex:Person | ex:City | `ex:{fname}-{lname}` | `persons.fname = lives.fname AND persons.lname = lives.lname` | | |
| city | ex:cityname | ex:City | | `ex:{city}` | | xsd:langString | en |
