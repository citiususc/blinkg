| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id (stop_times) | gtfs:trip | StopTime | Trip | stop_time/{trip_id}/{stop_id} | StopTime gtfs:trip = Trip gtfs:id | — | — | — |
| arrival_time | gtfs:arrivalTime | StopTime | — | stop_time/{trip_id}/{stop_id} | — | schema:Time (HH:MM:SS) | — | — |
| departure_time | gtfs:departureTime | StopTime | — | stop_time/{trip_id}/{stop_id} | — | schema:Time (HH:MM:SS) | — | — |
| stop_id (stop_times) | gtfs:stop | StopTime | Stop | stop_time/{trip_id}/{stop_id} | StopTime gtfs:stop = Stop gtfs:id | — | — | — |
| stop_sequence | gtfs:stopSequence | StopTime | — | stop_time/{trip_id}/{stop_id} | — | xsd:nonNegativeInteger | — | — |
| pickup_type | gtfs:pickupType | StopTime | — | stop_time/{trip_id}/{stop_id} | — | skos:Concept | — | map_pickup_type 0 → <http://transport.linkeddata.es/kos/pickup/available> |
| drop_off_type | gtfs:dropOffType | StopTime | — | stop_time/{trip_id}/{stop_id} | — | skos:Concept | — | map_drop_off_type 0 → <http://transport.linkeddata.es/kos/drop-off/available> |
| shape_dist_traveled | gtfs:distanceTraveled | StopTime | — | stop_time/{trip_id}/{stop_id} | — | gtfs:nonNegativeFloat | — | — |
| stop_id (stops) | gtfs:id | Stop | — | stop/{stop_id} | — | xsd:string | — | — |
| stop_name | rdfs:label | Stop | — | stop/{stop_id} | — | xsd:string | @es | — |
| stop_lat | gtfs:latitude | Stop | — | stop/{stop_id} | — | geo:lat (xsd:decimal) | — | — |
| stop_lon | gtfs:longitude | Stop | — | stop/{stop_id} | — | geo:long (xsd:decimal) | — | — |
| parent_station | gtfs:parentStation | Stop | Station | stop/{stop_id} | Stop gtfs:parentStation = Station gtfs:id | — | — | — |
| wheelchair_boarding | gtfs:wheelchairAccessible | Stop | — | stop/{stop_id} | — | skos:Concept | — | map_wheelchair_stop 0 → <http://transport.linkeddata.es/kos/wheelchair-accesible/no-information> <br> 2 → <http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible> |
| direction_id (trips) | gtfs:direction | Trip | — | trip/{trip_id} | — | skos:Concept | — | map_direction 0 → <http://transport.linkeddata.es/kos/direction/one-direction> <br> 1 → <http://transport.linkeddata.es/kos/direction/opposite-direction> |
| wheelchair_accessible | gtfs:wheelchairAccessible | Trip | — | trip/{trip_id} | — | skos:Concept | — | map_wheelchair_trip 1 → <http://transport.linkeddata.es/kos/wheelchair-accesible/accesible> |
| trip_headsign | gtfs:headsign | Trip | — | trip/{trip_id} | — | xsd:string (CamelCase) | — | format_headsign Convert to CamelCase (e.g., "VALDECARROS" → "Valdecarros") |
