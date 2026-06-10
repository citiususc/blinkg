| Data Reference           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| frequencies.csv trip_id | gtfs:trip | gtfs:Frequency | gtfs:Trip | http://example.org/frequency/{trip_id}_{start_time} | frequencies.csv trip_id = trips.csv trip_id | xsd:string | - | - |
| frequencies.csv start_time | gtfs:startTime | gtfs:Frequency | - | http://example.org/frequency/{trip_id}_{start_time} | - | schema:startTime | - | - |
| frequencies.csv end_time | gtfs:endTime | gtfs:Frequency | - | http://example.org/frequency/{trip_id}_{start_time} | - | schema:endTime | - | - |
| frequencies.csv headway_secs | gtfs:headwaySeconds | gtfs:Frequency | - | http://example.org/frequency/{trip_id}_{start_time} | - | xsd:positiveInteger | - | - |
| frequencies.csv exact_times | gtfs:usesExactTimes | gtfs:Frequency | skos:Concept | http://example.org/frequency/{trip_id}_{start_time} | - | - | - | directionSKOS 0 -> `http://transport.linkeddata.es/kos/direction/one-direction` <br> 1 -> `http://transport.linkeddata.es/kos/direction/opposite-direction` |
| trips.csv trip_id | gtfs:id | gtfs:Trip | - | http://example.org/trip/{trip_id} | - | xsd:string | - | - |
| trips.csv trip_headsign | gtfs:headsign | gtfs:Trip | - | http://example.org/trip/{trip_id} | - | xsd:string | - | capitalize Input string in capital format |
| trips.csv trip_short_name | gtfs:shortName | gtfs:Trip | - | http://example.org/trip/{trip_id} | - | foaf:name | - | capitalize Input string in capital format |
| trips.csv direction_id | gtfs:direction | gtfs:Trip | skos:Concept | http://example.org/trip/{trip_id} | - | - | - | directionSKOS 0 -> `http://transport.linkeddata.es/kos/direction/one-direction` <br> 1 -> `http://transport.linkeddata.es/kos/direction/opposite-direction` |
| trips.csv wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | http://example.org/trip/{trip_id} | - | - | - | wheelchairBoardingSKOS 0 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information` <br> 1 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible` <br>  2 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |
| trips.csv route_id | gtfs:route | gtfs:Trip | gtfs:Route | http://example.org/trip/{trip_id} | trips.csv route_id = routes.csv route_id | xsd:string | - | - |
| trips.csv service_id | gtfs:service | gtfs:Trip | gtfs:Service | http://example.org/trip/{trip_id} | trips.csv service_id = calendar.csv service_id or trips.csv service_id = calendar_dates.csv service_id | xsd:string | - | - |
