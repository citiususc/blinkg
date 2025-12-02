| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `trip_id` | `gtfs:id` | `gtfs:Trip` | - | Concatenate `agency_id` and `trip_id` with a hyphen | Replace first `_` with `-` | `xsd:string` | `clean_trip_id` | Cleaned Trip ID (e.g. `agency-1234`) |
| `start_time` | `gtfs:startTime` | `gtfs:Frequency` | - | - | - | `schema:startTime` | `parse_duration` | Parsed duration object or error message |
| `end_time` | `gtfs:endTime` | `gtfs:Frequency` | - | - | - | `schema:endTime` | `parse_duration` | Parsed duration object or error message |
| `headway_secs` | `gtfs:headwaySeconds` | `gtfs:Frequency` | - | - | - | `xsd:positiveInteger` | - | - |
| `exact_times` | `gtfs:usesExactTimes` | `gtfs:Frequency` | `skos:Concept` | Use SKOS URI from `inScheme` | Map: `frequency` or `schedule` | `skos:Concept` | `map_exact_times` | SKOS URI: `/exact-times/frequency` or `/exact-times/schedule` |
| `route_id` | `gtfs:id` | `gtfs:Route` | - | Replace `_` with `-`, concatenate `agency_id` and `route_id` | `route_short_name : route_long_name` | `xsd:string` | `clean_route_id` | Cleaned Route ID |
| `service_id` | `gtfs:id` | `gtfs:Service` | - | Concatenate `agency_id` and `service_id` with a hyphen | Replace first `_` with `-` | `xsd:string` | `clean_service_id` | Cleaned Service ID |
| `direction_id` | `gtfs:direction` | `gtfs:Trip` | `skos:Concept` | Use SKOS URI from `inScheme` | `0` = one-direction, `1` = opposite-direction | `skos:Concept` | `map_direction_id` | SKOS URI: `/direction/one-direction` or `/direction/opposite-direction` |
| `shape_id` | `gtfs:shape` | `gtfs:Trip` | `gtfs:Shape` | - | - | - | - | - |
| `wheelchair_accessible` | `gtfs:wheelchairAccessible` | - | `skos:Concept` | Use SKOS URI from `inScheme` | Map values to accessibility URIs | `skos:Concept` | `map_accessibility` | SKOS URI: `/accesible`, `/inaccesible`, or `/no-information` |
