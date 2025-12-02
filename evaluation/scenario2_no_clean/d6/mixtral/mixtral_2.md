| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `trip_id` | `gtfs:trip` | `gtfs:Trip` | - | `http://transport.linkeddata.es/mmt/{trip_id}` | - | `URI` | `mintTripUri` | `http://transport.linkeddata.es/mmt/4_I12-001_2016I12_1_1_4___` |
| `arrival_time` | `gtfs:arrivalTime` | `gtfs:StopTime` | `gtfs:Trip` | Inferred from `trip_id` | `trip_id` | `Time` | - | `HH:MM:SS` formatted time |
| `departure_time` | `gtfs:departureTime` | `gtfs:StopTime` | `gtfs:Trip` | Inferred from `trip_id` | `trip_id` | `Time` | - | `HH:MM:SS` formatted time |
| `stop_id` | `gtfs:stop` | `gtfs:StopTime` | `gtfs:Stop` | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `URI` | `mintStopUri` | `http://transport.linkeddata.es/stop/00010` |
| `stop_sequence` | `gtfs:stopSequence` | `gtfs:StopTime` | `gtfs:Trip` | Inferred from `trip_id` | `trip_id` | `Integer` | - | Ordinal number |
| `stop_headsign` | `gtfs:headsign` | `gtfs:StopTime` | `gtfs:Trip` | Inferred from `trip_id` | `trip_id` | `String` | - | `"VALDECARROS"` or similar |
| `pickup_type` | `gtfs:pickupType` | `gtfs:StopTime` | `gtfs:Stop` | Inferred from `stop_id` | `stop_id` | `skos:Concept` | `mapPickupType` | URI like `http://transport.linkeddata.es/kos/pickup/available` |
| `drop_off_type` | `gtfs:dropOffType` | `gtfs:StopTime` | `gtfs:Stop` | Inferred from `stop_id` | `stop_id` | `skos:Concept` | `mapDropOffType` | URI like `http://transport.linkeddata.es/kos/drop-off/must-phone` |
| `shape_dist_traveled` | `gtfs:distanceTraveled` | `gtfs:StopTime` | `gtfs:Shape` | Inferred from `shape_id` | `shape_id` | `Float` | - | Distance in meters (e.g., `104.528`) |

| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `http://transport.linkeddata.es/kos/pickup/available` |
| 1 | `http://transport.linkeddata.es/kos/pickup/not-available` |
| 2 | `http://transport.linkeddata.es/kos/pickup/must-phone` |
| 3 | `http://transport.linkeddata.es/kos/pickup/coordinate-with-driver` |

| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `http://transport.linkeddata.es/kos/drop-off/available` |
| 1 | `http://transport.linkeddata.es/kos/drop-off/not-available` |
| 2 | `http://transport.linkeddata.es/kos/drop-off/must-phone` |
| 3 | `http://transport.linkeddata.es/kos/drop-off/coordinate-with-driver` |
