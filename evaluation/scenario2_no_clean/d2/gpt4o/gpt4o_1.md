| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shape_id | gtfs:id | gtfs:Shape | — | `ex:shape/{shape_id}` | — | xsd:string | none | `generateShapeIRI` `ex:shape/4__1____1__IT_1` |
| shape_pt_lat | gtfs:latitude | gtfs:ShapePoint | — | `ex:shapepoint/{shape_id}/{sequence}` | — | geo:lat | none | `floatToDecimal` e.g., `40.4802624278576` |
| shape_pt_lon | gtfs:longitude | gtfs:ShapePoint | — | `ex:shapepoint/{shape_id}/{sequence}` | — | geo:long | none | `floatToDecimal` e.g., `-3.66723744236574` |
| shape_pt_sequence | gtfs:pointSequence | gtfs:ShapePoint | — | `ex:shapepoint/{shape_id}/{sequence}` | — | xsd:nonNegativeInteger | none | `intSequence` e.g., `1000001` |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:ShapePoint | — | `ex:shapepoint/{shape_id}/{sequence}` | — | gtfs:nonNegativeFloat | none | `floatToDecimal` e.g., `0.047428346568` |
| shape_id (link) | gtfs:shapePoint | gtfs:Shape | gtfs:ShapePoint | `ex:shape/{shape_id}` | shape_id = shape_id | owl:ObjectProperty | none | `linkShapeToPoints` triple: `ex:shape/4__1____1__IT_1 gtfs:shapePoint ex:shapepoint/4__1____1__IT_1/1000001` |
