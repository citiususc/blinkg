| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `service_id` | `gtfs:id` | `gtfs:Service` | - | `http://vocab.gtfs.org/terms#Service/{service_id}` | - | `xsd:string` | - | `http://vocab.gtfs.org/terms#Service/{service_id}` |
| `monday` | `gtfs:monday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `xsd:boolean` | `mapDayAvailability` | Available/Not-available SKOS URI |
| `tuesday` | `gtfs:tuesday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `xsd:boolean` | `mapDayAvailability` | Available/Not-available SKOS URI |
| `wednesday` | `gtfs:wednesday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `xsd:boolean` | `mapDayAvailability` | Available/Not-available SKOS URI |
| `thursday` | `gtfs:thursday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `xsd:boolean` | `mapDayAvailability` | Available/Not-available SKOS URI |
| `friday` | `gtfs:friday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `xsd:boolean` | `mapDayAvailability` | Available/Not-available SKOS URI |
| `saturday` | `gtfs:saturday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `xsd:boolean` | `mapDayAvailability` | Available/Not-available SKOS URI |
| `sunday` | `gtfs:sunday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `xsd:boolean` | `mapDayAvailability` | Available/Not-available SKOS URI |
| `start_date` | `gtfs:startDate` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `xsd:date` | - | `{start_date}` |
| `end_date` | `gtfs:endDate` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `xsd:date` | - | `{end_date}` |
| `date` | `gtfs:date` | `gtfs:CalendarDateRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarDateRule/{service_id}/{date}` | `service_id` and `date` | `xsd:date` | - | `{date}` |
| `exception_type` | `gtfs:exceptionType` | `gtfs:CalendarDateRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarDateRule/{service_id}/{date}` | `service_id` and `date` | `xsd:integer` | `mapExceptionType` | Added/Removed SKOS URI |
