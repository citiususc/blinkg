| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | urn:trip:{trip_id} | stop_times.csv.trip_id = trips.csv.trip_id | IRI |  | generateTripIRI urn:trip:{trip_id} |
| arrival_time | gtfs:arrivalTime | gtfs:StopTime |  | urn:stop_time:{trip_id}_{stop_sequence} |  | schema:Time |  |  HH:MM:SS |
| departure_time | gtfs:departureTime | gtfs:StopTime |  | urn:stop_time:{trip_id}_{stop_sequence} |  | schema:Time |  |  HH:MM:SS |
| stop_id | gtfs:stop | gtfs:StopTime | gtfs:Stop | urn:stop:{stop_id} | stop_times.csv.stop_id = stops.csv.stop_id | IRI |  | generateStopIRI urn:stop:{stop_id} |
| stop_sequence | gtfs:stopSequence | gtfs:StopTime |  | urn:stop_time:{trip_id}_{stop_sequence} |  | xsd:nonNegativeInteger |  |  Non-negative integer |
| stop_headsign | gtfs:headsign | gtfs:StopTime |  | urn:stop_time:{trip_id}_{stop_sequence} |  | xsd:string | language neutral |  String |
| pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | urn:stop_time:{trip_id}_{stop_sequence} |  | IRI |  | mapPickupType Available, Not Available, Must Phone, Coordinate With Driver |
| drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | urn:stop_time:{trip_id}_{stop_sequence} |  | IRI |  | mapDropOffType Available, Not Available, Must Phone, Coordinate With Driver |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:StopTime |  | urn:stop_time:{trip_id}_{stop_sequence} |  | gtfs:nonNegativeFloat |  |  Float >= 0 |
| stop_id | gtfs:id | gtfs:Stop |  | urn:stop:{stop_id} |  | xsd:string |  |  String |
| stop_code |  | gtfs:Stop |  | urn:stop:{stop_id} |  | xsd:string |  |  String (custom) |
| stop_name | dct:title | gtfs:Stop |  | urn:stop:{stop_id} |  | xsd:string | language neutral |  Stop name |
| stop_desc | dct:description | gtfs:Stop |  | urn:stop:{stop_id} |  | xsd:string | language neutral |  Stop description |
| stop_lat | gtfs:latitude | gtfs:Stop |  | urn:stop:{stop_id} |  | geo:lat |  |  Float |
| stop_lon | gtfs:longitude | gtfs:Stop |  | urn:stop:{stop_id} |  | geo:long |  |  Float |
| zone_id | gtfs:id | gtfs:Zone |  | urn:zone:{zone_id} | stops.csv.zone_id = zones.csv.zone_id | xsd:string |  |  String |
| stop_url | foaf:homepage | gtfs:Stop |  | urn:stop:{stop_id} |  | xsd:anyURI |  |  URI |
| location_type |  | gtfs:Stop |  | urn:stop:{stop_id} |  | xsd:integer |  |  Integer (custom) |
| parent_station | gtfs:parentStation | gtfs:Stop | gtfs:Station | urn:stop:{stop_id} | stops.csv.parent_station = stops.csv.stop_id | IRI |  | generateStopIRI urn:stop:{parent_station} |
| stop_timezone |  | gtfs:Stop |  | urn:stop:{stop_id} |  | xsd:string |  |  String (custom) |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Stop | skos:Concept | urn:stop:{stop_id} |  | IRI |  | mapWheelchairAccessible No information, Accesible, Inaccesible |
| trip_id | gtfs:id | gtfs:Trip |  | urn:trip:{trip_id} |  | xsd:string |  |  String |
| trip_headsign | gtfs:headsign | gtfs:Trip |  | urn:trip:{trip_id} |  | xsd:string | language neutral |  String |
| trip_short_name | gtfs:shortName | gtfs:Trip |  | urn:trip:{trip_id} |  | xsd:string |  |  String |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept | urn:trip:{trip_id} |  | IRI |  | mapDirection One Direction, Opposite Direction |
| block_id | gtfs:block | gtfs:Trip |  | urn:trip:{trip_id} |  | xsd:string |  |  String |
| shape_id | gtfs:id | gtfs:Shape |  | urn:shape:{shape_id} | trips.csv.shape_id = shapes.csv.shape_id | xsd:string |  |  String |
| wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | urn:trip:{trip_id} |  | IRI |  | mapWheelchairAccessible No information, Accesible, Inaccesible |

