| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `gtfs` | `http://vocab.gtfs.org/terms#` |
| `kos-day` | `http://transport.linkeddata.es/kos/day/` |
| `kos-exc` | `http://transport.linkeddata.es/kos/exception-type/` |
| `resource` | `http://transport.linkeddata.es/resource/` |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` |
| `skos` | `http://www.w3.org/2004/02/skos/core#` |

| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **calendar.csv** |
| `service_id` | `gtfs:id` | `gtfs:Service` | N/A | `resource:Service/{service_id}` | N/A | `xsd:string` | N/A | N/A |
| `service_id` | `gtfs:serviceRule` | `gtfs:Service` | `gtfs:CalendarRule` | `resource:Service/{service_id}` | N/A | N/A | N/A | The object is `resource:CalendarRule/{service_id}`. |
| `monday` | `gtfs:monday` | `gtfs:CalendarRule` | `skos:Concept` | `resource:CalendarRule/{service_id}` | N/A | N/A | `map_day_availability` | `kos-day:available` or `kos-day:not-available` |
| `tuesday` | `gtfs:tuesday` | `gtfs:CalendarRule` | `skos:Concept` | `resource:CalendarRule/{service_id}` | N/A | N/A | `map_day_availability` | `kos-day:available` or `kos-day:not-available` |
| `wednesday` | `gtfs:wednesday` | `gtfs:CalendarRule` | `skos:Concept` | `resource:CalendarRule/{service_id}` | N/A | N/A | `map_day_availability` | `kos-day:available` or `kos-day:not-available` |
| `thursday` | `gtfs:thursday` | `gtfs:CalendarRule` | `skos:Concept` | `resource:CalendarRule/{service_id}` | N/A | N/A | `map_day_availability` | `kos-day:available` or `kos-day:not-available` |
| `friday` | `gtfs:friday` | `gtfs:CalendarRule` | `skos:Concept` | `resource:CalendarRule/{service_id}` | N/A | N/A | `map_day_availability` | `kos-day:available` or `kos-day:not-available` |
| `saturday` | `gtfs:saturday` | `gtfs:CalendarRule` | `skos:Concept` | `resource:CalendarRule/{service_id}` | N/A | N/A | `map_day_availability` | `kos-day:available` or `kos-day:not-available` |
| `sunday` | `gtfs:sunday` | `gtfs:CalendarRule` | `skos:Concept` | `resource:CalendarRule/{service_id}` | N/A | N/A | `map_day_availability` | `kos-day:available` or `kos-day:not-available` |
| `start_date` | `gtfs:startDate` | `gtfs:CalendarRule` | N/A | `resource:CalendarRule/{service_id}` | N/A | `xsd:date` | N/A | N/A |
| `end_date` | `gtfs:endDate` | `gtfs:CalendarRule` | N/A | `resource:CalendarRule/{service_id}` | N/A | `xsd:date` | N/A | N/A |
| **calendar_dates.csv** |
| `service_id` | `gtfs:serviceRule` | `gtfs:Service` | `gtfs:CalendarDateRule` | `resource:Service/{service_id}` | `calendar.service_id` = `calendar_dates.service_id` | N/A | N/A | The object is `resource:CalendarDateRule/{service_id}-{date}`. |
| `date` | `gtfs:date` | `gtfs:CalendarDateRule` | N/A | `resource:CalendarDateRule/{service_id}-{date}` | N/A | `xsd:date` | N/A | N/A |
| `exception_type` | `gtfs:exceptionType` | `gtfs:CalendarDateRule` | `skos:Concept` | `resource:CalendarDateRule/{service_id}-{date}` | N/A | N/A | `map_exception_type` | `kos-exc:added` or `kos-exc:removed` |
