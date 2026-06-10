| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| frequencies.csv trip_id | gtfs:trip | gtfs:Frequency | gtfs:Trip | ex:frequency/{trip_id}_{start_time} | trips.trip_id=frequency.trip_id | xsd:string | - | - |
| frequencies.csv start_time | gtfs:startTime | gtfs:Frequency | - | ex:frequency/{trip_id}_{start_time} | - | schema:startTime | - | - |
| frequencies.csv end_time | gtfs:endTime | gtfs:Frequency | - | ex:frequency/{trip_id}_{start_time} | - | schema:endTime | - | - |
| frequencies.csv headway_secs | gtfs:headwaySeconds | gtfs:Frequency | - | ex:frequency/{trip_id}_{start_time} | - | xsd:positiveInteger | - | - |
| frequencies.csv exact_times | gtfs:usesExactTimes | gtfs:Frequency | skos:Concept | ex:frequency/{trip_id}_{start_time} | - | - | - | directionSKOS 0 -> `http://transport.linkeddata.es/kos/direction/one-direction` <br> 1 -> `http://transport.linkeddata.es/kos/direction/opposite-direction` |
| trips.csv trip_id | gtfs:id | gtfs:Trip | - | ex:trip/{trip_id} | - | xsd:string | - | - |
| trips.csv trip_headsign | gtfs:headsign | gtfs:Trip | - | ex:trip/{trip_id} | - | xsd:string | - | capitalize Input string in capital format |
| trips.csv trip_short_name | gtfs:shortName | gtfs:Trip | - | ex:trip/{trip_id} | - | foaf:name | - | capitalize Input string in capital format |
| trips.csv direction_id | gtfs:direction | gtfs:Trip | skos:Concept | ex:trip/{trip_id} | - | - | - | directionSKOS 0 -> `http://transport.linkeddata.es/kos/direction/one-direction` <br> 1 -> `http://transport.linkeddata.es/kos/direction/opposite-direction` |
| trips.csv wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | ex:trip/{trip_id} | - | - | - | wheelchairBoardingSKOS 0 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information` <br> 1 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible` <br>  2 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |
| trips.csv route_id | gtfs:route | gtfs:Trip | gtfs:Route | ex:trip/{trip_id} | trips.route_id=routes.route_id | xsd:string | - | - |
| trips.csv service_id | gtfs:service | gtfs:Trip | gtfs:Service | ex:trip/{trip_id} | trips.service_id=calendar.service_id or trips.service_id=calendar_dates.service_id | xsd:string | - | - |
