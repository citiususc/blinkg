| Data Reference           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype |
| --- | --- | --- | --- | --- | --- | --- |
| shapes.csv shape_id | gtfs:id | gtfs:Shape | - | http://example.org/shape/{shape_id} | - | xsd:string |
| shapes.csv shape_pt_lat | gtfs:latitude | gtfs:ShapePoint | - | http://example.org/shape/{shape_id}_{shape_pt_sequence} | - | geo:lat |
| shapes.csv shape_pt_lon | gtfs:longitude | gtfs:ShapePoint | - | http://example.org/shape/{shape_id}_{shape_pt_sequence} | - | geo:lon |
| shapes.csv shape_pt_sequence | gtfs:pointSequence | gtfs:ShapePoint | - | http://example.org/shape/{shape_id}_{shape_pt_sequence} | - | xsd:nonNegativeInteger |
| shapes.csv shape_dist_traveled | gtfs:distanceTraveled | gtfs:Shape | - | http://example.org/shape/{shape_id} | - | gtfs:nonNegativeFloat |
| shapes.csv shape_id | gtfs:shapePoint | gtfs:Shape | gtfs:ShapePoint | http://example.org/shape/{shape_id} | shapes.csv shape_id = shapes.csv shape_id | - |
