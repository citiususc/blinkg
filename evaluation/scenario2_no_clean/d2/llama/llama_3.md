| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `shape_id` | `gtfs:id` | `gtfs:Shape` | - | `http://vocab.gtfs.org/terms#Shape/${shape_id}` | - | `xsd:string` | - | `http://vocab.gtfs.org/terms#Shape/4__1____1__IT_1` |
| `shape_pt_lat` | `gtfs:latitude` | `gtfs:ShapePoint` | `gtfs:Shape` | `http://vocab.gtfs.org/terms#ShapePoint/${shape_id}_${shape_pt_sequence}` | `shape_id` | `geo:lat` | - | `40.4802624278576` |
| `shape_pt_lon` | `gtfs:longitude` | `gtfs:ShapePoint` | `gtfs:Shape` | `http://vocab.gtfs.org/terms#ShapePoint/${shape_id}_${shape_pt_sequence}` | `shape_id` | `geo:long` | - | `-3.66723744236574` |
| `shape_pt_sequence` | `gtfs:pointSequence` | `gtfs:ShapePoint` | `gtfs:Shape` | `http://vocab.gtfs.org/terms#ShapePoint/${shape_id}_${shape_pt_sequence}` | `shape_id` | `xsd:nonNegativeInteger` | - | `1000001` |
| `shape_dist_traveled` | `gtfs:distanceTraveled` | `gtfs:ShapePoint` | `gtfs:Shape` | `http://vocab.gtfs.org/terms#ShapePoint/${shape_id}_${shape_pt_sequence}` | `shape_id` | `gtfs:nonNegativeFloat` | - | `0.0` |
