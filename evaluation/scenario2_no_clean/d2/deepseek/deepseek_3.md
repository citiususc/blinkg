| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shape_id | gtfs:id | gtfs:Shape | - | `http://example.org/shape/{shape_id}` | N/A (root entity) | xsd:string | @en, @es | - |
| shape_pt_lat | gtfs:latitude | gtfs:ShapePoint | - | `http://example.org/shapepoint/{shape_id}_{shape_pt_sequence}` | Linked via gtfs:shapePoint to Shape | geo:lat | - | ValidateLat 40.4802624278576 → "40.480262"^^geo:lat |
| shape_pt_lon | gtfs:longitude | gtfs:ShapePoint | - | Same as above | Same as above | geo:long | - | ValidateLon "-3.667237"^^geo:long |
| shape_pt_sequence | gtfs:pointSequence | gtfs:ShapePoint | - | Same as above | Same as above | xsd:nonNegativeInteger | - | SequenceCast 1000001 → "1000001"^^xsd:nonNegativeInteger |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:ShapePoint | - | Same as above | Same as above | gtfs:nonNegativeFloat | - | FloatCast 0.0 → "0.0"^^gtfs:nonNegativeFloat |
