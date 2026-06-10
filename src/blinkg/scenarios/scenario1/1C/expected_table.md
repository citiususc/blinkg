| CSV Column | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation |Join |
|:----------:|:-----------------:|:------------:|:--------------:|:------------------:|:---:|
| Student | ex:fullname | ex:Person | | http://example.org/person/{Student} | |
| Sport | ex:sportname | ex:Sport | | http://example.org/person/{Sport} | |
|       | ex:practises | ex:Person| ex:Sport | http://example.org/person/{Student} | student=student, sport=sport |