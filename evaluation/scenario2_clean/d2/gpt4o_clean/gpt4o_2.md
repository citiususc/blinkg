| CSV Column           | Ontology Property        | Entity Class     | Related Entity Class | Subject Generation                 | Join              | Datatype             |
|----------------------|--------------------------|------------------|----------------------|------------------------------------|-----------------------------|-----------------------|
| shape_id             | gtfs:id                  | gtfs:Shape       |                      | `ex:shape/{shape_id}`              |                             | xsd:string            |
| shape_pt_lat         | gtfs:latitude            | gtfs:ShapePoint  |                      | `ex:shapePoint/{shape_id}_{seq}`   | shape_id + shape_pt_sequence | geo:lat               |
| shape_pt_lon         | gtfs:longitude           | gtfs:ShapePoint  |                      | `ex:shapePoint/{shape_id}_{seq}`   | shape_id + shape_pt_sequence | geo:long              |
| shape_pt_sequence    | gtfs:pointSequence       | gtfs:ShapePoint  |                      | `ex:shapePoint/{shape_id}_{seq}`   | shape_id + shape_pt_sequence | xsd:nonNegativeInteger |
| shape_dist_traveled  | gtfs:distanceTraveled    | gtfs:ShapePoint  |                      | `ex:shapePoint/{shape_id}_{seq}`   | shape_id + shape_pt_sequence | gtfs:nonNegativeFloat |
| shape_id             | gtfs:shapePoint (relates)| gtfs:Shape       | gtfs:ShapePoint      | `ex:shape/{shape_id}`              | shape_id                    |                       |
