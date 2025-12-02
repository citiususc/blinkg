| CSV Column          | Ontology Property     | Entity Class    | Related Entity Class | Subject Generation                      | Join                    | Datatype               |
|--:-:----------------|--:-:------------------|--:-:------------|--:-:--------------|--:-:------------------------------------|--:-:------------------------------|--:-:-------------------|
| shape_id            | gtfs:id               | gtfs:Shape      | -                 | ex:shape/{shape_id}                     | -                                 | xsd:string             |
| shape_pt_lat        | gtfs:latitude         | gtfs:ShapePoint | -                 | ex:shape/{shape_id}_{shape_pt_sequence} | -                                 | geo:lat                |
| shape_pt_lon        | gtfs:longitude        | gtfs:ShapePoint | -                 | ex:shape/{shape_id}_{shape_pt_sequence} | -                                 | geo:lon                |
| shape_pt_sequence   | gtfs:pointSequence    | gtfs:ShapePoint | -                 | ex:shape/{shape_id}_{shape_pt_sequence} | -                                 | xsd:nonNegativeInteger |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:Shape      | -                 | ex:shape/{shape_id}_{shape_pt_sequence} | -                                 | gtfs:nonNegativeFloat  |
|      -               | gtfs:shapePoint       | gtfs:Shape      | gtfs:ShapePoint   | ex:shape/{shape_id}                     | shapes.shape_id = shapes.shape_id | -                      |
