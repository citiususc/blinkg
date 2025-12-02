| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `stop_id` | `gtfs:id` | `gtfs:Location` | – | `ex:location/{stop_id}` | – | `xsd:string` | – | – |
| `stop_code` | `gtfs:code` | `gtfs:Location` | – | `ex:location/{stop_id}` | – | `xsd:string` | – | – |
| `stop_name` | `gtfs:name` | `gtfs:Location` | – | `ex:location/{stop_id}` | – | `xsd:string` | `lang:es` | – |
| `stop_desc` | `gtfs:desc` | `gtfs:Location` | – | `ex:location/{stop_id}` | – | `xsd:string` | `lang:es` | – |
| `stop_lat` | `gtfs:latitude` | `gtfs:Location` | – | `ex:location/{stop_id}` | – | `geo:lat` | – | – |
| `stop_lon` | `gtfs:longitude` | `gtfs:Location` | – | `ex:location/{stop_id}` | – | `geo:long` | – | – |
| `stop_url` | `gtfs:url` | `gtfs:Location` | – | `ex:location/{stop_id}` | – | `foaf:page` | – | – |
| `stop_timezone` | `gtfs:timezone` | `gtfs:Location` | – | `ex:location/{stop_id}` | – | `xsd:string` | – | – |
| `wheelchair_boarding` | `gtfs:wheelchairAccessible` | `gtfs:Location` | – | `ex:location/{stop_id}` | – | `skos:Concept` | – | `map_wheelchair_accessibility` `{ 0: "no-information", 1: "accesible", 2: "inaccesible" }` ↦ SKOS URIs |
| `location_type` | `gtfs:locationType` | `gtfs:Location` | – | `ex:location/{stop_id}` | – | `skos:Concept` | – | `map_location_type` `{ 0: "stop", 1: "station", 2: "entrance-exit", 3: "generic-node", 4: "boarding-area" }` ↦ SKOS URIs |
| `parent_station` | `gtfs:parentStation` | `gtfs:Location` | `gtfs:Station` | `ex:location/{stop_id}` | `location_type in [0,2,3,4] and parent_station != ""` | `xsd:string` | – | – |
