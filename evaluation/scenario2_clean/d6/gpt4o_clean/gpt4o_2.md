| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype |Function Name | Function Output |
|------------|-------------------|--------------|----------------------|--------------------|----------------|----------|---------------|-----------------|
| trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | stop_times.trip_id = trips.trip_id | || |
| arrival_time | gtfs:arrivalTime | gtfs:StopTime | None | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | schema:Time | None | |
| departure_time | gtfs:departureTime | gtfs:StopTime | None | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | schema:Time | None | |
| stop_id (stop_times) | gtfs:stop | gtfs:StopTime | gtfs:Stop | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | stop_times.stop_id = stops.stop_id | | None | ||
| stop_sequence | gtfs:stopSequence | gtfs:StopTime | None | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | xsd:nonNegativeInteger | None | |
| stop_headsign | gtfs:headsign | gtfs:StopTime | None | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | xsd:string | None | Text (Capitalized Words) |
| pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None |  | mapPickupType | 0:Available, 1:Not Available, 2:Must Phone, 3:Coordinate With Driver |
| drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | | mapDropOffType | 0:Available, 1:Not Available, 2:Must Phone, 3:Coordinate With Driver |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:StopTime | None | `http://transport.linkeddata.es/resource/stopTime/{trip_id}_{stop_sequence}` | None | gtfs:nonNegativeFloat | None | |
