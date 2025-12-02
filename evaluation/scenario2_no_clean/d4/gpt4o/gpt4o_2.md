| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| service_id | gtfs:id | gtfs:Service |  | `:Service/{service_id}` | `calendar.csv.service_id = calendar_dates.csv.service_id` | xsd:string |  | `generateServiceIDURI` `:Service/4_I12` |
| monday | gtfs:monday | gtfs:CalendarRule | skos:Concept | `:CalendarRule/{service_id}` | Linked via `gtfs:serviceRule` to `gtfs:Service` | xsd:boolean |  | `mapAvailability` `http://transport.linkeddata.es/kos/day/available` or `.../not-available` |
| tuesday | gtfs:tuesday | gtfs:CalendarRule | skos:Concept | Same as monday | Same | xsd:boolean |  | `mapAvailability` Same as monday |
| wednesday | gtfs:wednesday | gtfs:CalendarRule | skos:Concept | Same as monday | Same | xsd:boolean |  | `mapAvailability` Same as monday |
| thursday | gtfs:thursday | gtfs:CalendarRule | skos:Concept | Same as monday | Same | xsd:boolean |  | `mapAvailability` Same as monday |
| friday | gtfs:friday | gtfs:CalendarRule | skos:Concept | Same as monday | Same | xsd:boolean |  | `mapAvailability` Same as monday |
| saturday | gtfs:saturday | gtfs:CalendarRule | skos:Concept | Same as monday | Same | xsd:boolean |  | `mapAvailability` Same as monday |
| sunday | gtfs:sunday | gtfs:CalendarRule | skos:Concept | Same as monday | Same | xsd:boolean |  | `mapAvailability` Same as monday |
| start_date | gtfs:startDate | gtfs:CalendarRule |  | Same as monday | Same | xsd:date |  | `formatDate` Format: `YYYY-MM-DD` |
| end_date | gtfs:endDate | gtfs:CalendarRule |  | Same as monday | Same | xsd:date |  | `formatDate` Same |
| date | gtfs:date | gtfs:CalendarDateRule |  | `:CalendarDateRule/{service_id}/{date}` | `calendar.csv.service_id = calendar_dates.csv.service_id` | xsd:date |  | `formatDate` Same |
| exception_type | gtfs:exceptionType | gtfs:CalendarDateRule | skos:Concept | Same as date | Same | xsd:integer |  | `mapExceptionType` `http://transport.linkeddata.es/kos/exception-type/added` or `/removed` |

