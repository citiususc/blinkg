| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `trip_id` | `gtfs:id` | `gtfs:Trip` | N/A | `http://transport.linkeddata.es/trip/{trip_id}` | N/A | `xsd:string` | N/A | `http://transport.linkeddata.es/trip/4_I12-001_2016I12_1_1_4___` |
| `start_time` | `gtfs:startTime` | `gtfs:Frequency` | N/A | N/A | N/A | `xsd:time` | `convert_to_time_format("HH:MM:SS")` | `00:00:00` |
| `end_time` | `gtfs:endTime` | `gtfs:Frequency` | N/A | N/A | N/A | `xsd:time` | `convert_to_time_format("HH:MM:SS")` | `01:00:00` |
| `headway_secs` | `gtfs:headwaySeconds` | `gtfs:Frequency` | N/A | N/A | N/A | `xsd:int` | N/A | `600` |
| `exact_times` | `gtfs:usesExactTimes` | `gtfs:Frequency` | `gtfs:Service` | N/A | N/A | `xsd:boolean` | `map_exact_times_to_boolean` | `true` (if "Frequency") |
| `route_id` | `gtfs:route` | `gtfs:Trip` | `gtfs:Route` | N/A | N/A | `xsd:string` | N/A | `"4__1___"` |
| `service_id` | `gtfs:service` | `gtfs:Trip` | `gtfs:Service` | N/A | N/A | `xsd:string` | N/A | `"4_I12"` |
| `trip_headsign` | `gtfs:headsign` | `gtfs:Trip` | N/A | N/A | N/A | `xsd:string` | N/A | `"VALDECARROS"` |
| `trip_short_name` | `gtfs:shortName` | `gtfs:Route` | `gtfs:Trip` | `http://transport.linkeddata.es/route/{route_id}` | N/A | `xsd:string` | N/A | `"4__1___"` |
| `direction_id` | `gtfs:direction` | `gtfs:Trip` | N/A | SKOS mapping | N/A | `skos:Concept` | `map_direction("0")` | `"Opposite Direction"` |
| `shape_id` | `gtfs:shape` | `gtfs:Trip` | `gtfs:Shape` | `http://transport.linkeddata.es/shape/{shape_id}` | N/A | `xsd:string` | N/A | `"4__1____2__IT_1"` |
| `wheelchair_accessible` | `gtfs:wheelchairAccessible` | `gtfs:Trip` | N/A | SKOS mapping | N/A | `skos:Concept` | `map_accessibility("1")` | `"Accesible"` |
| `agency_id` | `gtfs:agency` | `gtfs:Route` | N/A | N/A | N/A | `xsd:string` | N/A | `"CRTM"` |
| `route_short_name` | `gtfs:shortName` | `gtfs:Route` | N/A | N/A | N/A | `xsd:string` | N/A | `"1"` |
| `route_desc` | `rdfs:comment` | `gtfs:Route` | N/A | N/A | N/A | `xsd:string` | N/A | `""` (empty description) |
| `shape_dist_traveled` | N/A | `gtfs:ShapePoint` | N/A | N/A | N/A | `xsd:float` | N/A | `0.047428346568` |
| `origin_lat` | N/A | `gtfs:Location` | N/A | N/A | N/A | `xsd:float` | N/A | `40.4802624278576` |
| `origin_lon` | N/A | `gtfs:Location` | N/A | N/A | N/A | `xsd:float` | N/A | `-3.66723744236574` |
| `origin_name` | N/A | `gtfs:Location` | N/A | N/A | N/A | `xsd:string` | N/A | `"Av de Pilar"` |
| `origin_type` | N/A | `gtfs:Location` | N/A | N/A | N/A | `xsd:string` | N/A | `"S"` |
