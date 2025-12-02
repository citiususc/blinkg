| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation       | Join                                   | Datatype        | Language Annotations |
|------------|-------------------|--------------|----------------------|--------------------------|-------------------------------------------------|-----------------|----------------------|
| **persons.csv**                                                                                                                             |
| `fname`    | `ex:firstname`    | `ex:Person`  | —                    | `ex:Person_{fname}_{lname}` | Unique combination of `fname` + `lname`         | `xsd:string`    | —                    |
| `lname`    | `ex:lastname`     | `ex:Person`  | —                    | `ex:Person_{fname}_{lname}` | Unique combination of `fname` + `lname`         | `xsd:string`    | —                    |
| `amount`   | `ex:owes`         | `ex:Person`  | —                    | `ex:Person_{fname}_{lname}` | Unique combination of `fname` + `lname`         | `xsd:double`    | —                    |
| **lives.csv**                                                                                                                              |
| `fname`    | `ex:firstname`    | `ex:Person`  | —                    | `ex:Person_{fname}_{lname}` | Join with `persons.csv` via `fname` + `lname`   | `xsd:string`    | —                    |
| `lname`    | `ex:lastname`     | `ex:Person`  | —                    | `ex:Person_{fname}_{lname}` | Join with `persons.csv` via `fname` + `lname`   | `xsd:string`    | —                    |
| `city`     | `ex:lives`        | `ex:Person`  | `ex:City`            | `ex:Person_{fname}_{lname}` | City entity generated from `city` column        | | —                    |
| `city`     | `ex:cityname`     | `ex:City`    | —                    | `ex:City_{city}`           | —                                               | `xsd:langString`| `@en`                |
