| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `trip_id` | `gtfs:id` | `gtfs:Trip` | - | Value of `trip_id` | - | `xsd:string` | - | - |
| `start_time` | `gtfs:startTime` | `gtfs:Frequency` | `gtfs:Trip` | frequency ID of `trip_id` | match `start_time` | `xsd:time` | `format_time` | Formatted time: `"HH:mm:ss"` |
| `end_time` | `gtfs:endTime` | `gtfs:Frequency` | `gtfs:Trip` | frequency ID of `trip_id` | match `end_time` | `xsd:time` | `format_time` | Formatted time: `"HH:mm:ss"` |
| `headway_secs` | `gtfs:headwaySeconds` | `gtfs:Frequency` | `gtfs:Trip` | frequency ID of `trip_id` | `headway_secs` exists | `xsd:integer` | - | Integer value of `headway_secs` |
| `exact_times` | `gtfs:usesExactTimes` | `gtfs:Frequency` | `gtfs:Trip` | frequency ID of `trip_id` | value exists | `skos:Concept` | `format_exact_times` | URI for `"Frequency"` or `"Schedule"` |

| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `gtfs:trip` | `gtfs:Frequency` | `gtfs:Trip` | - | join via `trip_id` | `gtfs:Trip` | `join_trips` | URI of Trip entity |
| `gtfs:route` | `gtfs:Trip` | `gtfs:Route` | - | `route_id` match | `gtfs:Route` | `join_routes` | URI of Route entity |
| `gtfs:service` | `gtfs:Trip` | `gtfs:Service` | - | `service_id` match | `gtfs:Service` | `join_services` | URI of Service entity |
| `gtfs:shape` | `gtfs:Trip` | `gtfs:Shape` | - | `shape_id` match | `gtfs:Shape` | `join_shapes` | URI of Shape entity |
| `gtfs:direction` | `gtfs:Trip` | `gtfs:Direction` | - | `direction_id` match | `skos:Concept` | `format_direction` | URI for Direction concept |
| `gtfs:wheelchairAccessible` | `gtfs:Trip` | `gtfs:WheelchairAccess` | - | `wheelchair_accessible` match | `skos:Concept` | `format_wheelchairAccess` | URI for Accessibility concept |
