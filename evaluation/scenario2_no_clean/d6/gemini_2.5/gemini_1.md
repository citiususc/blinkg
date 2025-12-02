| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **stops.csv** |  |  |  |  |  |  |  |  |
| stop_id | gtfs:id | gtfs:Stop |  | `http://transport.linkeddata.es/resource/Stop/{stop_id}` |  | xsd:string |  |  |
| stop_code | dct:identifier | gtfs:Stop |  | `http://transport.linkeddata.es/resource/Stop/{stop_id}` |  | xsd:string |  |  |
| stop_name | rdfs:label | gtfs:Stop |  | `http://transport.linkeddata.es/resource/Stop/{stop_id}` |  | xsd:string |  |  |
| stop_desc | dct:description | gtfs:Stop |  | `http://transport.linkeddata.es/resource/Stop/{stop_id}` |  | xsd:string |  |  |
| stop_lat | geo:lat | gtfs:Stop |  | `http://transport.linkeddata.es/resource/Stop/{stop_id}` |  | xsd:decimal |  |  |
| stop_lon | geo:long | gtfs:Stop |  | `http://transport.linkeddata.es/resource/Stop/{stop_id}` |  | xsd:decimal |  |  |
| stop_url | foaf:page | gtfs:Stop |  | `http://transport.linkeddata.es/resource/Stop/{stop_id}` |  | xsd:anyURI |  |  |
| parent_station | gtfs:parentStation | gtfs:Stop | gtfs:Station | `http://transport.linkeddata.es/resource/Stop/{stop_id}` | `stops.parent_station` = `stops.stop_id` |  |  | `http://transport.linkeddata.es/resource/Station/{parent_station}` |
| stop_timezone | schema:address | gtfs:Stop |  | `http://transport.linkeddata.es/resource/Stop/{stop_id}` |  | xsd:string |  |  |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Stop | skos:Concept | `http://transport.linkeddata.es/resource/Stop/{stop_id}` |  |  | get_wheelchair_boarding_uri | `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information`, `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible`, `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |
| **trips.csv** |  |  |  |  |  |  |  |  |
| trip_id | gtfs:id | gtfs:Trip |  | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |  | xsd:string |  |  |
| trip_headsign | gtfs:headsign | gtfs:Trip |  | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |  | xsd:string |  |  |
| trip_short_name | gtfs:shortName | gtfs:Trip |  | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |  | xsd:string |  |  |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |  |  | get_direction_uri | `http://transport.linkeddata.es/kos/direction/one-direction`, `http://transport.linkeddata.es/kos/direction/opposite-direction` |
| block_id | gtfs:block | gtfs:Trip |  | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |  | xsd:string |  |  |
| wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |  |  | get_wheelchair_boarding_uri | `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information`, `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible`, `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |
| **stop_times.csv** |  |  |  |  |  |  |  |  |
| trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | `http://transport.linkeddata.es/resource/StopTime/{trip_id}-{stop_sequence}` | `stop_times.trip_id` = `trips.trip_id` |  |  | `http://transport.linkeddata.es/resource/Trip/{trip_id}` |
| arrival_time | gtfs:arrivalTime | gtfs:StopTime |  | `http://transport.linkeddata.es/resource/StopTime/{trip_id}-{stop_sequence}` |  | xsd:time |  |  |
| departure_time | gtfs:departureTime | gtfs:StopTime |  | `http://transport.linkeddata.es/resource/StopTime/{trip_id}-{stop_sequence}` |  | xsd:time |  |  |
| stop_id | gtfs:stop | gtfs:StopTime | gtfs:Stop | `http://transport.linkeddata.es/resource/StopTime/{trip_id}-{stop_sequence}` | `stop_times.stop_id` = `stops.stop_id` |  |  | `http://transport.linkeddata.es/resource/Stop/{stop_id}` |
| stop_sequence | gtfs:stopSequence | gtfs:StopTime |  | `http://transport.linkeddata.es/resource/StopTime/{trip_id}-{stop_sequence}` |  | xsd:nonNegativeInteger |  |  |
| stop_headsign | gtfs:headsign | gtfs:StopTime |  | `http://transport.linkeddata.es/resource/StopTime/{trip_id}-{stop_sequence}` |  | xsd:string |  |  |
| pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | `http://transport.linkeddata.es/resource/StopTime/{trip_id}-{stop_sequence}` |  |  | get_pickup_type_uri | `http://transport.linkeddata.es/kos/pickup/available`, `http://transport.linkeddata.es/kos/pickup/not-available`, `http://transport.linkeddata.es/kos/pickup/must-phone`, `http://transport.linkeddata.es/kos/pickup/coordinate-with-driver` |
| drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | `http://transport.linkeddata.es/resource/StopTime/{trip_id}-{stop_sequence}` |  |  | get_drop_off_type_uri | `http://transport.linkeddata.es/kos/drop-off/available`, `http://transport.linkeddata.es/kos/drop-off/not-available`, `http://transport.linkeddata.es/kos/drop-off/must-phone`, `http://transport.linkeddata.es/kos/drop-off/coordinate-with-driver` |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:StopTime |  | `http://transport.linkeddata.es/resource/StopTime/{trip_id}-{stop_sequence}` |  | gtfs:nonNegativeFloat |  |  |
