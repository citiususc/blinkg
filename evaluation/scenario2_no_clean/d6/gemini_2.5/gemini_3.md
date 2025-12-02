| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **trips.csv** |  |  |  |  |  |  |  |  |
| trip_id | gtfs:id | gtfs:Trip |  | http://transport.linkeddata.es/madrid/trips/{trip_id} |  | xsd:string |  |  |
| trip_headsign | gtfs:headsign | gtfs:Trip |  | http://transport.linkeddata.es/madrid/trips/{trip_id} |  | xsd:string |  |  |
| trip_short_name | gtfs:shortName | gtfs:Trip |  | http://transport.linkeddata.es/madrid/trips/{trip_id} |  | xsd:string |  |  |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept | http://transport.linkeddata.es/madrid/trips/{trip_id} |  |  | mapDirection | 0: http://transport.linkeddata.es/kos/direction/one-direction <br> 1: http://transport.linkeddata.es/kos/direction/opposite-direction |
| block_id | gtfs:block | gtfs:Trip |  | http://transport.linkeddata.es/madrid/trips/{trip_id} |  | xsd:string |  |  |
| wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | http://transport.linkeddata.es/madrid/trips/{trip_id} |  |  | mapWheelchairAccessible | 0: http://transport.linkeddata.es/kos/wheelchair-accesible/no-information <br> 1: http://transport.linkeddata.es/kos/wheelchair-accesible/accesible <br> 2: http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible |
| **stops.csv** |  |  |  |  |  |  |  |  |
| stop_id | gtfs:id | gtfs:Stop |  | http://transport.linkeddata.es/madrid/stops/{stop_id} |  | xsd:string |  |  |
| stop_name | dct:title | gtfs:Stop |  | http://transport.linkeddata.es/madrid/stops/{stop_id} |  | xsd:string |  |  |
| stop_desc | dct:description | gtfs:Stop |  | http://transport.linkeddata.es/madrid/stops/{stop_id} |  | xsd:string |  |  |
| stop_lat | gtfs:latitude | gtfs:Stop |  | http://transport.linkeddata.es/madrid/stops/{stop_id} |  | geo:lat |  |  |
| stop_lon | gtfs:longitude | gtfs:Stop |  | http://transport.linkeddata.es/madrid/stops/{stop_id} |  | geo:long |  |  |
| stop_url | rdfs:seeAlso | gtfs:Stop |  | http://transport.linkeddata.es/madrid/stops/{stop_id} |  | xsd:anyURI |  |  |
| parent_station | gtfs:parentStation | gtfs:Stop | gtfs:Station | http://transport.linkeddata.es/madrid/stops/{stop_id} | stops.parent_station = stops.stop_id (of parent) |  |  |  |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Stop | skos:Concept | http://transport.linkeddata.es/madrid/stops/{stop_id} |  |  | mapWheelchairAccessible | 0: http://transport.linkeddata.es/kos/wheelchair-accesible/no-information <br> 1: http://transport.linkeddata.es/kos/wheelchair-accesible/accesible <br> 2: http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible |
| **stop_times.csv** |  |  |  |  |  |  |  |  |
| trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} | stop_times.trip_id = trips.trip_id |  |  |  |
| stop_id | gtfs:stop | gtfs:StopTime | gtfs:Stop | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} | stop_times.stop_id = stops.stop_id |  |  |  |
| arrival_time | gtfs:arrivalTime | gtfs:StopTime |  | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} |  | schema:Time |  |  |
| departure_time | gtfs:departureTime | gtfs:StopTime |  | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} |  | schema:Time |  |  |
| stop_sequence | gtfs:stopSequence | gtfs:StopTime |  | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} |  | xsd:nonNegativeInteger |  |  |
| stop_headsign | gtfs:headsign | gtfs:StopTime |  | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} |  | xsd:string |  |  |
| pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} |  |  | mapPickupType | 0: http://transport.linkeddata.es/kos/pickup/available <br> 1: http://transport.linkeddata.es/kos/pickup/not-available <br> 2: http://transport.linkeddata.es/kos/pickup/must-phone <br> 3: http://transport.linkeddata.es/kos/pickup/coordinate-with-driver |
| drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} |  |  | mapDropOffType | 0: http://transport.linkeddata.es/kos/drop-off/available <br> 1: http://transport.linkeddata.es/kos/drop-off/not-available <br> 2: http://transport.linkeddata.es/kos/drop-off/must-phone <br> 3: http://transport.linkeddata.es/kos/drop-off/coordinate-with-driver |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:StopTime |  | http://transport.linkeddata.es/madrid/stop_times/{trip_id}-{stop_sequence} |  | gtfs:nonNegativeFloat |  |  |
