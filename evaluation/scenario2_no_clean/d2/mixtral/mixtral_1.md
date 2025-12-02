| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `shape_id` | `gtfs:id` | `gtfs:Shape` | - | `<http://vocab.gtfs.org/terms#>` + `shape_id` | - | `xsd:string` | - | - |
| `shape_pt_lat` | `gtfs:latitude` | `gtfs:ShapePoint` | - | `<http://vocab.gtfs.org/terms#>` + `shape_id` + `"/shape_points/"` + `shape_pt_sequence` | `shape_id` | `geo:lat` | - | - |
| `shape_pt_lon` | `gtfs:longitude` | `gtfs:ShapePoint` | - | `<http://vocab.gtfs.org/terms#>` + `shape_id` + `"/shape_points/"` + `shape_pt_sequence` | `shape_id` | `geo:long` | - | - |
| `shape_pt_sequence` | `gtfs:pointSequence` | `gtfs:ShapePoint` | - | `<http://vocab.gtfs.org/terms#>` + `shape_id` + `"/shape_points/"` + `shape_pt_sequence` | `shape_id` | `xsd:nonNegativeInteger` | - | - |
| `shape_dist_traveled` | `gtfs:distanceTraveled` | `gtfs:ShapePoint` | - | `<http://vocab.gtfs.org/terms#>` + `shape_id` + `"/shape_points/"` + `shape_pt_sequence` | `shape_id` | `gtfs:nonNegativeFloat` | - | - |
