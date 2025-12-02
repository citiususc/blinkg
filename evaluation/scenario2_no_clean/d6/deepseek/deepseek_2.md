| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id | gtfs:trip | StopTime | Trip | stoptime/{trip_id}_{stop_sequence} | stop_times.trip_id = trips.trip_id | - | - | - |
| arrival_time | gtfs:arrivalTime | StopTime | - | - | - | schema:Time (xsd:time) | - | - |
| departure_time | gtfs:departureTime | StopTime | - | - | - | schema:Time (xsd:time) | - | - |
| stop_id | gtfs:stop | StopTime | Stop | - | stop_times.stop_id = stops.stop_id | - | - | - |
| stop_sequence | gtfs:stopSequence | StopTime | - | - | - | xsd:nonNegativeInteger | - | - |
| stop_headsign | gtfs:headsign | StopTime | - | - | - | xsd:string | es | - |
| pickup_type | gtfs:pickupType | StopTime | skos:Concept | - | - | skos:Concept | - | mapPickupType 0 → <http://transport.linkeddata.es/kos/pickup/available>, 1 → .../not-available, 2 → .../must-phone, 3 → .../coordinate-with-driver |
| drop_off_type | gtfs:dropOffType | StopTime | skos:Concept | - | - | skos:Concept | - | mapDropOffType Same pattern as pickup_type mappings |
| shape_dist_traveled | gtfs:distanceTraveled | StopTime | - | - | - | gtfs:nonNegativeFloat | - | - |

| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| stop_id | gtfs:id | Stop | - | stop/{stop_id} | - | xsd:string | - | - |
| stop_name | rdfs:label | Stop | - | - | - | xsd:string | es | - |
| stop_desc | dct:description | Stop | - | - | - | xsd:string | es | - |
| stop_lat | gtfs:latitude | Stop | - | - | - | geo:lat | - | - |
| stop_lon | gtfs:longitude | Stop | - | - | - | geo:long | - | - |
| parent_station | gtfs:parentStation | Stop | Station | - | stops.parent_station = stops.stop_id | - | - | - |
| wheelchair_boarding | gtfs:wheelchairAccessible | Stop | skos:Concept | - | - | skos:Concept | - | mapWheelchairAccessibility 0 → <http://transport.linkeddata.es/kos/wheelchair-accesible/no-information>, 1 → .../accesible, 2 → .../inaccesible |

| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id | gtfs:id | Trip | - | trip/{trip_id} | - | xsd:string | - | - |
| trip_headsign | gtfs:headsign | Trip | - | - | - | xsd:string | es | - |
| trip_short_name | gtfs:shortName | Trip | - | - | - | xsd:string | - | formatShortName Capitalize first letters (e.g., "VALDECARROS" → "Valdecarros") |
| direction_id | gtfs:direction | Trip | skos:Concept | - | - | skos:Concept | - | mapDirection 0 → <http://transport.linkeddata.es/kos/direction/one-direction>, 1 → .../opposite-direction |
| wheelchair_accessible | gtfs:wheelchairAccessible | Trip | skos:Concept | - | - | skos:Concept | - | mapWheelchairAccessibility Same as stops.csv mapping |
