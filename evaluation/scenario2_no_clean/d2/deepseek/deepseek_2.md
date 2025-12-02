| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `shape_id` | `gtfs:id` | `gtfs:Shape` | — | `GenerateShapeSubject(shape_id)` | — | `xsd:string` | — | `GenerateShapeSubject` `http://example.org/shapes/{shape_id}` |
| `shape_pt_lat` | `gtfs:latitude` | `gtfs:ShapePoint` | — | `GenerateShapePointSubject(...)` | Linked via `gtfs:shapePoint` to parent Shape | `geo:lat` (xsd:float) | — | `GenerateShapePointSubject` `http://example.org/shape_points/{shape_id}_{shape_pt_sequence}` |
| `shape_pt_lon` | `gtfs:longitude` | `gtfs:ShapePoint` | — | `GenerateShapePointSubject(...)` | Linked via `gtfs:shapePoint` to parent Shape | `geo:long` (xsd:float) | — | `GenerateShapePointSubject` Same as above |
| `shape_pt_sequence` | `gtfs:pointSequence` | `gtfs:ShapePoint` | — | `GenerateShapePointSubject(...)` | Linked via `gtfs:shapePoint` to parent Shape | `xsd:nonNegativeInteger` | — | `GenerateShapePointSubject` Same as above |
| `shape_dist_traveled` | `gtfs:distanceTraveled` | `gtfs:ShapePoint` | — | `GenerateShapePointSubject(...)` | Linked via `gtfs:shapePoint` to parent Shape | `gtfs:nonNegativeFloat` | — | — |
