| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `trip_id` | `gtfs:trip` | `gtfs:StopTime` | `gtfs:Trip` | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_id` | `xsd:string` | - | Trip URI |
| `arrival_time` | `gtfs:arrivalTime` | `gtfs:StopTime` | - | `http://transport.linkeddata.es/stopTime/{stop_id}/{trip_id}` | `stop_id`, `trip_id` | `xsd:time` | `formatTime` | `HH:MM:SS` |
| `departure_time` | `gtfs:departureTime` | `gtfs:StopTime` | - | `http://transport.linkeddata.es/stopTime/{stop_id}/{trip_id}` | `stop_id`, `trip_id` | `xsd:time` | `formatTime` | `HH:MM:SS` |
| `stop_id` | `gtfs:stop` | `gtfs:StopTime` | `gtfs:Stop` | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `xsd:string` | - | Stop URI |
| `stop_sequence` | `gtfs:stopSequence` | `gtfs:StopTime` | - | Same as above | `stop_id`, `trip_id` | `xsd:nonNegativeInteger` | - | Integer |
| `stop_headsign` | `gtfs:headsign` | `gtfs:StopTime` | - | Same as above | `stop_id`, `trip_id` | `xsd:string` | - | Custom headsign text |
| `pickup_type` | `gtfs:pickupType` | `gtfs:StopTime` | SKOS Concept | Same as above | `stop_id`, `trip_id` | `xsd:string` | `mapPickupType` | `http://transport.linkeddata.es/kos/pickup/{pickup_type}` |
| `drop_off_type` | `gtfs:dropOffType` | `gtfs:StopTime` | SKOS Concept | Same as above | `stop_id`, `trip_id` | `xsd:string` | `mapDropOffType` | `http://transport.linkeddata.es/kos/drop-off/{drop_off_type}` |
| `shape_dist_traveled` | `gtfs:distanceTraveled` | `gtfs:StopTime` | - | Same as above | `stop_id`, `trip_id` | `xsd:float` | - | Distance in meters (e.g., `1547.23`) |
| `wheelchair_boarding` | `gtfs:wheelchairAccessible` | `gtfs:Stop` | SKOS Concept | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `xsd:string` | `mapWheelchairBoarding` | `http://transport.linkeddata.es/kos/wheelchair-accesible/{wheelchair_boarding}` |
| `direction_id` | `gtfs:direction` | `gtfs:Trip` | SKOS Concept | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_id` | `xsd:string` | `mapDirection` | `http://transport.linkeddata.es/kos/direction/{direction_id}` |
| `wheelchair_accessible` | `gtfs:wheelchairAccessible` | `gtfs:Trip` | SKOS Concept | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_id` | `xsd:string` | `mapWheelchairAccessible` | `http://transport.linkeddata.es/kos/wheelchair-accesible/{wheelchair_accessible}` |
