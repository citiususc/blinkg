| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id | gtfs:trip | gtfs:Frequency | gtfs:Trip | ex:frequency/{trip_id}/{start_time} | frequencies.trip_id = trips.trip_id | xsd:string |  |  |
| start_time | gtfs:startTime | gtfs:Frequency |  |  |  | schema:startTime |  |  |
| end_time | gtfs:endTime | gtfs:Frequency |  |  |  | schema:endTime |  |  |
| headway_secs | gtfs:headwaySeconds | gtfs:Frequency |  |  |  | xsd:positiveInteger |  |  |
| exact_times | gtfs:usesExactTimes | gtfs:Frequency | skos:Concept |  |  | xsd:boolean |  | map_exact_times 0 → Frequency, 1 → Schedule |
| trip_id | gtfs:id | gtfs:Trip |  | ex:trip/{trip_id} |  | xsd:string |  |  |
| trip_headsign | gtfs:headsign | gtfs:Trip |  |  |  | xsd:string | en |  |
| trip_short_name | gtfs:shortName | gtfs:Trip |  |  |  | xsd:string | en |  |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept |  |  | xsd:boolean |  | map_direction 0 → One Direction, 1 → Opposite Direction |
| wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept |  |  | xsd:nonNegativeInteger |  | map_wheelchair 0 → No information, 1 → Accesible, 2 → Inaccesible |
| route_id | gtfs:route | gtfs:Trip | gtfs:Route |  | trips.route_id = routes.route_id | xsd:string |  |  |
| service_id | gtfs:service | gtfs:Trip | gtfs:Service |  | trips.service_id = calendar.service_id | xsd:string |  |  |
| shape_id | gtfs:shape | gtfs:Trip | gtfs:Shape |  | trips.shape_id = shapes.shape_id | xsd:string |  |  |
