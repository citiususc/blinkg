| CSV Column            | Ontology Property | Entity Class | Related Entity Class | Subject Generation        | Join                                                                 |
|-----------------------|-------------------|--------------|----------------------|---------------------------|--------------------------------------------------------------------------------|
| student.ID            | ex:id             | ex:Person    | -                    | ex:Person/{ID}            | -                                                                              |
| student.FirstName     | ex:firstname      | ex:Person    | -                    | ex:Person/{ID}            | -                                                                              |
| student.LastName      | ex:lastname       | ex:Person    | -                    | ex:Person/{ID}            | -                                                                              |
| (Generated) FullName  | ex:fullname       | ex:Person    | -                    | ex:Person/{ID}            | Concatenate FirstName + " " + LastName                                         |
| sport.ID              | ex:sportid        | ex:Sport     | -                    | ex:Sport/{ID}             | -                                                                              |
| sport.Description     | ex:sportname      | ex:Sport     | -                    | ex:Sport/{ID}             | -                                                                              |
| student_sport.ID_Student | ex:practises    | ex:Person    | ex:Sport             | ex:Person/{ID_Student}    | Match student_sport.ID_Student = student.ID AND student_sport.ID_Sport = sport.ID |
| student_sport.ID_Sport  | ex:practises    | ex:Sport     | ex:Person            | ex:Sport/{ID_Sport}       | Match student_sport.ID_Sport = sport.ID AND student_sport.ID_Student = student.ID |
