| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shape_id | gtfs:id | gtfs:Shape | - | `http://vocab.gtfs.org/terms#Shape/${shape_id}` | - | xsd:string | - | `http://vocab.gtfs.org/terms#Shape/${shape_id}` |
| shape_pt_lat | gtfs:latitude | gtfs:ShapePoint | gtfs:Shape | `http://vocab.gtfs.org/terms#ShapePoint/${shape_id}-${shape_pt_sequence}` | shape_id | geo:lat | - | `${shape_pt_lat}` |
| shape_pt_lon | gtfs:longitude | gtfs:ShapePoint | gtfs:Shape | `http://vocab.gtfs.org/terms#ShapePoint/${shape_id}-${shape_pt_sequence}` | shape_id | geo:long | - | `${shape_pt_lon}` |
| shape_pt_sequence | gtfs:pointSequence | gtfs:ShapePoint | gtfs:Shape | `http://vocab.gtfs.org/terms#ShapePoint/${shape_id}-${shape_pt_sequence}` | shape_id | xsd:nonNegativeInteger | - | `${shape_pt_sequence}` |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:ShapePoint | gtfs:Shape | `http://vocab.gtfs.org/terms#ShapePoint/${shape_id}-${shape_pt_sequence}` | shape_id | gtfs:nonNegativeFloat | - | `${shape_dist_traveled}` |
