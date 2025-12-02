| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| --- | --- | --- | --- | --- | --- |
| Student | ex:fullname | ex:Person | - | `http://example.org/person/{Student}` | - |
| Sport | ex:sportname | ex:Sport | - | `http://example.org/sport/{Sport}` | - |
| Student, Sport | ex:practises | ex:Person | ex:Sport | `http://example.org/person/{Student}`, `http://example.org/sport/{Sport}` | Student and Sport appear together in the same row |
