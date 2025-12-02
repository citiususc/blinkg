| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id | gtfs:trip | gtfs:Frequency | gtfs:Trip | ex:frequency/{trip_id}/{start_time} | frequencies.trip_id = trips.trip_id | xsd:string |  |  |
| start_time | gtfs:startTime | gtfs:Frequency |  | ex:frequency/{trip_id}/{start_time} |  | schema:startTime |  |  |
| end_time | gtfs:endTime | gtfs:Frequency |  | ex:frequency/{trip_id}/{start_time} |  | schema:endTime |  |  |
| headway_secs | gtfs:headwaySeconds | gtfs:Frequency |  | ex:frequency/{trip_id}/{start_time} |  | xsd:positiveInteger |  |  |
| exact_times | gtfs:usesExactTimes | gtfs:Frequency | skos:Concept | ex:frequency/{trip_id}/{start_time} |  | skos:Concept | en | map_exact_times 0 → Frequency, 1 → Schedule |
| route_id | gtfs:route | gtfs:Trip | gtfs:Route | ex:trip/{trip_id} | trips.route_id = routes.route_id | xsd:string |  |  |
| service_id | gtfs:service | gtfs:Trip | gtfs:Service | ex:trip/{trip_id} | trips.service_id = calendar.service_id | xsd:string |  |  |
| trip_id | gtfs:id | gtfs:Trip |  | ex:trip/{trip_id} |  | xsd:string |  |  |
| trip_headsign | gtfs:headsign | gtfs:Trip |  | ex:trip/{trip_id} |  | xsd:string | en |  |
| trip_short_name | gtfs:shortName | gtfs:Trip |  | ex:trip/{trip_id} |  | xsd:string | en |  |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept | ex:trip/{trip_id} |  | skos:Concept | en | map_direction 0 → One Direction, 1 → Opposite Direction |
| shape_id | gtfs:shape | gtfs:Trip | gtfs:Shape | ex:trip/{trip_id} | trips.shape_id = shapes.shape_id | xsd:string |  |  |
| wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | ex:trip/{trip_id} |  | skos:Concept | en | map_wheelchair_accessible 0 → No information, 1 → Accesible, 2 → Inaccesible |
