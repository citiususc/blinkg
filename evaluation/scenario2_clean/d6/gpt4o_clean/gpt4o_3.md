| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
|------------|-------------------|--------------|----------------------|--------------------|----------------|----------|----------------------|---------------|
| trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | `concat('http://example.org/StopTime/', trip_id, '_', stop_id)` | stop_times.trip_id = trips.trip_id || None | None |
| arrival_time | gtfs:arrivalTime | gtfs:StopTime | None | None | None | schema:Time | None | None |
| departure_time | gtfs:departureTime | gtfs:StopTime | None | None | None | schema:Time | None | None |
| stop_id | gtfs:stop | gtfs:StopTime | gtfs:Stop | `concat('http://example.org/Stop/', stop_id)` | stop_times.stop_id = stops.stop_id || None | None |
| stop_sequence | gtfs:stopSequence | gtfs:StopTime | None | None | None | xsd:nonNegativeInteger | None | None |
| stop_headsign | gtfs:headsign | gtfs:StopTime | None | None | None | xsd:string | None | None |
| pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | None | None || mapPickupType | `http://transport.linkeddata.es/kos/pickup/` `{0: 'Available', 1: 'Not Available', 2: 'Must Phone', 3: 'Coordinate With Driver'}` |
| drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | None | None || mapDropOffType | `http://transport.linkeddata.es/kos/drop-off/` `{0: 'Available', 1: 'Not Available', 2: 'Must Phone', 3: 'Coordinate With Driver'}` |
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:StopTime | None | None | None | gtfs:nonNegativeFloat | None | None |