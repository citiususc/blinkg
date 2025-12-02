| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
|------------|------------------|-------------|----------------------|--------------------|---------------|
| Student    | ex:fullname      | ex:Person   | None                 | ex:Person/{Student} | None          |
| Sport      | ex:sportname     | ex:Sport    | None                 | ex:Sport/{Sport}    | None          |
| Student    | ex:practises     | ex:Person   | ex:Sport             | ex:Person/{Student} | ex:Sport/{Sport} |
