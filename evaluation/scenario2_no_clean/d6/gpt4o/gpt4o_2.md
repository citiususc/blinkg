| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | stop_times.trip_id = trips.trip_id | xsd:string | None | generateStopTimeURI `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` |
| arrival_time | gtfs:arrivalTime | gtfs:StopTime | None | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | schema:Time | None | None HH:MM:SS |
| departure_time | gtfs:departureTime | gtfs:StopTime | None | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | schema:Time | None | None HH:MM:SS |
| stop_id (stop_times) | gtfs:stop | gtfs:StopTime | gtfs:Stop | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | stop_times.stop_id = stops.stop_id | xsd:string | None | generateStopURI `http://transport.linkeddata.es/resource/stop/{stop_id}` |
| stop_sequence | gtfs:stopSequence | gtfs:StopTime | None | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | xsd:nonNegativeInteger | None | None Integer |
| stop_headsign | gtfs:headsign | gtfs:StopTime | None | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | xsd:string | None | None Text (Capitalized Words) |
| pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | skos:Concept | None | mapPickupType 0:Available, 1:Not Available, 2:Must Phone, 3:Coordinate With Driver |
| drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | skos:Concept | None | mapDropOffType 0:Available, 1:Not Available, 2:Must Phone, 3:Coordinate With Driver |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:StopTime | None | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | gtfs:nonNegativeFloat | None | None Float |
| stop_id (stops) | gtfs:id | gtfs:Stop | None | `http://transport.linkeddata.es/resource/stop/{stop_id}` | None | xsd:string | None | None String |
| stop_name | rdfs:label | gtfs:Stop | None | `http://transport.linkeddata.es/resource/stop/{stop_id}` | None | xsd:string | es | None Stop name in Spanish |
| stop_lat | gtfs:latitude | gtfs:Stop | None | `http://transport.linkeddata.es/resource/stop/{stop_id}` | None | geo:lat | None | None Decimal |
| stop_lon | gtfs:longitude | gtfs:Stop | None | `http://transport.linkeddata.es/resource/stop/{stop_id}` | None | geo:long | None | None Decimal |
| parent_station | gtfs:parentStation | gtfs:Stop | gtfs:Station | `http://transport.linkeddata.es/resource/stop/{stop_id}` | stops.parent_station = stops.stop_id | xsd:string | None | generateStopURI `http://transport.linkeddata.es/resource/stop/{parent_station}` |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Stop | skos:Concept | `http://transport.linkeddata.es/resource/stop/{stop_id}` | None | skos:Concept | None | mapWheelchairBoarding 0:No information, 1:Accessible, 2:Inaccessible |
| trip_id (trips) | gtfs:id | gtfs:Trip | None | `http://transport.linkeddata.es/resource/trip/{trip_id}` | None | xsd:string | None | None String |
| trip_headsign | gtfs:headsign | gtfs:Trip | None | `http://transport.linkeddata.es/resource/trip/{trip_id}` | None | xsd:string | None | None Text (Capitalized Words) |
| trip_short_name | gtfs:shortName | gtfs:Trip | None | `http://transport.linkeddata.es/resource/trip/{trip_id}` | None | xsd:string | None | None String (Pattern) |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept | `http://transport.linkeddata.es/resource/trip/{trip_id}` | None | skos:Concept | None | mapDirection 0:One Direction, 1:Opposite Direction |
| block_id | gtfs:block | gtfs:Trip | None | `http://transport.linkeddata.es/resource/trip/{trip_id}` | None | xsd:string | None | None String |
| wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | `http://transport.linkeddata.es/resource/trip/{trip_id}` | None | skos:Concept | None | mapWheelchairBoarding 0:No information, 1:Accessible, 2:Inaccessible |

