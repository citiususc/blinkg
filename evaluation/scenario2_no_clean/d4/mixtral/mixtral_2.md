| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `service_id` | `gtfs:id` | `gtfs:Service` | - | Generate a URI using: `http://gtfs.org/services/{service_id}` | Join with `gtfs:id` of `gtfs:Service` | String | `URI Construction` | `http://gtfs.org/services/{service_id}` |
| `monday` | `gtfs:monday` | `gtfs:CalendarRule` | `gtfs:Day` | Use `http://transport.linkeddata.es/kos/day/available` as subject if value is true | Join with URI of day concept | Boolean | `Boolean to URI` | If true, return URI; otherwise, return `null` |
| `tuesday` | `gtfs:tuesday` | `gtfs:CalendarRule` | `gtfs:Day` | Same as above | Same as above | Boolean | `Boolean to URI` | Same as above |
| `wednesday` | `gtfs:wednesday` | `gtfs:CalendarRule` | `gtfs:Day` | Same as above | Same as above | Boolean | `Boolean to URI` | Same as above |
| `thursday` | `gtfs:thursday` | `gtfs:CalendarRule` | `gtfs:Day` | Same as above | Same as above | Boolean | `Boolean to URI` | Same as above |
| `friday` | `gtfs:friday` | `gtfs:CalendarRule` | `gtfs:Day` | Same as above | Same as above | Boolean | `Boolean to URI` | Same as above |
| `saturday` | `gtfs:saturday` | `gtfs:CalendarRule` | `gtfs:Day` | Same as above | Same as above | Boolean | `Boolean to URI` | Same as above |
| `sunday` | `gtfs:sunday` | `gtfs:CalendarRule` | `gtfs:Day` | Same as above | Same as above | Boolean | `Boolean to URI` | Same as above |
| `start_date` | `gtfs:startDate` | `gtfs:Service` | - | Generate URI: `http://gtfs.org/services/{service_id}` | Join with `gtfs:id` of `gtfs:Service` | Date | `Date Formatting` | Format `start_date` as `yyyy-MM-dd` |
| `end_date` | `gtfs:endDate` | `gtfs:Service` | - | Generate URI: `http://gtfs.org/services/{service_id}` | Join with `gtfs:id` of `gtfs:Service` | Date | `Date Formatting` | Format `end_date` as `yyyy-MM-dd` |
| `service_id` | `gtfs:id` | `gtfs:CalendarDateRule` | - | Generate URI: `http://gtfs.org/calendar-dates/{service_id}` | Join with `gtfs:id` of `CalendarDateRule` | String | `URI Construction` | `http://gtfs.org/calendar-dates/{service_id}` |
| `date` | `gtfs:date` | `gtfs:CalendarDateRule` | - | Convert to xsd:date | Join with `gtfs:date` in ontology | Date | `Date Conversion` | Convert to `yyyy-MM-dd` |
| `exception_type` | `gtfs:exceptionType` | `gtfs:CalendarDateRule` | `gtfs:ExceptionType` | Return URI depending on value (1 = removed, 2 = added) | Join with URI representing `exception_type` | Integer | `Enum to URI` | Added: `.../added`, Removed: `.../removed` |
