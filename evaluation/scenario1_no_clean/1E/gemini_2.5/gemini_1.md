| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `student.csv`'s `ID` | `ex:id` | `ex:Person` | | `ex:Person/{ID}` | |
| `student.csv`'s `Name` | `ex:fullname` | `ex:Person` | | `ex:Person/{ID}` | |
| `sport.csv`'s `ID` | `ex:sportid` | `ex:Sport` | | `ex:Sport/{ID}` | |
| `sport.csv`'s `Name` | `ex:sportname` | `ex:Sport` | | `ex:Sport/{ID}` | |
| `student.csv`'s `Sport` | `ex:practises` | `ex:Person` | `ex:Sport` | `ex:Person/{ID}` | `student.csv`'s `Sport` column equals `sport.csv`'s `ID` column. |
