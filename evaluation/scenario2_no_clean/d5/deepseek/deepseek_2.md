| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **trips.csv** |  |  |  |  |  |  |  |  |
| trip_id | gtfs:id | gtfs:Trip | - | `<http://example.org/trip/{trip_id}>` | - | xsd:string | - | - |
| route_id | gtfs:route | gtfs:Trip | gtfs:Route | - | route_id = routes.route_id | owl:ObjectProperty | - | - `<http://example.org/route/{route_id}>` |
| service_id | gtfs:service | gtfs:Trip | gtfs:Service | - | service_id = calendar.service_id | owl:ObjectProperty | - | - `<http://example.org/service/{service_id}>` |
| trip_headsign | gtfs:headsign | gtfs:Trip | - | - | - | xsd:string (pattern) | en/es | - |
| direction_id | gtfs:direction | gtfs:Trip | skos:Concept | - | - | owl:ObjectProperty | en | map_direction `0`→`<http://transport.linkeddata.es/kos/direction/one-direction>`, `1`→opposite |
| wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | - | - | owl:ObjectProperty | en | map_wheelchair `0`→no-information, `1`→accesible, `2`→inaccesible |
| trip_short_name | gtfs:shortName | gtfs:Trip | - | - | - | xsd:string (pattern) | en/es | format_short_name PascalCase string (e.g., "Valdecarros" → "Valdecarros") |
| **frequencies.csv** |  |  |  |  |  |  |  |  |
| trip_id | gtfs:trip | gtfs:Frequency | gtfs:Trip | `<http://example.org/frequency/{trip_id}_{start_time}>` | trip_id = trips.trip_id | owl:ObjectProperty | - | - `<http://example.org/trip/{trip_id}>` |
| start_time | gtfs:startTime | gtfs:Frequency | - | - | - | schema:startTime | - | time_to_xsd xsd:time (e.g., "00:00:00" → `"00:00:00"^^xsd:time`) |
| end_time | gtfs:endTime | gtfs:Frequency | - | - | - | schema:endTime | - | time_to_xsd xsd:time (e.g., "01:00:00" → `"01:00:00"^^xsd:time`) |
| headway_secs | gtfs:headwaySeconds | gtfs:Frequency | - | - | - | xsd:positiveInteger | - | - |
| exact_times | gtfs:usesExactTimes | gtfs:Frequency | skos:Concept | - | - | owl:ObjectProperty | en | map_exact_times Empty→`<http://transport.linkeddata.es/kos/exact-times/frequency>` (default) |
| **routes.csv** |  |  |  |  |  |  |  |  |
| route_id | gtfs:id | gtfs:Route | - | `<http://example.org/route/{route_id}>` | - | xsd:string | - | - |
| route_short_name | gtfs:shortName | gtfs:Route | - | - | - | xsd:string (pattern) | en/es | format_short_name PascalCase string (e.g., "1" → "Line1") |
| **shapes.csv** |  |  |  |  |  |  |  |  |
| shape_id | gtfs:id | gtfs:Shape | - | `<http://example.org/shape/{shape_id}>` | shape_id = trips.shape_id | xsd:string | - | - |
| **calendar.csv** |  |  |  |  |  |  |  |  |
| service_id | gtfs:id | gtfs:Service | - | `<http://example.org/service/{service_id}>` | - | xsd:string | - | - |
