| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Language Annotations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| fname | `ex:firstname` | `ex:Person` | N/A | `ex:person/{fname}-{lname}` | N/A | `xsd:string` | N/A |
| lname | `ex:lastname` | `ex:Person` | N/A | `ex:person/{fname}-{lname}` | N/A | `xsd:string` | N/A |
| amount | `ex:owes` | `ex:Person` | N/A | `ex:person/{fname}-{lname}` | N/A | `xsd:double` | N/A |
| city | `ex:cityname` | `ex:City` | N/A | `ex:city/{city}` | N/A | `xsd:langString` | en |
| N/A | `ex:lives` | `ex:Person` | `ex:City` | `ex:person/{fname}-{lname}` | `persons.fname = lives.fname`<br>`persons.lname = lives.lname` | N/A | N/A |
| (fname, lname) | `ex:fullname` | `ex:Person` | N/A | `ex:person/{fname}-{lname}` | N/A | `xsd:string` | N/A |
