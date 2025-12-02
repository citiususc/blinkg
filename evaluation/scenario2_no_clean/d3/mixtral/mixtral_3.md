| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `stop_id` | `gtfs:id` | `gtfs:Stop` | - | `URI: <http://vocab.gtfs.org/Stop/><stop_id>` | - | - | - | - |
| `stop_code` | `gtfs:code` | `gtfs:Stop` | - | `URI: <http://vocab.gtfs.org/Stop/><stop_id>` | - | - | - | - |
| `stop_name` | `gtfs:name` | `gtfs:Stop` | - | `URI: <http://vocab.gtfs.org/Stop/><stop_id>` | - | - | - | - |
| `stop_desc` | `gtfs:desc` | `gtfs:Stop` | - | `URI: <http://vocab.gtfs.org/Stop/><stop_id>` | - | - | - | - |
| `stop_lat` | `gtfs:latitude` | `gtfs:Stop` | - | `URI: <http://vocab.gtfs.org/Stop/><stop_id>` | - | - | - | - |
| `stop_lon` | `gtfs:longitude` | `gtfs:Stop` | - | `URI: <http://vocab.gtfs.org/Stop/><stop_id>` | - | - | - | - |
| `zone_id` | `gtfs:zone_id` | `gtfs:Stop` | - | `URI: <http://vocab.gtfs.org/Stop/><stop_id>` | - | - | - | - |
| `stop_url` | `gtfs:url` | `gtfs:Stop` | - | `URI: <http://vocab.gtfs.org/Stop/><stop_id>` | - | - | - | - |
| `location_type` | `gtfs:locationType` | `gtfs:Location` | - | `URI: <http://vocab.gtfs.org/Location/><location_type>` (SKOS) | - | - | `skos_mapping()` | `URI: <http://transport.linkeddata.es/kos/location-type/<location_type>>` |
| `parent_station` | `gtfs:parentStation` | `gtfs:Stop` | `gtfs:Station` | `URI: <http://vocab.gtfs.org/Stop/><stop_id>` | Join: value equals `gtfs:id` of `gtfs:Station` | - | - | - |
| `stop_timezone` | `gtfs:timezone` | `gtfs:Stop` | - | `URI: <http://vocab.gtfs.org/Stop/><stop_id>` | - | - | - | - |
| `wheelchair_boarding` | `gtfs:wheelchairAccessible` | `gtfs:Stop` | - | `URI: <http://vocab.gtfs.org/Stop/><stop_id>` | - | - | `accessibility_mapping()` | `URI: <http://transport.linkeddata.es/kos/wheelchair-accesible/<accessibility>>` |
