| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| service_id | gtfs:id | gtfs:Service | - | `http://example.org/service/{service_id}` | - | xsd:string | - | - |
| monday | gtfs:monday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | URI | - | mapDayAvailability 1 → `<http://transport.linkeddata.es/kos/day/available>`<br>0 → `<http://transport.linkeddata.es/kos/day/not-available>` |
| tuesday | gtfs:tuesday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | URI | - | mapDayAvailability Same as above |
| wednesday | gtfs:wednesday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | URI | - | mapDayAvailability Same as above |
| thursday | gtfs:thursday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | URI | - | mapDayAvailability Same as above |
| friday | gtfs:friday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | URI | - | mapDayAvailability Same as above |
| saturday | gtfs:saturday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | URI | - | mapDayAvailability Same as above |
| sunday | gtfs:sunday | gtfs:CalendarRule | skos:Concept | `http://example.org/rule/{service_id}` | - | URI | - | mapDayAvailability Same as above |
| start_date | gtfs:startDate | gtfs:CalendarRule | - | `http://example.org/rule/{service_id}` | - | schema:startDate | - | - |
| end_date | gtfs:endDate | gtfs:CalendarRule | - | `http://example.org/rule/{service_id}` | - | schema:endDate | - | - |
| date (calendar_dates) | gtfs:date | gtfs:CalendarDateRule | - | `http://example.org/rule/{service_id}_{date}` | - | xsd:date | - | - |
| exception_type | gtfs:exceptionType | gtfs:CalendarDateRule | skos:Concept | `http://example.org/rule/{service_id}_{date}` | - | URI | - | mapExceptionType 1 → `<http://transport.linkeddata.es/kos/exception-type/removed>`<br>2 → `<http://transport.linkeddata.es/kos/exception-type/added>` |
