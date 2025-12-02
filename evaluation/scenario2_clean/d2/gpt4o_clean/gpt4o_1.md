| CSV Column          | Ontology Property     | Entity Class     | Related Entity Class | Subject Generation                          | Join         | Datatype            |
|---------------------|-----------------------|------------------|----------------------|---------------------------------------------|------------------------|---------------------|
| shape_id            | gtfs:id               | gtfs:Shape       | —                    | `ex:shape/{shape_id}`                       | —                      | xsd:string          |
| shape_pt_lat        | gtfs:latitude         | gtfs:ShapePoint  | —                    | `ex:shapepoint/{shape_id}/{sequence}`       | —                      | geo:lat             |
| shape_pt_lon        | gtfs:longitude        | gtfs:ShapePoint  | —                    | `ex:shapepoint/{shape_id}/{sequence}`       | —                      | geo:long            |
| shape_pt_sequence   | gtfs:pointSequence    | gtfs:ShapePoint  | —                    | `ex:shapepoint/{shape_id}/{sequence}`       | —                      | xsd:nonNegativeInteger |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:ShapePoint  | —                    | `ex:shapepoint/{shape_id}/{sequence}`       | —                      | gtfs:nonNegativeFloat | 
| shape_id (link)     | gtfs:shapePoint       | gtfs:Shape       | gtfs:ShapePoint      | `ex:shape/{shape_id}`                       | shape_id = shape_id    |  |
