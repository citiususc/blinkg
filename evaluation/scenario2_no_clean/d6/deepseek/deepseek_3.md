| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id (stop_times) | gtfs:trip | gtfs:StopTime | gtfs:Trip | stop_time/{trip_id}/{stop_sequence} | trip_id = trips.trip_id | xsd:anyURI |  |  |
| arrival_time | gtfs:arrivalTime | gtfs:StopTime |  |  |  | schema:Time |  |  |
| departure_time | gtfs:departureTime | gtfs:StopTime |  |  |  | schema:Time |  |  |
| stop_id | gtfs:stop | gtfs:StopTime | gtfs:Stop | stop/{stop_id} | stop_id = stops.stop_id | xsd:anyURI |  |  |
| stop_sequence | gtfs:stopSequence | gtfs:StopTime |  |  |  | xsd:nonNegativeInteger |  |  |
| stop_headsign | gtfs:headsign | gtfs:StopTime |  |  |  | xsd:string (pattern) | @es |  |
| pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept |  |  | xsd:anyURI |  | map_pickup_type 0→<http://transport.linkeddata.es/kos/pickup/available>, 1→<.../not-available> |
| drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept |  |  | xsd:anyURI |  | map_dropoff_type 0→<http://transport.linkeddata.es/kos/drop-off/available>, 1→<.../not-available> |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:StopTime |  |  |  | gtfs:nonNegativeFloat |  |  |
| stop_id (stops) | gtfs:id | gtfs:Stop |  | stop/{stop_id} |  | xsd:string |  |  |
| stop_name | rdfs:label | gtfs:Stop |  |  |  | xsd:string | @es |  |
| stop_lat | gtfs:latitude | gtfs:Stop |  |  |  | geo:lat |  |  |
| stop_lon | gtfs:longitude | gtfs:Stop |  |  |  | geo:long |  |  |
| parent_station | gtfs:parentStation | gtfs:Stop | gtfs:Station | station/{parent_station} | parent_station = stops.stop_id | xsd:anyURI |  |  |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Stop | skos:Concept |  |  | xsd:anyURI |  | map_wheelchair 0→<.../no-information>, 1→<.../accesible>, 2→<.../inaccesible> |
| trip_id (trips) | gtfs:id | gtfs:Trip |  | trip/{trip_id} |  | xsd:string |  |  |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept |  |  | xsd:anyURI |  | map_direction 0→<.../one-direction>, 1→<.../opposite-direction> |
| trip_headsign | gtfs:headsign | gtfs:Trip |  |  |  | xsd:string (pattern) | @es |  |
| wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept |  |  | xsd:anyURI |  | map_wheelchair 1→<.../accesible> |
