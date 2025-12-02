| CSV Column   | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join      |
|-------------|------------------|--------------|----------------------|--------------------|---------------------|
| ID          | ex:id            | ex:Person    | None                 | ex:Person/{ID}     | None                |
| FirstName   | ex:firstname     | ex:Person    | None                 | ex:Person/{ID}     | None                |
| LastName    | ex:lastname      | ex:Person    | None                 | ex:Person/{ID}     | None                |
| ID          | ex:sportid       | ex:Sport     | None                 | ex:Sport/{ID}      | None                |
| Description | ex:sportname     | ex:Sport     | None                 | ex:Sport/{ID}      | None                |
| ID_Student  | None             | ex:Person    | ex:Sport             | ex:Person/{ID_Student} | ID_Student = ID |
| ID_Sport    | ex:practises     | ex:Person    | ex:Sport             | ex:Sport/{ID_Sport}  | ID_Sport = ID  |

