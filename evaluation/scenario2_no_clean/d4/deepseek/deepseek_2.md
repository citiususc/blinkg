| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| service_id (calendar) | gtfs:id | gtfs:Service | - | http://example.org/service/{service_id} | - | xsd:string | en | - |
| monday | gtfs:monday | gtfs:CalendarRule | gtfs:Service | http://example.org/calendar/{service_id} | service_id match | URI | en | map_day_availability <http://transport.../day/available> if 1, <http://transport.../day/not-available> if 0 |
| tuesday | gtfs:tuesday | gtfs:CalendarRule | gtfs:Service | Same as above | Same as above | URI | en | map_day_availability Same as above |
| wednesday | gtfs:wednesday | gtfs:CalendarRule | gtfs:Service | Same as above | Same as above | URI | en | map_day_availability Same as above |
| thursday | gtfs:thursday | gtfs:CalendarRule | gtfs:Service | Same as above | Same as above | URI | en | map_day_availability Same as above |
| friday | gtfs:friday | gtfs:CalendarRule | gtfs:Service | Same as above | Same as above | URI | en | map_day_availability Same as above |
| saturday | gtfs:saturday | gtfs:CalendarRule | gtfs:Service | Same as above | Same as above | URI | en | map_day_availability Same as above |
| sunday | gtfs:sunday | gtfs:CalendarRule | gtfs:Service | Same as above | Same as above | URI | en | map_day_availability Same as above |
| start_date | gtfs:startDate | gtfs:CalendarRule | - | Same as above | - | xsd:date | en | - |
| end_date | gtfs:endDate | gtfs:CalendarRule | - | Same as above | - | xsd:date | en | - |
| service_id (dates) | gtfs:id | gtfs:Service | - | http://example.org/service/{service_id} | service_id match | xsd:string | en | - |
| date | gtfs:date | gtfs:CalendarDateRule | gtfs:Service | http://example.org/date_rule/{service_id}-{date} | service_id match | xsd:date | en | - |
| exception_type | gtfs:exceptionType | gtfs:CalendarDateRule | gtfs:Service | Same as above | Same as above | URI | en | map_exception_type <http://transport.../exception-type/added> if 1, <http://transport.../exception-type/removed> if 2 |
