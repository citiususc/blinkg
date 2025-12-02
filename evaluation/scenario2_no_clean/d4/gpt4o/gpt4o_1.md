| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| service_id | gtfs:id | gtfs:Service |  | `ex:service/{service_id}` | calendar.service_id = calendar_dates.service_id | xsd:string |  |  Direct copy of service_id |
| monday | gtfs:monday | gtfs:CalendarRule | skos:Concept | `ex:calendarRule/{service_id}` |  | xsd:string | skos:inScheme=<http://transport.linkeddata.es/kos/day> | mapAvailability "0" → "http://transport.linkeddata.es/kos/day/not-available", "1" → "http://transport.linkeddata.es/kos/day/available" |
| tuesday | gtfs:tuesday | gtfs:CalendarRule | skos:Concept | Same as above |  | xsd:string | skos:inScheme=<http://transport.linkeddata.es/kos/day> | mapAvailability Same as above |
| wednesday | gtfs:wednesday | gtfs:CalendarRule | skos:Concept | Same as above |  | xsd:string | skos:inScheme=<http://transport.linkeddata.es/kos/day> | mapAvailability Same as above |
| thursday | gtfs:thursday | gtfs:CalendarRule | skos:Concept | Same as above |  | xsd:string | skos:inScheme=<http://transport.linkeddata.es/kos/day> | mapAvailability Same as above |
| friday | gtfs:friday | gtfs:CalendarRule | skos:Concept | Same as above |  | xsd:string | skos:inScheme=<http://transport.linkeddata.es/kos/day> | mapAvailability Same as above |
| saturday | gtfs:saturday | gtfs:CalendarRule | skos:Concept | Same as above |  | xsd:string | skos:inScheme=<http://transport.linkeddata.es/kos/day> | mapAvailability Same as above |
| sunday | gtfs:sunday | gtfs:CalendarRule | skos:Concept | Same as above |  | xsd:string | skos:inScheme=<http://transport.linkeddata.es/kos/day> | mapAvailability Same as above |
| start_date | gtfs:startDate | gtfs:CalendarRule |  | Same as above |  | xsd:date |  | formatDate Outputs in ISO date format (YYYY-MM-DD) |
| end_date | gtfs:endDate | gtfs:CalendarRule |  | Same as above |  | xsd:date |  | formatDate Outputs in ISO date format (YYYY-MM-DD) |
| service_id | gtfs:id | gtfs:Service |  | `ex:service/{service_id}` | calendar.service_id = calendar_dates.service_id | xsd:string |  |  Direct copy |
| date | gtfs:date | gtfs:CalendarDateRule |  | `ex:calendarDateRule/{service_id}/{date}` | calendar.service_id = calendar_dates.service_id | xsd:date |  | formatDate Outputs in ISO date format (YYYY-MM-DD) |
| exception_type | gtfs:exceptionType | gtfs:CalendarDateRule | skos:Concept | Same as above |  | xsd:string | skos:inScheme=<http://transport.linkeddata.es/kos/exception-type> | mapExceptionType "1" → "http://transport.linkeddata.es/kos/exception-type/added", "2" → "http://transport.linkeddata.es/kos/exception-type/removed" |
