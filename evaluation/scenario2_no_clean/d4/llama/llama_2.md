| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `service_id` | `gtfs:id` | `gtfs:Service` | - | `http://vocab.gtfs.org/terms#Service/{service_id}` | - | `xsd:string` | - | - |
| `monday` | `gtfs:monday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `skos:Concept` | `mapDayAvailability` | `http://transport.linkeddata.es/kos/day/available` or `.../not-available` |
| `tuesday` | `gtfs:tuesday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `skos:Concept` | `mapDayAvailability` | same as above |
| `wednesday` | `gtfs:wednesday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `skos:Concept` | `mapDayAvailability` | same as above |
| `thursday` | `gtfs:thursday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `skos:Concept` | `mapDayAvailability` | same as above |
| `friday` | `gtfs:friday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `skos:Concept` | `mapDayAvailability` | same as above |
| `saturday` | `gtfs:saturday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `skos:Concept` | `mapDayAvailability` | same as above |
| `sunday` | `gtfs:sunday` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `skos:Concept` | `mapDayAvailability` | same as above |
| `start_date` | `gtfs:startDate` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `schema:startDate` | - | `{start_date}` |
| `end_date` | `gtfs:endDate` | `gtfs:CalendarRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarRule/{service_id}` | `service_id` | `schema:endDate` | - | `{end_date}` |
| `date` | `gtfs:date` | `gtfs:CalendarDateRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarDateRule/{service_id}/{date}` | `service_id` and `date` | `xsd:date` | - | `{date}` |
| `exception_type` | `gtfs:exceptionType` | `gtfs:CalendarDateRule` | `gtfs:Service` | `http://vocab.gtfs.org/terms#CalendarDateRule/{service_id}/{date}` | `service_id` and `date` | `skos:Concept` | `mapExceptionType` | `http://transport.linkeddata.es/kos/exception-type/added` or `.../removed` |
