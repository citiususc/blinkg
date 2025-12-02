| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `service_id` | `gtfs:id` | `gtfs:Service` | - | Service ID from CSV file | - | `xsd:string` | - | - |
| `monday` | `gtfs:monday` | `gtfs:CalendarRule` | `gtfs:Service` | `ServiceID + '/' + Day` | `gtfs:serviceRule` | `owl:ObjectProperty` | `get_day_value` | `1` (available) / `0` (not available) |
| `tuesday` | `gtfs:tuesday` | `gtfs:CalendarRule` | `gtfs:Service` | `ServiceID + '/' + Day` | `gtfs:serviceRule` | `owl:ObjectProperty` | `get_day_value` | Same as above |
| `wednesday` | `gtfs:wednesday` | `gtfs:CalendarRule` | `gtfs:Service` | `ServiceID + '/' + Day` | `gtfs:serviceRule` | `owl:ObjectProperty` | `get_day_value` | Same as above |
| `thursday` | `gtfs:thursday` | `gtfs:CalendarRule` | `gtfs:Service` | `ServiceID + '/' + Day` | `gtfs:serviceRule` | `owl:ObjectProperty` | `get_day_value` | Same as above |
| `friday` | `gtfs:friday` | `gtfs:CalendarRule` | `gtfs:Service` | `ServiceID + '/' + Day` | `gtfs:serviceRule` | `owl:ObjectProperty` | `get_day_value` | Same as above |
| `saturday` | `gtfs:saturday` | `gtfs:CalendarRule` | `gtfs:Service` | `ServiceID + '/' + Day` | `gtfs:serviceRule` | `owl:ObjectProperty` | `get_day_value` | Same as above |
| `sunday` | `gtfs:sunday` | `gtfs:CalendarRule` | `gtfs:Service` | `ServiceID + '/' + Day` | `gtfs:serviceRule` | `owl:ObjectProperty` | `get_day_value` | Same as above |
| `start_date` | `gtfs:startDate` | `gtfs:CalendarRule` | - | `ServiceID + '/' + Date property` | - | `schema:startDate` | `convert_date_format` | `yyyy-mm-dd` formatted date as `xsd:date` |
| `end_date` | `gtfs:endDate` | `gtfs:CalendarRule` | - | `ServiceID + '/' + Date property` | - | `schema:endDate` | `convert_date_format` | `yyyy-mm-dd` formatted date as `xsd:date` |

| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `service_id` | `gtfs:id` | `gtfs:Service` | - | Service ID from CSV file | - | `xsd:string` | - | - |
| `date` | `gtfs:date` | `gtfs:CalendarDateRule` | `gtfs:Service` | `ServiceID + '/' + Date` | `gtfs:service` | `rdf:ObjectProperty` | `convert_date_format` | Date in `yyyy-mm-dd` format as `xsd:date` |
| `exception_type` | `gtfs:exceptionType` | *(inferred class)* | - | `ServiceID + '/' + Exception Type` | `gtfs:date` | `owl:ObjectProperty` | `get_exception_type` | `Added` or `Removed` SKOS URI from `skos.ttl` |
