| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | `concat('http://example.org/StopTime/', trip_id, '_', stop_id)` | trip_id = trips.trip_id | IRI | None | None |
| arrival_time | gtfs:arrivalTime | gtfs:StopTime | None | None | None | schema:Time | None | None |
| departure_time | gtfs:departureTime | gtfs:StopTime | None | None | None | schema:Time | None | None |
| stop_id | gtfs:stop | gtfs:StopTime | gtfs:Stop | `concat('http://example.org/Stop/', stop_id)` | stop_id = stops.stop_id | IRI | None | None |
| stop_sequence | gtfs:stopSequence | gtfs:StopTime | None | None | None | xsd:nonNegativeInteger | None | None |
| stop_headsign | gtfs:headsign | gtfs:StopTime | None | None | None | xsd:string | @es/@en | None |
| pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | None | None | IRI | None | mapPickupType `{0: 'Available', 1: 'Not Available', 2: 'Must Phone', 3: 'Coordinate With Driver'}` |
| drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | None | None | IRI | None | mapDropOffType `{0: 'Available', 1: 'Not Available', 2: 'Must Phone', 3: 'Coordinate With Driver'}` |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:StopTime | None | None | None | gtfs:nonNegativeFloat | None | None |
| stop_id | gtfs:id | gtfs:Stop | None | `concat('http://example.org/Stop/', stop_id)` | None | xsd:string | None | None |
| stop_code | dct:identifier | gtfs:Stop | None | None | None | xsd:string | None | None |
| stop_name | dct:title | gtfs:Stop | None | None | None | xsd:string | @es/@en | None |
| stop_desc | dct:description | gtfs:Stop | None | None | None | xsd:string | @es/@en | None |
| stop_lat | gtfs:latitude | gtfs:Stop | None | None | None | geo:lat | None | None |
| stop_lon | gtfs:longitude | gtfs:Stop | None | None | None | geo:long | None | None |
| zone_id | gtfs:id | gtfs:Stop | None | None | None | xsd:string | None | None |
| stop_url | foaf:homepage | gtfs:Stop | None | None | None | xsd:anyURI | None | None |
| location_type | gtfs:locationType | gtfs:Stop | None | None | None | xsd:nonNegativeInteger | None | None |
| parent_station | gtfs:parentStation | gtfs:Stop | gtfs:Station | `concat('http://example.org/Station/', parent_station)` | None | IRI | None | None |
| stop_timezone | gtfs:timezone | gtfs:Stop | None | None | None | xsd:string | None | None |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Stop | skos:Concept | None | None | IRI | None | mapWheelchair `{0: 'No information', 1: 'Accesible', 2: 'Inaccesible'}` |
| route_id | gtfs:id | gtfs:Trip | None | `concat('http://example.org/Trip/', trip_id)` | None | xsd:string | None | None |
| service_id | gtfs:id | gtfs:Trip | None | None | None | xsd:string | None | None |
| trip_id | gtfs:id | gtfs:Trip | None | `concat('http://example.org/Trip/', trip_id)` | None | xsd:string | None | None |
| trip_headsign | gtfs:headsign | gtfs:Trip | None | None | None | xsd:string | @es/@en | None |
| trip_short_name | gtfs:shortName | gtfs:Trip | None | None | None | xsd:string | None | None |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept | None | None | IRI | None | mapDirection `{0: 'One Direction', 1: 'Opposite Direction'}` |
| block_id | gtfs:block | gtfs:Trip | None | None | None | xsd:string | None | None |
| shape_id | gtfs:id | gtfs:Trip | None | None | None | xsd:string | None | None |
| wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | None | None | IRI | None | mapWheelchair `{0: 'No information', 1: 'Accesible', 2: 'Inaccesible'}` |
