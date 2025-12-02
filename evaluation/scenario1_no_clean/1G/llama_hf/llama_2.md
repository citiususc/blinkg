| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Language Annotations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fname | ex:firstname | ex:Person | - | ex:Person_\<fname>_\<lname> | fname and lname | xsd:string | - |
| lname | ex:lastname | ex:Person | - | ex:Person_\<fname>_\<lname> | fname and lname | xsd:string | - |
| amount | ex:owes | ex:Person | - | ex:Person_\<fname>_\<lname> | fname and lname | xsd:double | - |
| city | ex:cityname | ex:City | ex:Person | ex:City_\<city> | city | xsd:langString | @en |
