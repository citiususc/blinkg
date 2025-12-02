| CSV Column    | Ontology Property | Entity Class | Related Entity Class | Subject Generation   | Join                    |
|--------------|------------------|-------------|----------------------|----------------------|----------------------------------|
| ID           | ex:id            | ex:Person  |                      | ex:Person/{ID}       |                                  |
| FirstName    | ex:firstname     | ex:Person  |                      | ex:Person/{ID}       |                                  |
| LastName     | ex:lastname      | ex:Person  |                      | ex:Person/{ID}       |                                  |
| ID           | ex:sportid       | ex:Sport   |                      | ex:Sport/{ID}        |                                  |
| Description  | ex:sportname     | ex:Sport   |                      | ex:Sport/{ID}        |                                  |
| ID_Student   | ex:practises     | ex:Person  | ex:Sport             | ex:Person/{ID_Student} | ID_Student -> ID en student.csv  |
| ID_Sport     | ex:practises     | ex:Sport   | ex:Person            | ex:Sport/{ID_Sport}  | ID_Sport -> ID en sport.csv      |
