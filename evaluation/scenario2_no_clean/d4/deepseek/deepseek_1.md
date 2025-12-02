| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| service_id | gtfs:id | gtfs:Service | - | `http://example.org/service/{service_id}` | Primary key | xsd:string | - | - |
| monday | gtfs:monday | gtfs:CalendarRule | skos:Concept (from day scheme) | `http://example.org/rule/{service_id}/calendar` | service_id → Service | URI | - | mapDayAvailability 1 → `<http://transport.linkeddata.es/kos/day/available>`<br>0 → `<http://transport.linkeddata.es/kos/day/not-available>` |
| tuesday | gtfs:tuesday | gtfs:CalendarRule | skos:Concept (from day scheme) | Same as CalendarRule subject | Same as CalendarRule | URI | - | mapDayAvailability Same as above |
| wednesday | gtfs:wednesday | gtfs:CalendarRule | skos:Concept (from day scheme) | Same as CalendarRule subject | Same as CalendarRule | URI | - | mapDayAvailability Same as above |
| thursday | gtfs:thursday | gtfs:CalendarRule | skos:Concept (from day scheme) | Same as CalendarRule subject | Same as CalendarRule | URI | - | mapDayAvailability Same as above |
| friday | gtfs:friday | gtfs:CalendarRule | skos:Concept (from day scheme) | Same as CalendarRule subject | Same as CalendarRule | URI | - | mapDayAvailability Same as above |
| saturday | gtfs:saturday | gtfs:CalendarRule | skos:Concept (from day scheme) | Same as CalendarRule subject | Same as CalendarRule | URI | - | mapDayAvailability Same as above |
| sunday | gtfs:sunday | gtfs:CalendarRule | skos:Concept (from day scheme) | Same as CalendarRule subject | Same as CalendarRule | URI | - | mapDayAvailability Same as above |
| start_date | gtfs:startDate | gtfs:CalendarRule | - | Same as CalendarRule subject | Same as CalendarRule | xsd:date | - | - |
| end_date | gtfs:endDate | gtfs:CalendarRule | - | Same as CalendarRule subject | Same as CalendarRule | xsd:date | - | - |
| date (calendar_dates) | gtfs:date | gtfs:CalendarDateRule | - | `http://example.org/rule/{service_id}/date/{date}` | service_id → Service | xsd:date | - | - |
| exception_type | gtfs:exceptionType | gtfs:CalendarDateRule | skos:Concept (from exception-type scheme) | Same as CalendarDateRule subject | service_id → Service | URI | - | mapExceptionType 1 → `<http://transport.linkeddata.es/kos/exception-type/removed>`<br>2 → `<http://transport.linkeddata.es/kos/exception-type/added>` |
