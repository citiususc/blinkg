| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shape_id | gtfs:id | gtfs:Shape |  | ex:shape/{shape_id} |  | xsd:string |  |  |
|  | gtfs:shapePoint | gtfs:Shape | gtfs:ShapePoint | ex:shape/{shape_id} | The subject is generated for each unique `shape_id`. |  |  |  |
| shape_pt_lat | gtfs:latitude | gtfs:ShapePoint |  | ex:shapepoint/{shape_id}-{shape_pt_sequence} | The subject is generated for each row in the CSV. | geo:lat |  |  |
| shape_pt_lon | gtfs:longitude | gtfs:ShapePoint |  | ex:shapepoint/{shape_id}-{shape_pt_sequence} | The subject is generated for each row in the CSV. | geo:long |  |  |
| shape_pt_sequence | gtfs:pointSequence | gtfs:ShapePoint |  | ex:shapepoint/{shape_id}-{shape_pt_sequence} | The subject is generated for each row in the CSV. | xsd:nonNegativeInteger |  |  |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:ShapePoint |  | ex:shapepoint/{shape_id}-{shape_pt_sequence} | The subject is generated for each row in the CSV. | gtfs:nonNegativeFloat |  |  |
