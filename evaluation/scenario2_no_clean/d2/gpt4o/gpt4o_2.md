| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shape_id | gtfs:id | gtfs:Shape |  | `ex:shape/{shape_id}` |  | xsd:string |  | `generateShapeURI` `ex:shape/4__1____1__IT_1` |
| shape_pt_lat | gtfs:latitude | gtfs:ShapePoint |  | `ex:shapePoint/{shape_id}_{seq}` | shape_id + shape_pt_sequence | geo:lat |  |  Float values |
| shape_pt_lon | gtfs:longitude | gtfs:ShapePoint |  | `ex:shapePoint/{shape_id}_{seq}` | shape_id + shape_pt_sequence | geo:long |  |  Float values |
| shape_pt_sequence | gtfs:pointSequence | gtfs:ShapePoint |  | `ex:shapePoint/{shape_id}_{seq}` | shape_id + shape_pt_sequence | xsd:nonNegativeInteger |  |  Integer values |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:ShapePoint |  | `ex:shapePoint/{shape_id}_{seq}` | shape_id + shape_pt_sequence | gtfs:nonNegativeFloat |  |  Float values ≥ 0 |
| shape_id | gtfs:shapePoint (relates) | gtfs:Shape | gtfs:ShapePoint | `ex:shape/{shape_id}` | shape_id |  |  | `relateShapeToPoint` `ex:shape/4__1____1__IT_1 gtfs:shapePoint ex:shapePoint/4__1____1__IT_1_1000001` |
