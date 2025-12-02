| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **calendar.csv** |  |  |  |  |  |  |  |  |
| service_id | gtfs:id | gtfs:Service | - | `http://transport.linkeddata.es/services/{service_id}` | - | xsd:string | - | - |
| service_id | gtfs:serviceRule | gtfs:Service | gtfs:CalendarRule | `http://transport.linkeddata.es/services/{service_id}` | `calendar.service_id` | - | - | - |
| monday | gtfs:monday | gtfs:CalendarRule | skos:Concept | `http://transport.linkeddata.es/calendar_rules/{service_id}` | - | - | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` OR `http://transport.linkeddata.es/kos/day/not-available` |
| tuesday | gtfs:tuesday | gtfs:CalendarRule | skos:Concept | `http://transport.linkeddata.es/calendar_rules/{service_id}` | - | - | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` OR `http://transport.linkeddata.es/kos/day/not-available` |
| wednesday | gtfs:wednesday | gtfs:CalendarRule | skos:Concept | `http://transport.linkeddata.es/calendar_rules/{service_id}` | - | - | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` OR `http://transport.linkeddata.es/kos/day/not-available` |
| thursday | gtfs:thursday | gtfs:CalendarRule | skos:Concept | `http://transport.linkeddata.es/calendar_rules/{service_id}` | - | - | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` OR `http://transport.linkeddata.es/kos/day/not-available` |
| friday | gtfs:friday | gtfs:CalendarRule | skos:Concept | `http://transport.linkeddata.es/calendar_rules/{service_id}` | - | - | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` OR `http://transport.linkeddata.es/kos/day/not-available` |
| saturday | gtfs:saturday | gtfs:CalendarRule | skos:Concept | `http://transport.linkeddata.es/calendar_rules/{service_id}` | - | - | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` OR `http://transport.linkeddata.es/kos/day/not-available` |
| sunday | gtfs:sunday | gtfs:CalendarRule | skos:Concept | `http://transport.linkeddata.es/calendar_rules/{service_id}` | - | - | `map_day_availability` | `http://transport.linkeddata.es/kos/day/available` OR `http://transport.linkeddata.es/kos/day/not-available` |
| start_date | gtfs:startDate | gtfs:CalendarRule | - | `http://transport.linkeddata.es/calendar_rules/{service_id}` | - | schema:startDate | - | - |
| end_date | gtfs:endDate | gtfs:CalendarRule | - | `http://transport.linkeddata.es/calendar_rules/{service_id}` | - | schema:endDate | - | - |
| **calendar_dates.csv** |  |  |  |  |  |  |  |  |
| service_id | gtfs:serviceRule | gtfs:Service | gtfs:CalendarDateRule | `http://transport.linkeddata.es/services/{service_id}` | `calendar_dates.service_id` | - | - | - |
| date | gtfs:date | gtfs:CalendarDateRule | - | `http://transport.linkeddata.es/calendar_date_rules/{service_id}-{date}` | - | xsd:date | - | - |
| exception_type | gtfs:exceptionType | gtfs:CalendarDateRule | skos:Concept | `http://transport.linkeddata.es/calendar_date_rules/{service_id}-{date}` | - | - | `map_exception_type` | `http://transport.linkeddata.es/kos/exception-type/added` OR `http://transport.linkeddata.es/kos/exception-type/removed` |
