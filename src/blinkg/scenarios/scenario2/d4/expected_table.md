| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    |Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| calendar.csv service_id | gtfs:id | gtfs:Service | - | `http://example.org/service/{service_id}` | - | xsd:string | - | - |
| calendar.csv monday | gtfs:monday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | - | - | mapDayAvailability 1 → `<http://transport.linkeddata.es/kos/day/available>`<br>0 → `<http://transport.linkeddata.es/kos/day/not-available>` |
| calendar.csv tuesday | gtfs:tuesday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | - | - | mapDayAvailability Same as above |
| calendar.csv wednesday | gtfs:wednesday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | - | - | mapDayAvailability Same as above |
| calendar.csv thursday | gtfs:thursday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | - | - | mapDayAvailability Same as above |
| calendar.csv friday | gtfs:friday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | - | - | mapDayAvailability Same as above |
| calendar.csv saturday | gtfs:saturday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | - | - | mapDayAvailability Same as above |
| calendar.csv sunday | gtfs:sunday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | - | - | mapDayAvailability Same as above |
| calendar.csv start_date | gtfs:startDate | gtfs:CalendarRule | - | `http://example.org/rule/{service_id}` | - | schema:startDate | - | - |
| calendar.csv end_date | gtfs:endDate | gtfs:CalendarRule | - | `http://example.org/rule/{service_id}` | - | schema:endDate | - | - |
| calendar_dates.csv date | gtfs:date | gtfs:CalendarDateRule | - | `http://example.org/rule/{service_id}_{date}` | - | xsd:date | - | - |
| calendar_dates.csv exception_type | gtfs:exceptionType | gtfs:CalendarDateRule | skos:Concept | `http://example.org/rule/{service_id}_{date}` | - | - | - | mapExceptionType 1 → `<http://transport.linkeddata.es/kos/exception-type/removed>`<br>2 → `<http://transport.linkeddata.es/kos/exception-type/added>` |
