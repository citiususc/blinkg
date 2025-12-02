| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `service_id` | `gtfs:id` | `gtfs:Service` | N/A | `gtfs:Service(SERVICE_ID)` | N/A | `xsd:string` | N/A | N/A |
| `monday` | `gtfs:monday` | `gtfs:CalendarRule` | `gtfs:CalendarRule` | `gtfs:CalendarRule(SERVICE_ID)` | N/A | `xsd:boolean` | N/A | N/A |
| `tuesday` | `gtfs:tuesday` | `gtfs:CalendarRule` | `gtfs:CalendarRule` | `gtfs:CalendarRule(SERVICE_ID)` | N/A | `xsd:boolean` | N/A | N/A |
| `wednesday` | `gtfs:wednesday` | `gtfs:CalendarRule` | `gtfs:CalendarRule` | `gtfs:CalendarRule(SERVICE_ID)` | N/A | `xsd:boolean` | N/A | N/A |
| `thursday` | `gtfs:thursday` | `gtfs:CalendarRule` | `gtfs:CalendarRule` | `gtfs:CalendarRule(SERVICE_ID)` | N/A | `xsd:boolean` | N/A | N/A |
| `friday` | `gtfs:friday` | `gtfs:CalendarRule` | `gtfs:CalendarRule` | `gtfs:CalendarRule(SERVICE_ID)` | N/A | `xsd:boolean` | N/A | N/A |
| `saturday` | `gtfs:saturday` | `gtfs:CalendarRule` | `gtfs:CalendarRule` | `gtfs:CalendarRule(SERVICE_ID)` | N/A | `xsd:boolean` | N/A | N/A |
| `sunday` | `gtfs:sunday` | `gtfs:CalendarRule` | `gtfs:CalendarRule` | `gtfs:CalendarRule(SERVICE_ID)` | N/A | `xsd:boolean` | N/A | N/A |
| `start_date` | `gtfs:startDate` | `gtfs:Service` | `gtfs:CalendarRule` | `gtfs:ServiceRule(gtfs:Service(SERVICE_ID))` | `service_id` | `xsd:date` | N/A | N/A |
| `end_date` | `gtfs:endDate` | `gtfs:Service` | `gtfs:CalendarRule` | `gtfs:ServiceRule(gtfs:Service(SERVICE_ID))` | `service_id` | `xsd:date` | N/A | N/A |
| `date` | `gtfs:date` | `gtfs:CalendarDateRule` | `gtfs:CalendarDateRule` | `gtfs:CalendarDateRule(SERVICE_ID, DATE)` | `service_id` | `xsd:date` | N/A | N/A |
| `exception_type` | `gtfs:exceptionType` | `gtfs:CalendarDateRule` | `gtfs:CalendarDateRule` | `gtfs:CalendarDateRule(SERVICE_ID, DATE)` | `service_id and date` | `xsd:string` | N/A | N/A |
