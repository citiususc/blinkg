| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} | `stop_times.trip_id == trips.trip_id` | | | |
| stop_id | gtfs:stop | gtfs:StopTime | gtfs:Stop | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} | `stop_times.stop_id == stops.stop_id` | | | |
| arrival_time | gtfs:arrivalTime | gtfs:StopTime | | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} | | schema:Time | | |
| departure_time | gtfs:departureTime | gtfs:StopTime | | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} | | schema:Time | | |
| stop_sequence | gtfs:stopSequence | gtfs:StopTime | | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} | | xsd:nonNegativeInteger | | |
| stop_headsign | gtfs:headsign | gtfs:StopTime | | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} | | xsd:string | | |
| pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} | | | `map_pickup(pickup_type)` | `http://transport.linkeddata.es/kos/pickup/available`, `http://transport.linkeddata.es/kos/pickup/not-available`, `http://transport.linkeddata.es/kos/pickup/must-phone`, `http://transport.linkeddata.es/kos/pickup/coordinate-with-driver` |
| drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} | | | `map_dropoff(drop_off_type)` | `http://transport.linkeddata.es/kos/drop-off/available`, `http://transport.linkeddata.es/kos/drop-off/not-available`, `http://transport.linkeddata.es/kos/drop-off/must-phone`, `http://transport.linkeddata.es/kos/drop-off/coordinate-with-driver` |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:StopTime | | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} | | gtfs:nonNegativeFloat | | |
