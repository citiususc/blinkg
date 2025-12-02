| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shape_id | gtfs:id | gtfs:Shape | - | `http://example.org/shapes/{shape_id}` | - | xsd:string | - | GenerateShapeURI `http://example.org/shapes/4__1____1__IT_1` |
| shape_pt_lat | gtfs:latitude | gtfs:ShapePoint | - | `http://example.org/shape_points/{shape_id}_{shape_pt_sequence}` | Linked via `gtfs:shapePoint` to Shape | geo:lat | - | CastToLatitude `40.4802624278576`^^geo:lat |
| shape_pt_lon | gtfs:longitude | gtfs:ShapePoint | - | Same as above | Same as above | geo:long | - | CastToLongitude `-3.66723744236574`^^geo:long |
| shape_pt_sequence | gtfs:pointSequence | gtfs:ShapePoint | - | Same as above | Same as above | xsd:nonNegativeInteger | - | CastToNonNegativeInteger `1000001`^^xsd:nonNegativeInteger |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:ShapePoint | - | Same as above | Same as above | gtfs:nonNegativeFloat | - | CastToNonNegativeFloat `0.0`^^gtfs:nonNegativeFloat |
