| CSV Column | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation |Join |
|:----------:|:-----------------:|:------------:|:--------------------:|:----------:|:-----:|
| student.csv ID | ex:id | ex:Person || http://example.org/person/{ID} | |
| student.csv concat(FirstName,LastName) | ex:fullname | ex:Person || http://example.org/person/{ID} | |
| student.csv FirstName | ex:firstname | ex:Person || http://example.org/person/{ID} | |
| student.csv LastName | ex:lastname | ex:Person || http://example.org/person/{ID} | |
| student_sport.csv Sport | ex:practises | ex:Person | ex:Sport | http://example.org/person/{ID} | student_sport.ID_Student==student.ID and student_sport.ID_Sport==sport.ID |
| sport.csv ID | ex:sportid | ex:Sport || http://example.org/sport/{ID} | |
| sport.csv Description | ex:sportname | ex:Sport || http://example.org/sport/{ID} | |