| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Language Annotations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fname | ex:firstname | ex:Person |  | ex:Person_\<fname>_\<lname> | fname and lname | xsd:string | @en |
| lname | ex:lastname | ex:Person |  | ex:Person_\<fname>_\<lname> | fname and lname | xsd:string | @en |
| amount | ex:owes | ex:Person |  | ex:Person_\<fname>_\<lname> | fname and lname | xsd:double | @en |
| city | ex:cityname | ex:City | ex:Person | ex:City_\<city> | city | xsd:langString | @en |
| fname (lives) | ex:firstname | ex:Person | ex:City | ex:Person_\<fname>_\<lname> | fname and lname | xsd:string | @en |
| lname (lives) | ex:lastname | ex:Person | ex:City | ex:Person_\<fname>_\<lname> | fname and lname | xsd:string | @en |
