| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id | gtfs:id | gtfs:Trip | - | ex:trip/{trip_id} | - | xsd:string | - | - |
| trip_headsign | gtfs:headsign | gtfs:Trip | - | ex:trip/{trip_id} | - | xsd:string | - | capitalize Input string in capital format |
| trip_short_name | gtfs:shortName | gtfs:Trip | - | ex:trip/{trip_id} | - | xsd:string | - | capitalize Input string in capital format |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept | ex:trip/{trip_id} | - | - | - | directionSKOS 0 -> `http://transport.linkeddata.es/kos/direction/one-direction` <br> 1 -> `http://transport.linkeddata.es/kos/direction/opposite-direction` |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | ex:trip/{trip_id} | - | - | - | wheelchairBoardingSKOS 0 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information` <br> 1 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible` <br>  2 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |
| trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | ex:stoptimes/{trip_id}_{stop_sequence} | stop_times.trip_id=trips.trip_id | - | - | - |
| arrival_time | gtfs:arrivalTime | gtfs:StopTime | - | ex:stoptimes/{trip_id}_{stop_sequence} | - | schema:Time | - | - |
| stop_sequence | gtfs:departureTime | gtfs:StopTime | - | ex:stoptimes/{trip_id}_{stop_sequence} | - | schema:Time | - | - |
| stop_id | gtfs:stop | gtfs:StopTime | gtfs:Stop | ex:stoptimes/{trip_id}_{stop_sequence} | stop_times.stop_id=stops.stop_id | - | - | - |
| departure_time | gtfs:stopSequence | gtfs:StopTime | - | ex:stoptimes/{trip_id}_{stop_sequence} | - | xsd:nonNegativeInteger | - | - |
| stop_headsign | gtfs:headsign | gtfs:StopTime | - | ex:stoptimes/{trip_id}_{stop_sequence} | - | xsd:string | - | capitalize Input string in capital format |
| shape_dist_traveled | gtfs:distancedTraveled | gtfs:StopTime | - | ex:stoptimes/{trip_id}_{stop_sequence} | - | xsd:nonNegativeFloat | - | - |
| pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | ex:stoptimes/{trip_id}_{stop_sequence} | - | - | - | pickupSKOS 0 -> `http://transport.linkeddata.es/kos/pickup/available` <br> 1 -> `http://transport.linkeddata.es/kos/pickup/not-avaliable` <br>  2 -> `http://transport.linkeddata.es/kos/pickup/must-phone` <br> 3 -> `http://transport.linkeddata.es/kos/pickup/coordinate-with-driver` |
| drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | ex:stoptimes/{trip_id}_{stop_sequence} | - | - | - | dropOffSKOS 0 -> `http://transport.linkeddata.es/kos/drop-off/available` <br> 1 -> `http://transport.linkeddata.es/kos/drop-off/not-available` <br>  2 -> `http://transport.linkeddata.es/kos/drop-off/must-phone` <br> 3 -> `http://transport.linkeddata.es/kos/drop-off/coordinate-with-driver` |
