| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **`frequencies.csv`** |  |  |  |  |  |  |  |  |
| `trip_id` | `gtfs:trip` | `gtfs:Frequency` | `gtfs:Trip` | `http://transport.linkeddata.es/resource/Frequency/{trip_id}-{start_time}-{end_time}` | `frequencies.trip_id` = `trips.trip_id` |  |  |  |
| `start_time` | `gtfs:startTime` | `gtfs:Frequency` |  | `http://transport.linkeddata.es/resource/Frequency/{trip_id}-{start_time}-{end_time}` |  | `xsd:time` |  | HH:MM:SS |
| `end_time` | `gtfs:endTime` | `gtfs:Frequency` |  | `http://transport.linkeddata.es/resource/Frequency/{trip_id}-{start_time}-{end_time}` |  | `xsd:time` |  | HH:MM:SS |
| `headway_secs` | `gtfs:headwaySeconds` | `gtfs:Frequency` |  | `http://transport.linkeddata.es/resource/Frequency/{trip_id}-{start_time}-{end_time}` |  | `xsd:positiveInteger` |  |  |
| `exact_times` | `gtfs:usesExactTimes` | `gtfs:Frequency` | `skos:Concept` | `http://transport.linkeddata.es/resource/Frequency/{trip_id}-{start_time}-{end_time}` |  |  | `map_exact_times` | `<http://transport.linkeddata.es/kos/exact-times/frequency>` or `<http://transport.linkeddata.es/kos/exact-times/schedule>` |
| **`trips.csv`** |  |  |  |  |  |  |  |  |
| `trip_id` | `gtfs:id` | `gtfs:Trip` |  | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |  | `xsd:string` |  |  |
| `route_id` | `gtfs:route` | `gtfs:Trip` | `gtfs:Route` | `http://transport.linkeddata.es/resource/Trip/{trip_id}` | `trips.route_id` = `routes.route_id` |  |  |  |
| `service_id` | `gtfs:service` | `gtfs:Trip` | `gtfs:Service` | `http://transport.linkeddata.es/resource/Trip/{trip_id}` | `trips.service_id` = `calendar.service_id` |  |  |  |
| `trip_headsign` | `gtfs:headsign` | `gtfs:Trip` |  | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |  | `xsd:string` |  |  |
| `trip_short_name` | `gtfs:shortName` | `gtfs:Trip` |  | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |  | `xsd:string` |  |  |
| `direction_id` | `gtfs:direction` | `gtfs:Trip` | `skos:Concept` | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |  |  | `map_direction` | `<http://transport.linkeddata.es/kos/direction/one-direction>` or `<http://transport.linkeddata.es/kos/direction/opposite-direction>` |
| `shape_id` | `gtfs:shape` | `gtfs:Trip` | `gtfs:Shape` | `http://transport.linkeddata.es/resource/Trip/{trip_id}` | `trips.shape_id` = `shapes.shape_id` |  |  |  |
| `wheelchair_accessible` | `gtfs:wheelchairAccessible` | `gtfs:Trip` | `skos:Concept` | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |  |  | `map_wheelchair` | `<http://transport.linkeddata.es/kos/wheelchair-accesible/no-information>`, `<.../accesible>`, or `<.../inaccesible>` |
| **`routes.csv`** |  |  |  |  |  |  |  |  |
| `route_id` | `gtfs:id` | `gtfs:Route` |  | `http://transport.linkeddata.es/resource/Route/{route_id}` |  | `xsd:string` |  |  |
| `route_short_name` | `gtfs:shortName` | `gtfs:Route` |  | `http://transport.linkeddata.es/resource/Route/{route_id}` |  | `xsd:string` |  |  |
| **`shapes.csv`** |  |  |  |  |  |  |  |  |
| `shape_id` | `gtfs:id` | `gtfs:Shape` |  | `http://transport.linkeddata.es/resource/Shape/{shape_id}` |  | `xsd:string` |  |  |
| **`calendar.csv`** |  |  |  |  |  |  |  |  |
| `service_id` | `gtfs:id` | `gtfs:Service` |  | `http://transport.linkeddata.es/resource/Service/{service_id}` |  | `xsd:string` |  |  |
