| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id | gtfs:trip | gtfs:Frequency | gtfs:Trip | ex:frequency/{trip_id}_{start_time} | trips.trip_id=frequency.trip_id | xsd:string | - | - |
| start_time | gtfs:startTime | gtfs:Frequency | - | ex:frequency/{trip_id}_{start_time} | - | schema:startTime | - | - |
| end_time | gtfs:endTime | gtfs:Frequency | - | ex:frequency/{trip_id}_{start_time} | - | schema:endTime | - | - |
| headway_secs | gtfs:headwaySeconds | gtfs:Frequency | - | ex:frequency/{trip_id}_{start_time} | - | xsd:positiveInteger | - | - |
| exact_times | gtfs:usesExactTimes | gtfs:Frequency | skos:Concept | ex:frequency/{trip_id}_{start_time} | - | - | - | directionSKOS 0 -> `http://transport.linkeddata.es/kos/direction/one-direction` <br> 1 -> `http://transport.linkeddata.es/kos/direction/opposite-direction` |
| trip_id | gtfs:id | gtfs:Trip | - | ex:trip/{trip_id} | - | xsd:string | - | - |
| trip_headsign | gtfs:headsign | gtfs:Trip | - | ex:trip/{trip_id} | - | xsd:string | - | capitalize Input string in capital format |
| trip_short_name | gtfs:shortName | gtfs:Trip | - | ex:trip/{trip_id} | - | foaf:name | - | capitalize Input string in capital format |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept | ex:trip/{trip_id} | - | - | - | directionSKOS 0 -> `http://transport.linkeddata.es/kos/direction/one-direction` <br> 1 -> `http://transport.linkeddata.es/kos/direction/opposite-direction` |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | ex:trip/{trip_id} | - | - | - | wheelchairBoardingSKOS 0 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information` <br> 1 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible` <br>  2 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |
| route_id | gtfs:route | gtfs:Trip | gtfs:Route | ex:trips/{trip_id} | trips.route_id=routes.route_id | xsd:string | - | - |
| service_id | gtfs:service | gtfs:Trip | gtfs:Service | ex:trips/{trip_id} | trips.service_id=calendar.service_id or trips.service_id=calendar_dates.service_id | xsd:string | - | - |
