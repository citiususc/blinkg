| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `shape_id` | `gtfs:id` | `gtfs:Shape` | N/A | `"gtfs:shape/" + {shape_id}` | N/A | `xsd:string` | N/A | N/A |
| `shape_id`, `shape_pt_sequence` | `gtfs:shapePoint` | `gtfs:Shape` | `gtfs:ShapePoint` | Subject: `"gtfs:shape/" + {shape_id}`<br>Object: `"gtfs:shapepoint/" + {shape_id} + "-" + {shape_pt_sequence}` | A `gtfs:Shape` is linked to each of its `gtfs:ShapePoint`s. This relationship is created for every row in the CSV. |  | N/A | N/A |
| `shape_pt_lat` | `gtfs:latitude` | `gtfs:ShapePoint` | N/A | `"gtfs:shapepoint/" + {shape_id} + "-" + {shape_pt_sequence}` | N/A | `geo:lat` | N/A | N/A |
| `shape_pt_lon` | `gtfs:longitude` | `gtfs:ShapePoint` | N/A | `"gtfs:shapepoint/" + {shape_id} + "-" + {shape_pt_sequence}` | N/A | `geo:long` | N/A | N/A |
| `shape_pt_sequence` | `gtfs:pointSequence` | `gtfs:ShapePoint` | N/A | `"gtfs:shapepoint/" + {shape_id} + "-" + {shape_pt_sequence}` | N/A | `xsd:nonNegativeInteger` | N/A | N/A |
| `shape_dist_traveled` | `gtfs:distanceTraveled` | `gtfs:ShapePoint` | N/A | `"gtfs:shapepoint/" + {shape_id} + "-" + {shape_pt_sequence}` | N/A | `gtfs:nonNegativeFloat` | N/A | N/A |
