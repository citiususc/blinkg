| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `service_id` | `gtfs:id` | `gtfs:Service` |  | `ex:Service/{service_id}` |  | string |  |  e.g., `ex:Service/4_I12` |
| `monday` | `gtfs:monday` | `gtfs:CalendarRule` | `skos:Concept` | `ex:CalendarRule/{service_id}` | `service_id = service_id` | boolean |  | `mapDayAvailability` "Available" or "Not Available" (linked to SKOS concepts) |
| `tuesday` | `gtfs:tuesday` | `gtfs:CalendarRule` | `skos:Concept` | `ex:CalendarRule/{service_id}` | `service_id = service_id` | boolean |  | `mapDayAvailability` "Available" or "Not Available" |
| `wednesday` | `gtfs:wednesday` | `gtfs:CalendarRule` | `skos:Concept` | `ex:CalendarRule/{service_id}` | `service_id = service_id` | boolean |  | `mapDayAvailability` "Available" or "Not Available" |
| `thursday` | `gtfs:thursday` | `gtfs:CalendarRule` | `skos:Concept` | `ex:CalendarRule/{service_id}` | `service_id = service_id` | boolean |  | `mapDayAvailability` "Available" or "Not Available" |
| `friday` | `gtfs:friday` | `gtfs:CalendarRule` | `skos:Concept` | `ex:CalendarRule/{service_id}` | `service_id = service_id` | boolean |  | `mapDayAvailability` "Available" or "Not Available" |
| `saturday` | `gtfs:saturday` | `gtfs:CalendarRule` | `skos:Concept` | `ex:CalendarRule/{service_id}` | `service_id = service_id` | boolean |  | `mapDayAvailability` "Available" or "Not Available" |
| `sunday` | `gtfs:sunday` | `gtfs:CalendarRule` | `skos:Concept` | `ex:CalendarRule/{service_id}` | `service_id = service_id` | boolean |  | `mapDayAvailability` "Available" or "Not Available" |
| `start_date` | `gtfs:startDate` | `gtfs:CalendarRule` |  | `ex:CalendarRule/{service_id}` | `service_id = service_id` | date |  |  ISO 8601 date format (e.g., `2017-06-29`) |
| `end_date` | `gtfs:endDate` | `gtfs:CalendarRule` |  | `ex:CalendarRule/{service_id}` | `service_id = service_id` | date |  |  ISO 8601 date format (e.g., `2018-06-29`) |
| `service_id` | `gtfs:id` | `gtfs:Service` |  | `ex:Service/{service_id}` |  | string |  |  e.g., `ex:Service/4_I12` |
| `service_id (dates)` | `gtfs:id` | `gtfs:Service` |  | `ex:Service/{service_id}` |  | string |  |  e.g., `ex:Service/4_I12` |
| `date` | `gtfs:date` | `gtfs:CalendarDateRule` |  | `ex:CalendarDateRule/{service_id}/{date}` | `service_id = service_id`, `date = date` | date |  |  ISO 8601 date format (e.g., `2017-01-06`) |
| `exception_type` | `gtfs:exceptionType` | `gtfs:CalendarDateRule` | `skos:Concept` | `ex:CalendarDateRule/{service_id}/{date}` | `service_id = service_id`, `date = date` | integer |  | `mapExceptionType` "Added" or "Removed" (linked to SKOS concepts) |

