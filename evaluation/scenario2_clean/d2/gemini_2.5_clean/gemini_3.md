| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `shape_id` | `gtfs:id` | `gtfs:Shape` | | `gtfs:Shape/{shape_id}` | | `xsd:string` |
| | `gtfs:shapePoint` | `gtfs:Shape` | `gtfs:ShapePoint` | `gtfs:Shape/{shape_id}` | `shape_id` value from `gtfs:Shape` must match the `shape_id` part of the `gtfs:ShapePoint` subject | |
| `shape_pt_lat` | `gtfs:latitude` | `gtfs:ShapePoint` | | `gtfs:ShapePoint/{shape_id}-{shape_pt_sequence}` | | `geo:lat` |
| `shape_pt_lon` | `gtfs:longitude` | `gtfs:ShapePoint` | | `gtfs:ShapePoint/{shape_id}-{shape_pt_sequence}` | | `geo:long` |
| `shape_pt_sequence` | `gtfs:pointSequence`| `gtfs:ShapePoint` | | `gtfs:ShapePoint/{shape_id}-{shape_pt_sequence}` | | `xsd:nonNegativeInteger` |
| `shape_dist_traveled`| `gtfs:distanceTraveled`| `gtfs:ShapePoint` | | `gtfs:ShapePoint/{shape_id}-{shape_pt_sequence}` | | `gtfs:nonNegativeFloat`|
