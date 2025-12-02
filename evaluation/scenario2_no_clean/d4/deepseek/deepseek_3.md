| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| service_id (calendar) | gtfs:id | gtfs:Service | - | http://example.org/service/{service_id} | - | xsd:string | - | - |
| monday | gtfs:monday | gtfs:CalendarRule | skos:Concept (day scheme) | http://example.org/calendar_rule/{service_id} | service_id | - | - | map_day_availability 1 → <http://transport.linkeddata.es/kos/day/available>, 0 → .../not-available |
| tuesday | gtfs:tuesday | gtfs:CalendarRule | skos:Concept (day scheme) | Same as above | service_id | - | - | map_day_availability Same as above |
| wednesday | gtfs:wednesday | gtfs:CalendarRule | skos:Concept (day scheme) | Same as above | service_id | - | - | map_day_availability Same as above |
| thursday | gtfs:thursday | gtfs:CalendarRule | skos:Concept (day scheme) | Same as above | service_id | - | - | map_day_availability Same as above |
| friday | gtfs:friday | gtfs:CalendarRule | skos:Concept (day scheme) | Same as above | service_id | - | - | map_day_availability Same as above |
| saturday | gtfs:saturday | gtfs:CalendarRule | skos:Concept (day scheme) | Same as above | service_id | - | - | map_day_availability Same as above |
| sunday | gtfs:sunday | gtfs:CalendarRule | skos:Concept (day scheme) | Same as above | service_id | - | - | map_day_availability Same as above |
| start_date | gtfs:startDate | gtfs:CalendarRule | - | Same as above | service_id | xsd:date | - | - |
| end_date | gtfs:endDate | gtfs:CalendarRule | - | Same as above | service_id | xsd:date | - | - |
| service_id (dates) | gtfs:serviceRule | gtfs:Service | gtfs:CalendarDateRule | http://example.org/service/{service_id} | service_id | - | - | - |
| date | gtfs:date | gtfs:CalendarDateRule | - | http://example.org/date_rule/{service_id}/{date} | service_id | xsd:date | - | - |
| exception_type | gtfs:exceptionType | gtfs:CalendarDateRule | skos:Concept (exception-type scheme) | Same as above | service_id | - | - | map_exception_type 1 → <http://transport.linkeddata.es/kos/exception-type/added>, 2 → .../removed |
