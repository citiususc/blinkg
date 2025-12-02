| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `shape_id` | `gtfs:id` | `gtfs:Shape` | N/A | `URI(<http://vocab.gtfs.org/Shape/{SHAPE_ID}>)` | `SHAPE_ID = SUBJECT.shape_id` | `xsd:string` | `URI_VECTOR_SHAPE` | `<http://vocab.gtfs.org/Shape/{SHAPE_ID}>` |
| `shape_pt_lat` | `gtfs:latitude` | `gtfs:ShapePoint` | N/A | `float(SHAPE_PT_LAT)` | `None` | `geo:lat` | `LATITUDE` | `{SHAPE_PT_LAT}` (e.g., `40.4802624278576`) |
| `shape_pt_lon` | `gtfs:longitude` | `gtfs:ShapePoint` | N/A | `float(SHAPE_PT_LON)` | `None` | `geo:long` | `LONGITUDE` | `{SHAPE_PT_LON}` (e.g., `-3.66723744236574`) |
| `shape_pt_sequence` | `gtfs:pointSequence` | `gtfs:ShapePoint` | N/A | `int(SHAPE_PT_SEQUENCE)` | `None` | `xsd:nonNegativeInteger` | `POINT_SEQUENCE` | `{SHAPE_PT_SEQUENCE}` (e.g., `1000001`) |
| `shape_dist_traveled` | `gtfs:distanceTraveled` | `gtfs:ShapePoint` | N/A | `float(SHAPE_DIST_TRAVELED)` | `None` | `gtfs:nonNegativeFloat` | `DISTANCE_TRAVELED` | `{SHAPE_DIST_TRAVELED}` (e.g., `0.0`) |
