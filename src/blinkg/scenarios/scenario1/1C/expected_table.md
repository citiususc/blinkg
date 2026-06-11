| Data Reference | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation |Join |
|:----------:|:-----------------:|:------------:|:--------------:|:------------------:|:---:|
| student_sport.csv Student | ex:fullname | ex:Person | | http://example.org/person/{Student} | |
| student_sport.csv Sport | ex:sportname | ex:Sport | | http://example.org/sport/{Sport} | |
| - | ex:practises | ex:Person | ex:Sport | http://example.org/person/{Student} | student_sport.csv Student = student_sport.csv Student and student_sport.csv Sport = student_sport.csv Sport |
