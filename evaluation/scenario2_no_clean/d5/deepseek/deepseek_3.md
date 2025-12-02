| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| frequencies.csv |  |  |  |  |  |  |  |  |
| trip_id | gtfs:trip | Frequency | Trip | generateFrequencyID() | trip_id = Trip.id | URI |  | generateFrequencyID http://example.org/frequency/{trip_id}_{start_time}_{end_time} |
| start_time | gtfs:startTime | Frequency |  |  |  | xsd:time |  | parseTime XSD time literal (e.g. "00:00:00"^^xsd:time) |
| end_time | gtfs:endTime | Frequency |  |  |  | xsd:time |  | parseTime XSD time literal |
| headway_secs | gtfs:headwaySeconds | Frequency |  |  |  | xsd:positiveInteger |  |  |
| exact_times | gtfs:usesExactTimes | Frequency | skos:Concept |  |  | URI |  | mapExactTimes 0/empty → http://.../exact-times/frequency<br>1 → http://.../exact-times/schedule |
| trips.csv |  |  |  |  |  |  |  |  |
| trip_id | gtfs:id | Trip |  | http://example.org/trip/{trip_id} |  | xsd:string |  |  |
| route_id | gtfs:route | Trip | Route |  | route_id = Route.id | URI |  |  |
| service_id | gtfs:service | Trip | Service |  | service_id = Service.id | URI |  |  |
| shape_id | gtfs:shape | Trip | Shape |  | shape_id = Shape.id | URI |  |  |
| trip_headsign | gtfs:headsign | Trip |  |  |  | xsd:string | es, en | formatHeadsign Capitalized string (e.g. "Valdecarros") |
| direction_id | gtfs:direction | Trip | skos:Concept |  |  | URI |  | mapDirection 0 → http://.../direction/one-direction<br>1 → http://.../direction/opposite-direction |
| wheelchair_accessible | gtfs:wheelchairAccessible | Trip | skos:Concept |  |  | URI |  | mapWheelchair 0 → http://.../no-information<br>1 → http://.../accesible<br>2 → http://.../inaccesible |
| routes.csv |  |  |  |  |  |  |  |  |
| route_id | gtfs:id | Route |  | http://example.org/route/{route_id} |  | xsd:string |  |  |
| route_short_name | gtfs:shortName | Route |  |  |  | xsd:string | es, en | formatShortName "Line " + value (e.g. "Line 1") |
| route_long_name | dct:description | Route |  |  |  | xsd:string | es, en |  |
| shapes.csv |  |  |  |  |  |  |  |  |
| shape_id | gtfs:id | Shape |  | http://example.org/shape/{shape_id} |  | xsd:string |  |  |
| calendar.csv |  |  |  |  |  |  |  |  |
| service_id | gtfs:id | Service |  | http://example.org/service/{service_id} |  | xsd:string |  |  |
