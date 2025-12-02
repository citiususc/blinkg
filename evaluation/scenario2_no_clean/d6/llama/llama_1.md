| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `trip_id` | `gtfs:trip` | `gtfs:StopTime` | `gtfs:Trip` | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_id` | `xsd:string` | - | - |
| `arrival_time` | `gtfs:arrivalTime` | `gtfs:StopTime` | - | `http://transport.linkeddata.es/stopTime/{stop_id}/{trip_id}` | `stop_id, trip_id` | `schema:Time` | `formatTime` | `HH:MM:SS` |
| `departure_time` | `gtfs:departureTime` | `gtfs:StopTime` | - | `http://transport.linkeddata.es/stopTime/{stop_id}/{trip_id}` | `stop_id, trip_id` | `schema:Time` | `formatTime` | `HH:MM:SS` |
| `stop_id` | `gtfs:stop` | `gtfs:StopTime` | `gtfs:Stop` | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `xsd:string` | - | - |
| `stop_sequence` | `gtfs:stopSequence` | `gtfs:StopTime` | - | `http://transport.linkeddata.es/stopTime/{stop_id}/{trip_id}` | `stop_id, trip_id` | `xsd:nonNegativeInteger` | - | - |
| `stop_headsign` | `gtfs:headsign` | `gtfs:StopTime` | - | `http://transport.linkeddata.es/stopTime/{stop_id}/{trip_id}` | `stop_id, trip_id` | `xsd:string` | - | - |
| `pickup_type` | `gtfs:pickupType` | `gtfs:StopTime` | - | `http://transport.linkeddata.es/stopTime/{stop_id}/{trip_id}` | `stop_id, trip_id` | `skos:Concept` | `mapPickupType` | `http://transport.linkeddata.es/kos/pickup/{pickup_type}` |
| `drop_off_type` | `gtfs:dropOffType` | `gtfs:StopTime` | - | `http://transport.linkeddata.es/stopTime/{stop_id}/{trip_id}` | `stop_id, trip_id` | `skos:Concept` | `mapDropOffType` | `http://transport.linkeddata.es/kos/drop-off/{drop_off_type}` |
| `shape_dist_traveled` | `gtfs:distanceTraveled` | `gtfs:StopTime` | - | `http://transport.linkeddata.es/stopTime/{stop_id}/{trip_id}` | `stop_id, trip_id` | `gtfs:nonNegativeFloat` | - | - |
| `stop_code` | `gtfs:id` | `gtfs:Stop` | - | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `xsd:string` | - | - |
| `stop_name` | `gtfs:shortName` | `gtfs:Stop` | - | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `xsd:string` | - | - |
| `stop_desc` | `gtfs:shortName` | `gtfs:Stop` | - | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `xsd:string` | - | - |
| `stop_lat` | `gtfs:latitude` | `gtfs:Stop` | - | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `geo:lat` | - | - |
| `stop_lon` | `gtfs:longitude` | `gtfs:Stop` | - | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `geo:long` | - | - |
| `zone_id` | `gtfs:id` | `gtfs:Zone` | - | `http://transport.linkeddata.es/zone/{zone_id}` | `zone_id` | `xsd:string` | - | - |
| `stop_url` | `gtfs:id` | `gtfs:Stop` | - | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `xsd:string` | - | - |
| `location_type` | `gtfs:id` | `gtfs:Location` | - | `http://transport.linkeddata.es/location/{location_type}` | `location_type` | `xsd:string` | - | - |
| `parent_station` | `gtfs:parentStation` | `gtfs:Stop` | `gtfs:Station` | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `xsd:string` | - | - |
| `stop_timezone` | `gtfs:id` | `gtfs:Stop` | - | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `xsd:string` | - | - |
| `wheelchair_boarding` | `gtfs:wheelchairAccessible` | `gtfs:Stop` | - | `http://transport.linkeddata.es/stop/{stop_id}` | `stop_id` | `skos:Concept` | `mapWheelchairBoarding` | `http://transport.linkeddata.es/kos/wheelchair-accesible/{wheelchair_boarding}` |
| `route_id` | `gtfs:id` | `gtfs:Route` | - | `http://transport.linkeddata.es/route/{route_id}` | `route_id` | `xsd:string` | - | - |
| `service_id` | `gtfs:id` | `gtfs:Service` | - | `http://transport.linkeddata.es/service/{service_id}` | `service_id` | `xsd:string` | - | - |
| `trip_id (trips)` | `gtfs:trip` | `gtfs:Trip` | - | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_id` | `xsd:string` | - | - |
| `trip_headsign` | `gtfs:headsign` | `gtfs:Trip` | - | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_id` | `xsd:string` | - | - |
| `trip_short_name` | `gtfs:shortName` | `gtfs:Trip` | - | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_id` | `xsd:string` | - | - |
| `direction_id` | `gtfs:direction` | `gtfs:Trip` | - | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_id` | `skos:Concept` | `mapDirection` | `http://transport.linkeddata.es/kos/direction/{direction_id}` |
| `block_id` | `gtfs:block` | `gtfs:Trip` | - | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_id` | `xsd:string` | - | - |
| `shape_id` | `gtfs:id` | `gtfs:Shape` | - | `http://transport.linkeddata.es/shape/{shape_id}` | `shape_id` | `xsd:string` | - | - |
| `wheelchair_accessible` | `gtfs:wheelchairAccessible` | `gtfs:Trip` | - | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_id` | `skos:Concept` | `mapWheelchairAccessible` | `http://transport.linkeddata.es/kos/wheelchair-accesible/{wheelchair_accessible}` |
