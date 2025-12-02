| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| service_id | gtfs:id | gtfs:Service |  | `ex:service/{service_id}` |  | xsd:string |  |  |
| service_id | gtfs:serviceRule | gtfs:Service | gtfs:CalendarRule | `ex:service/{service_id}` |  |  |  |  |
| start_date | gtfs:startDate | gtfs:CalendarRule |  | `ex:calendar_rule/{service_id}` |  | schema:startDate |  |  |
| end_date | gtfs:endDate | gtfs:CalendarRule |  | `ex:calendar_rule/{service_id}` |  | schema:endDate |  |  |
| monday | gtfs:monday | gtfs:CalendarRule | skos:Concept | `ex:calendar_rule/{service_id}` |  |  | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` or `http://transport.linkeddata.es/kos/day/not-available` |
| tuesday | gtfs:tuesday | gtfs:CalendarRule | skos:Concept | `ex:calendar_rule/{service_id}` |  |  | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` or `http://transport.linkeddata.es/kos/day/not-available` |
| wednesday | gtfs:wednesday | gtfs:CalendarRule | skos:Concept | `ex:calendar_rule/{service_id}` |  |  | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` or `http://transport.linkeddata.es/kos/day/not-available` |
| thursday | gtfs:thursday | gtfs:CalendarRule | skos:Concept | `ex:calendar_rule/{service_id}` |  |  | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` or `http://transport.linkeddata.es/kos/day/not-available` |
| friday | gtfs:friday | gtfs:CalendarRule | skos:Concept | `ex:calendar_rule/{service_id}` |  |  | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` or `http://transport.linkeddata.es/kos/day/not-available` |
| saturday | gtfs:saturday | gtfs:CalendarRule | skos:Concept | `ex:calendar_rule/{service_id}` |  |  | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` or `http://transport.linkeddata.es/kos/day/not-available` |
| sunday | gtfs:sunday | gtfs:CalendarRule | skos:Concept | `ex:calendar_rule/{service_id}` |  |  | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` or `http://transport.linkeddata.es/kos/day/not-available` |
| service_id | gtfs:serviceRule | gtfs:Service | gtfs:CalendarDateRule | `ex:service/{service_id}` | `calendar.service_id = calendar_dates.service_id` |  |  |  |
| date | gtfs:date | gtfs:CalendarDateRule |  | `ex:calendar_date_rule/{service_id}/{date}` |  | xsd:date |  |  |
| exception_type | gtfs:exceptionType | gtfs:CalendarDateRule | skos:Concept | `ex:calendar_date_rule/{service_id}/{date}` |  |  | `map_exception_type` | `http://transport.linkeddata.es/kos/exception-type/added` or `http://transport.linkeddata.es/kos/exception-type/removed` |
