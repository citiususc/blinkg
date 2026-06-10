| Data Reference | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation | Join |
|:----------:|:-----------------:|:------------:|:--------------------:|:----------:|:-----:|
| student.csv ID | ex:id | ex:Person | - | http://example.org/person/{ID} | - |
| concat(student.csv FirstName, student.csv LastName) | ex:fullname | ex:Person | - | http://example.org/person/{ID} | - |
| student.csv FirstName | ex:firstname | ex:Person | - | http://example.org/person/{ID} | - |
| student.csv LastName | ex:lastname | ex:Person | - | http://example.org/person/{ID} | - |
| - | ex:practises | ex:Person | ex:Sport | http://example.org/person/{ID_Student} | student_sport.csv ID_Student = student.csv ID and student_sport.csv ID_Sport = sport.csv ID |
| sport.csv ID | ex:sportid | ex:Sport | - | http://example.org/sport/{ID} | - |
| sport.csv Description | ex:sportname | ex:Sport | - | http://example.org/sport/{ID} | - |
