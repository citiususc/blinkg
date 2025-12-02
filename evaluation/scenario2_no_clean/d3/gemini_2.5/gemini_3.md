| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| stop_id | gtfs:id | gtfs:Location | - | `http://transport.linkeddata.es/madrid/metro/stops/<stop_id>` | - | xsd:string | - | - |
| stop_code | gtfs:code | gtfs:Location | - | `http://transport.linkeddata.es/madrid/metro/stops/<stop_id>` | - | xsd:string | - | - |
| stop_name | gtfs:name | gtfs:Location | - | `http://transport.linkeddata.es/madrid/metro/stops/<stop_id>` | - | foaf:name | - | - |
| stop_desc | gtfs:desc | gtfs:Location | - | `http://transport.linkeddata.es/madrid/metro/stops/<stop_id>` | - | xsd:string | - | - |
| stop_lat | geo:lat | gtfs:Location | - | `http://transport.linkeddata.es/madrid/metro/stops/<stop_id>` | - | geo:lat | - | - |
| stop_lon | geo:long | gtfs:Location | - | `http://transport.linkeddata.es/madrid/metro/stops/<stop_id>` | - | geo:long | - | - |
| stop_url | gtfs:url | gtfs:Location | - | `http://transport.linkeddata.es/madrid/metro/stops/<stop_id>` | - | foaf:page | - | - |
| location_type | gtfs:locationType | gtfs:Location | skos:Concept | `http://transport.linkeddata.es/madrid/metro/stops/<stop_id>` | - | - | getLocationType | `http://transport.linkeddata.es/kos/location-type/stop`, `http://transport.linkeddata.es/kos/location-type/station`, `http://transport.linkeddata.es/kos/location-type/entrance-exit`, `http://transport.linkeddata.es/kos/location-type/generic-node`, `http://transport.linkeddata.es/kos/location-type/boarding-area` |
| parent_station | gtfs:parentStation | gtfs:Stop, gtfs:StationEntrance, gtfs:GenericNode, gtfs:BoardingArea | gtfs:Station | `http://transport.linkeddata.es/madrid/metro/stops/<stop_id>` | stop_id = parent_station | - | - | - |
| stop_timezone | gtfs:timezone | gtfs:Location | - | `http://transport.linkeddata.es/madrid/metro/stops/<stop_id>` | - | xsd:string | - | - |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Stop, gtfs:Station, gtfs:StationEntrance | skos:Concept | `http://transport.linkeddata.es/madrid/metro/stops/<stop_id>` | - | - | getWheelchairAccessible | `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information`, `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible`, `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |
