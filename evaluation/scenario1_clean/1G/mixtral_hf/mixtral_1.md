| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Language Annotations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fname | ex:firstname | ex:Person | - | Combine fname and lname to generate the subject | - | xsd:string | - |
| lname | ex:lastname | ex:Person | - | Combine fname and lname to generate the subject | - | xsd:string | - |
| amount | ex:owes | ex:Person | - | Combine fname and lname to generate the subject | - | xsd:double | - |
| fname | ex:firstname | ex:Person | ex:City | Combine fname and lname to generate the subject | Combine fname and lname to find the matching city | xsd:string | - |
| lname | ex:lastname | ex:Person | ex:City | Combine fname and lname to generate the subject | Combine fname and lname to find the matching city | xsd:string | - |
| city | ex:cityname | ex:City | - | Use city as the subject | - | xsd:langString | - |
