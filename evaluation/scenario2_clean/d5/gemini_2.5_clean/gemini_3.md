| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| trip_id | `gtfs:id` | `gtfs:Trip` | | `ex:Trip/{trip_id}` | | `xsd:string` | | |
| route_id | `gtfs:route` | `gtfs:Trip` | `gtfs:Route` | `ex:Trip/{trip_id}` | `trips.csv.route_id` = `routes.csv.route_id` || `| |
| service_id | `gtfs:service` | `gtfs:Trip` | `gtfs:Service` | `ex:Trip/{trip_id}` | `trips.csv.service_id` = `calendar.csv.service_id` || | |
| shape_id | `gtfs:shape` | `gtfs:Trip` | `gtfs:Shape` | `ex:Trip/{trip_id}` | `trips.csv.shape_id` = `shapes.csv.shape_id` || | |
| trip_headsign | `gtfs:headsign` | `gtfs:Trip` | | `ex:Trip/{trip_id}` | | `xsd:string` | | |
| trip_short_name | `gtfs:shortName` | `gtfs:Trip` | | `ex:Trip/{trip_id}` | | `xsd:string` | | |
| direction_id | `gtfs:direction` | `gtfs:Trip` | `skos:Concept` | `ex:Trip/{trip_id}` | || `map_direction` | `0` -> `http://transport.linkeddata.es/kos/direction/one-direction`<br>`1` -> `http://transport.linkeddata.es/kos/direction/opposite-direction` |
| wheelchair_accessible | `gtfs:wheelchairAccessible` | `gtfs:Trip` | `skos:Concept` | `ex:Trip/{trip_id}` | || `map_wheelchair` | `0` -> `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information`<br>`1` -> `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible`<br>`2` -> `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |
| trip_id | `gtfs:trip` | `gtfs:Frequency` | `gtfs:Trip` | `ex:Frequency/{trip_id}-{start_time}` | `frequencies.csv.trip_id` = `trips.csv.trip_id` || | |
| start_time | `gtfs:startTime` | `gtfs:Frequency` | | `ex:Frequency/{trip_id}-{start_time}` | | `xsd:time` | | |
| end_time | `gtfs:endTime` | `gtfs:Frequency` | | `ex:Frequency/{trip_id}-{start_time}` | | `xsd:time` | | |
| headway_secs | `gtfs:headwaySeconds` | `gtfs:Frequency` | | `ex:Frequency/{trip_id}-{start_time}` | | `xsd:positiveInteger` | | |
| exact_times | `gtfs:usesExactTimes` | `gtfs:Frequency` | `skos:Concept` | `ex:Frequency/{trip_id}-{start_time}` | || `map_exact_times` | `0` -> `http://transport.linkeddata.es/kos/exact-times/frequency`<br>`1` -> `http://transport.linkeddata.es/kos/exact-times/schedule` |
