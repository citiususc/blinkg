| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
|------------|------------------|--------------|----------------------|--------------------|---------------|
| Student    | `ex:fullname`     | `ex:Person`  | N/A                  | `ex:Person/{Student}` | N/A |
| Sport      | `ex:sportname`    | `ex:Sport`   | N/A                  | `ex:Sport/{Sport}` | N/A |
| Student    | `ex:practises`    | `ex:Person`  | `ex:Sport`           | `ex:Person/{Student}` | `ex:Person/{Student} -> ex:practises -> ex:Sport/{Sport}` |
