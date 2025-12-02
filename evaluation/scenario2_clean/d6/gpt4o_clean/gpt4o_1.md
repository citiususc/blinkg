| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
|------------|-------------------|--------------|----------------------|--------------------|----------------|----------|----------------------|---------------|
| trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | urn:trip:{trip_id} | stop_times.csv.trip_id = trips.csv.trip_id || | |
| arrival_time | gtfs:arrivalTime | gtfs:StopTime |  | urn:stop_time:{trip_id}_{stop_sequence} |  | schema:Time |  ||
| departure_time | gtfs:departureTime | gtfs:StopTime |  | urn:stop_time:{trip_id}_{stop_sequence} |  | schema:Time |  ||
| stop_id | gtfs:stop | gtfs:StopTime | gtfs:Stop | urn:stop:{stop_id} | stop_times.csv.stop_id = stops.csv.stop_id || | |
| stop_sequence | gtfs:stopSequence | gtfs:StopTime |  | urn:stop_time:{trip_id}_{stop_sequence} |  | xsd:nonNegativeInteger |  ||
| stop_headsign | gtfs:headsign | gtfs:StopTime |  | urn:stop_time:{trip_id}_{stop_sequence} |  | xsd:string |  | String |
| pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | urn:stop_time:{trip_id}_{stop_sequence} |  || mapPickupType | 0 : http://transport.linkeddata.es/kos/pickup/available <br> 1 : http://transport.linkeddata.es/kos/pickup/not-available <br> 2 : http://transport.linkeddata.es/kos/pickup/must-phone <br> 3 : http://transport.linkeddata.es/kos/pickup/coordinate-with-driver |
| drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | urn:stop_time:{trip_id}_{stop_sequence} |  || mapDropOffType |0 : http://transport.linkeddata.es/kos/drop-off/available <br> 1 : http://transport.linkeddata.es/kos/drop-off/not-available <br> 2 : http://transport.linkeddata.es/kos/drop-off/must-phone <br> 3 : http://transport.linkeddata.es/kos/drop-off/coordinate-with-driver|
| shape_dist_traveled | gtfs:distanceTraveled | gtfs:StopTime |  | urn:stop_time:{trip_id}_{stop_sequence} |  | gtfs:nonNegativeFloat |  ||
