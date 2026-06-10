| Data Reference           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    |Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| stops.csv stop_id | gtfs:id | gtfs:Location | - | http://example.org/stop/{stop_id} | - | xsd:string | - | - |
| stops.csv stop_code | gtfs:code | gtfs:Location | - | http://example.org/stop/{stop_id} | - | xsd:string | - | - |
| stops.csv stop_name | gtfs:name | gtfs:Location | - | http://example.org/stop/{stop_id} | - | foaf:name | - | - |
| stops.csv stop_desc | gtfs:desc | gtfs:Location | - | http://example.org/stop/{stop_id} | - | xsd:string | - | - |
| stops.csv stop_lat | gtfs:latitude | gtfs:Stop/gtfs:Station/gtfs:StationEntrance | - | http://example.org/stop/{stop_id} | - | geo:lat | - | - |
| stops.csv stop_lon | gtfs:longitude | gtfs:Stop/gtfs:Station/gtfs:StationEntrance | - | http://example.org/stop/{stop_id} | - | geo:lon | - | - |
| stops.csv stop_url | gtfs:url | gtfs:Location | - | http://example.org/stop/{stop_id} | - | foaf:page | - | - |
| stops.csv stop_timezone | gtfs:timezone | gtfs:Location | - | http://example.org/stop/{stop_id} | - | xsd:string | - | - |
| stops.csv location_type | gtfs:locationType | gtfs:Location | skos:Concept | http://example.org/stop/{stop_id} | - | - | - | locationTypeSKOS 0 -> `http://transport.linkeddata.es/kos/location-type/stop` <br> 1 -> `http://transport.linkeddata.es/kos/location-type/station` <br> 2 -> `http://transport.linkeddata.es/kos/location-type/entrance-exit` <br> 3 -> `http://transport.linkeddata.es/kos/location-type/generic-node` <br> 4 -> `http://transport.linkeddata.es/kos/location-type/boarding-area` |
| stops.csv parent_station | gtfs:parentStation | gtfs:Stop | gtfs:Station | http://example.org/stop/{stop_id} | stops.csv parent_station = stops.csv stop_id | - | - | - |
| stops.csv wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Stop/gtfs:Station/gtfs:StationEntrance | skos:Concept | http://example.org/stop/{stop_id} | - | - | - | wheelchairBoardingSKOS 0 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information` <br> 1 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible` <br>  2 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |
