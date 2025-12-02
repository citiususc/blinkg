| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **trips.csv** |  |  |  |  |  |  |  |  |
| trip_id | gtfs:id | gtfs:Trip |  | `generate_trip_subject(trip_id)` |  | xsd:string |  | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |
| trip_headsign | gtfs:headsign | gtfs:Trip |  | `generate_trip_subject(trip_id)` |  | xsd:string |  |  |
| trip_short_name | gtfs:shortName | gtfs:Trip |  | `generate_trip_subject(trip_id)` |  | xsd:string |  |  |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept | `generate_trip_subject(trip_id)` |  |  | `map_direction(direction_id)` | `http://transport.linkeddata.es/kos/direction/one-direction`, `http://transport.linkeddata.es/kos/direction/opposite-direction` |
| block_id | gtfs:block | gtfs:Trip |  | `generate_trip_subject(trip_id)` |  | xsd:string |  |  |
| wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | `generate_trip_subject(trip_id)` |  |  | `map_wheelchair(wheelchair_accessible)` | `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information`, `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible`, `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |
| **stops.csv** |  |  |  |  |  |  |  |  |
| stop_id | gtfs:id | gtfs:Stop / gtfs:Station |  | `generate_stop_subject(stop_id)` |  | xsd:string |  | `http://transport.linkeddata.es/resource/Stop/{stop_id}` |
| stop_lat | gtfs:latitude | gtfs:Stop / gtfs:Station |  | `generate_stop_subject(stop_id)` |  | geo:lat |  |  |
| stop_lon | gtfs:longitude | gtfs:Stop / gtfs:Station |  | `generate_stop_subject(stop_id)` |  | geo:long |  |  |
| parent_station | gtfs:parentStation | gtfs:Stop | gtfs:Station | `generate_stop_subject(stop_id)` | `stops.parent_station == stops.stop_id` |  |  |  |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Stop / gtfs:Station | skos:Concept | `generate_stop_subject(stop_id)` |  |  | `map_wheelchair(wheelchair_boarding)` | `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information`, `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible`, `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |
| **stop_times.csv** |  |  |  |  |  |  |  |  |
| trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | `generate_stop_time_subject(trip_id, stop_sequence)` | `stop_times.trip_id == trips.trip_id` |  |  |  |
| stop_id | gtfs:stop | gtfs:StopTime | gtfs:Stop | `generate_stop_time_subject(trip_id, stop_sequence)` | `stop_times.stop_id == stops.stop_id` |  |  |  |
| arrival_time | gtfs:arrivalTime | gtfs:StopTime |  | `generate_stop_time_subject(trip_id, stop_sequence)` |  | schema:Time |  |  |
| departure_time | gtfs:departureTime | gtfs:StopTime |  | `generate_stop_time_subject(trip_id, stop_sequence)` |  | schema:Time |  |  |
| stop_sequence | gtfs:stopSequence | gtfs:StopTime |  | `generate_stop_time_subject(trip_id, stop_sequence)` |  | xsd:nonNegativeInteger |  |  |
| stop_headsign | gtfs:headsign | gtfs:StopTime |  | `generate_stop_time_subject(trip_id, stop_sequence)` |  | xsd:string |  |  |
| pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | `generate_stop_time_subject(trip_id, stop_sequence)` |  |  | `map_pickup(pickup_type)` | `http://transport.linkeddata.es/kos/pickup/available`, `http://transport.linkeddata.es/kos/pickup/not-available`, `http://transport.linkeddata.es/kos/pickup/must-phone`, `http://transport.linkeddata.es/kos/pickup/coordinate-with-driver` |
| drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | `generate_stop_time_subject(trip_id, stop_sequence)` |  |  | `map_dropoff(drop_off_type)` | `http://transport.linkeddata.es/kos/drop-off/available`, `http://transport.linkeddata.es/kos/drop-off/not-available`, `http://transport.linkeddata.es/kos/drop-off/must-phone`, `http://transport.linkeddata.es/kos/drop-off/coordinate-with-driver` |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:StopTime |  | `generate_stop_time_subject(trip_id, stop_sequence)` |  | gtfs:nonNegativeFloat |  |  |
