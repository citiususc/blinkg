| CSV Column                     | Ontology Property | Entity Class | Related Entity Class | Subject Generation       | Join                              |
|--------------------------------|-------------------|--------------|----------------------|--------------------------|---------------------------------------------|
| **student.csv/ID**             | `ex:id`           | `ex:Person`  | -                    | `ex:Student_{ID}`        | -                                           |
| **student.csv/FirstName**      | `ex:firstname`    | `ex:Person`  | -                    | `ex:Student_{ID}`        | -                                           |
| **student.csv/LastName**       | `ex:lastname`     | `ex:Person`  | -                    | `ex:Student_{ID}`        | -                                           |
| **sport.csv/ID**               | `ex:sportid`      | `ex:Sport`   | -                    | `ex:Sport_{ID}`          | -                                           |
| **sport.csv/Description**      | `ex:sportname`    | `ex:Sport`   | -                    | `ex:Sport_{ID}`          | -                                           |
| **student_sport.csv/ID_Student** | `ex:practises`  | `ex:Person`  | `ex:Sport`           | `ex:Student_{ID_Student}` | `student_sport.ID_Student = student.ID`     |
| **student_sport.csv/ID_Sport**   | `ex:practises`  | `ex:Sport`   | `ex:Person`          | `ex:Sport_{ID_Sport}`     | `student_sport.ID_Sport = sport.ID`         |
