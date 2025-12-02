| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `trip_id` | `gtfs:id` | `gtfs:Trip` | - | `URI("http://linked.data.es/resource/" + trip_id)` | - | `xsd:string` | - | `http://linked.data.es/resource/4_I12-001_2016I12` |
| `arrival_time` | `gtfs:arrivalTime` | `gtfs:StopTime` | - | `subject + "/arrival_time"` | StopTime.trip_id = Trip.id | `schema:Time` | formatTime | `HH:MM:SS` |
| `departure_time` | `gtfs:departureTime` | `gtfs:StopTime` | - | `subject + "/departure_time"` | StopTime.trip_id = Trip.id | `schema:Time` | formatTime | `HH:MM:SS` |
| `stop_id` | `gtfs:id` | `gtfs:Stop` | - | `URI("http://linked.data.es/resource/" + stop_id)` | StopTime.stop_id = Stop.id | `xsd:string` | - | `http://linked.data.es/resource/STOP123` |
| `stop_sequence` | *(implicit)* | `gtfs:StopTime` | - | `subject + "/stop_sequence"` | StopTime.trip_id = Trip.id | `xsd:nonNegativeInteger` | - | Integer sequence (e.g., 1, 2, 3...) |
| `pickup_type` | `gtfs:pickupType` | `gtfs:StopTime` | `skos:Concept` | `subject + "/pickup_type"` | From `http://transport.linkeddata.es/kos/pickup` | `skos:notation` | pickupTypeURI | e.g., `http://transport.linkeddata.es/kos/pickup/available` |
| `drop_off_type` | `gtfs:dropOffType` | `gtfs:StopTime` | `skos:Concept` | `subject + "/drop_off_type"` | From `http://transport.linkeddata.es/kos/drop-off` | `skos:notation` | dropoffTypeURI | e.g., `http://transport.linkeddata.es/kos/drop-off/must-phone` |
| `shape_dist_traveled` | `gtfs:distanceTraveled` | `gtfs:StopTime` | - | `subject + "/shape_dist_traveled"` | StopTime.trip_id = Trip.id | `gtfs:distanceTraveled` | - | Float distance value (e.g., `12.345`) |
