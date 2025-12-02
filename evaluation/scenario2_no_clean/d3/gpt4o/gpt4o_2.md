| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| stop_id | gtfs:id | gtfs:Location |  | `:Location/{stop_id}` |  | xsd:string |  |  |
| stop_code | gtfs:code | gtfs:Location |  |  |  | xsd:string |  |  |
| stop_name | gtfs:name | gtfs:Location |  |  |  | foaf:name | `@es`, `@en` |  |
| stop_desc | gtfs:desc | gtfs:Location |  |  |  | xsd:string | `@es`, `@en` |  |
| stop_lat | gtfs:latitude | gtfs:Location |  |  |  | geo:lat |  |  |
| stop_lon | gtfs:longitude | gtfs:Location |  |  |  | geo:long |  |  |
| zone_id | gtfs:id (zone concept) |  | gtfs:Zone | `:Zone/{zone_id}` | `stops.zone_id = zones.zone_id` | xsd:string |  |  |
| stop_url | gtfs:url | gtfs:Location |  |  |  | foaf:page |  |  |
| location_type | gtfs:locationType | gtfs:Location | skos:Concept |  |  | skos:Concept |  | `map_location_type()` `0=stop`, `1=station`, `2=entrance-exit`, `3=generic-node`, `4=boarding-area` → URIs from location-type SKOS |
| parent_station | gtfs:parentStation | gtfs:Location | gtfs:Station |  | `stops.parent_station = stations.stop_id` | URI |  |  |
| stop_timezone | gtfs:timezone | gtfs:Location |  |  |  | xsd:string |  |  |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Location | skos:Concept |  |  | skos:Concept |  | `map_wheelchair_accessible()` `0=no-information`, `1=accessible`, `2=inaccessible` → URIs from wheelchair-accessible SKOS |
