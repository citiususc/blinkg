| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id | gtfs:trip | gtfs:Frequency | gtfs:Trip | ex:frequency/{trip_id}/{start_time} | trip_id | xsd:string |  |  |
| start_time | gtfs:startTime | gtfs:Frequency |  | ex:frequency/{trip_id}/{start_time} |  | xsd:time |  |  |
| end_time | gtfs:endTime | gtfs:Frequency |  | ex:frequency/{trip_id}/{start_time} |  | xsd:time |  |  |
| headway_secs | gtfs:headwaySeconds | gtfs:Frequency |  | ex:frequency/{trip_id}/{start_time} |  | xsd:positiveInteger |  |  |
| exact_times | gtfs:usesExactTimes | gtfs:Frequency | skos:Concept (exact-times) | ex:frequency/{trip_id}/{start_time} |  | xsd:integer | @en | mapExactTimes {'0': '.../exact-times/frequency', '1': '.../exact-times/schedule'} |
| trip_id | gtfs:id | gtfs:Trip |  | ex:trip/{trip_id} | trip_id | xsd:string |  |  |
| route_id | gtfs:route | gtfs:Trip | gtfs:Route | ex:trip/{trip_id} | route_id | xsd:string |  |  |
| service_id | gtfs:service | gtfs:Trip | gtfs:Service | ex:trip/{trip_id} | service_id | xsd:string |  |  |
| trip_headsign | gtfs:headsign | gtfs:Trip |  | ex:trip/{trip_id} |  | xsd:string | @es |  |
| trip_short_name | gtfs:shortName | gtfs:Trip |  | ex:trip/{trip_id} |  | xsd:string | @es |  |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept (direction) | ex:trip/{trip_id} |  | xsd:integer | @en | mapDirection {'0': '.../direction/one-direction', '1': '.../direction/opposite-direction'} |
| shape_id | gtfs:shape | gtfs:Trip | gtfs:Shape | ex:trip/{trip_id} | shape_id | xsd:string |  |  |
| wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept (wheelchair-accessible) | ex:trip/{trip_id} |  | xsd:integer | @en | mapWheelchairAccess {'0': '.../wheelchair-accesible/no-information', '1': '.../wheelchair-accesible/accesible', '2': '.../wheelchair-accesible/inaccesible'} |
