| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shape_id | gtfs:id | gtfs:Shape |  | `ex:shape/{shape_id}` |  | xsd:string | en, es | generateShapeURI `ex:shape/4__1____1__IT_1` |
| shape_pt_lat | gtfs:latitude | gtfs:ShapePoint |  | `ex:shapePoint/{shape_id}/{sequence}` |  | geo:lat | en | — raw float value |
| shape_pt_lon | gtfs:longitude | gtfs:ShapePoint |  | `ex:shapePoint/{shape_id}/{sequence}` |  | geo:long | en | — raw float value |
| shape_pt_sequence | gtfs:pointSequence | gtfs:ShapePoint |  | `ex:shapePoint/{shape_id}/{sequence}` |  | xsd:nonNegativeInteger | en, es | — raw integer value |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:ShapePoint |  | `ex:shapePoint/{shape_id}/{sequence}` |  | gtfs:nonNegativeFloat | en, es | — raw float value |
| shape_id (link) | gtfs:shapePoint | gtfs:Shape | gtfs:ShapePoint | `ex:shape/{shape_id}` | shape_id matches in both classes |  |  | — Create triple: `ex:shape/{id} gtfs:shapePoint ex:shapePoint/{id}/{sequence}` |
