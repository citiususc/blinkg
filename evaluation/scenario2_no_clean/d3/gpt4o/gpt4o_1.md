| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| stop_id | gtfs:id | gtfs:Location | — | `ex:stop/{stop_id}` | — | xsd:string | — | — e.g., `ex:stop/acc_4_1_1` |
| stop_code | gtfs:code | gtfs:Location | — | `ex:stop/{stop_id}` | — | xsd:string | — | — "1", "95", ... |
| stop_name | gtfs:name | gtfs:Location | — | `ex:stop/{stop_id}` | — | xsd:string | @es, @en | — "Plaza de Castilla"@es |
| stop_desc | gtfs:desc | gtfs:Location | — | `ex:stop/{stop_id}` | — | xsd:string | @es, @en | — "Paseo de la Castellana 189"@es |
| stop_lat | gtfs:latitude | gtfs:Location | — | `ex:stop/{stop_id}` | — | geo:lat | — | — 40.46682, etc. |
| stop_lon | gtfs:longitude | gtfs:Location | — | `ex:stop/{stop_id}` | — | geo:long | — | — -3.68918, etc. |
| zone_id | gtfs:zoneId | gtfs:Location | — | `ex:stop/{stop_id}` | — | xsd:string | — | — "A" |
| stop_url | gtfs:url | gtfs:Location | — | `ex:stop/{stop_id}` | — | foaf:page | — | — `http://www.crtm.es` |
| location_type | gtfs:locationType | gtfs:Location | — | `ex:stop/{stop_id}` | — | skos:Concept | — | `map_location_type(location_type)` `http://transport.linkeddata.es/kos/location-type/station`, `stop`, etc. |
| parent_station | gtfs:parentStation | gtfs:Location | gtfs:Station | `ex:stop/{stop_id}` | `stop_id = parent_station` | URI | — | `generate_station_uri(id)` `ex:stop/est_90_21`, etc. |
| stop_timezone | gtfs:timezone | gtfs:Location | — | `ex:stop/{stop_id}` | — | xsd:string | — | — "Europe/Madrid" |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Location | skos:Concept | `ex:stop/{stop_id}` | — | skos:Concept | — | `map_wheelchair_accessibility(code)` `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information`, `accesible`, `inaccesible` |
