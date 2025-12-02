| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| stop_id | `gtfs:id` | `gtfs:Stop`, `gtfs:Station`, or `gtfs:StationEntrance` (determined by `location_type`) | - | `http://transport.linkeddata.es/resource/Location/{stop_id}` | - | `xsd:string` | - | - |
| stop_code | `gtfs:code` | `gtfs:Location` | - | `http://transport.linkeddata.es/resource/Location/{stop_id}` | Where `stop_code` is not empty. | `xsd:string` | - | - |
| stop_name | `gtfs:name` | `gtfs:Location` | - | `http://transport.linkeddata.es/resource/Location/{stop_id}` | - | `foaf:name` | - | - |
| stop_desc | `gtfs:desc` | `gtfs:Location` | - | `http://transport.linkeddata.es/resource/Location/{stop_id}` | Where `stop_desc` is not empty. | `xsd:string` | - | - |
| stop_lat | `gtfs:latitude` | `gtfs:Location` | - | `http://transport.linkeddata.es/resource/Location/{stop_id}` | - | `geo:lat` | - | - |
| stop_lon | `gtfs:longitude` | `gtfs:Location` | - | `http://transport.linkeddata.es/resource/Location/{stop_id}` | - | `geo:long` | - | - |
| stop_url | `gtfs:url` | `gtfs:Location` | - | `http://transport.linkeddata.es/resource/Location/{stop_id}` | - | `foaf:page` | - | - |
| location_type | `rdf:type` | - | `gtfs:Stop`, `gtfs:Station`, or `gtfs:StationEntrance` | `http://transport.linkeddata.es/resource/Location/{stop_id}` | - | - | | |
| location_type | `gtfs:locationType` | `gtfs:Location` | `skos:Concept` | `http://transport.linkeddata.es/resource/Location/{stop_id}` | - | - | `map_location_type` | `http://transport.linkeddata.es/kos/location-type/{value}` where value is `stop`, `station`, or `entrance-exit` |
| parent_station | `gtfs:parentStation` | `gtfs:Stop`, `gtfs:StationEntrance` | `gtfs:Station` | `http://transport.linkeddata.es/resource/Location/{stop_id}` | Where `parent_station` is not empty. | - | - | - |
| stop_timezone | `gtfs:timezone` | `gtfs:Location` | - | `http://transport.linkeddata.es/resource/Location/{stop_id}` | Where `stop_timezone` is not empty. | `xsd:string` | - | - |
| wheelchair_boarding | `gtfs:wheelchairAccessible` | `gtfs:Stop`, `gtfs:Station`, `gtfs:StationEntrance` | `skos:Concept` | `http://transport.linkeddata.es/resource/Location/{stop_id}` | - | - | `map_wheelchair_boarding` | `http://transport.linkeddata.es/kos/wheelchair-accesible/{value}` where value is `no-information`, `accesible`, or `inaccesible` |
