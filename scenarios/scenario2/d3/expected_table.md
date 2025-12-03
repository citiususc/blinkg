| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    |Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| stop_id | gtfs:id | gtfs:Location | - | ex:stop/{stop_id} | - | xsd:string | - | - |
| stop_code | gtfs:code | gtfs:Location | - | ex:stop/{stop_id} | - | xsd:string | - | - |
| stop_name | gtfs:name | gtfs:Location | - | ex:stop/{stop_id} | - | foaf:name | - | - |
| stop_desc | gtfs:desc | gtfs:Location | - | ex:stop/{stop_id} | - | xsd:string | - | - |
| stop_lat | gtfs:latitude | gtfs:Stop/gtfs:Station/gtfs:StationEntrance | - | ex:stop/{stop_id} | - | geo:lat | - | - |
| stop_lon | gtfs:longitude | gtfs:Stop/gtfs:Station/gtfs:StationEntrance | - | ex:stop/{stop_id} | - | geo:lon | - | - |
| stop_url | gtfs:url | gtfs:Location | - | ex:stop/{stop_id} | - | foaf:page | - | - |
| stop_timezone | gtfs:timezone | gtfs:Location | - | ex:stop/{stop_id} | - | xsd:string | - | - |
| location_type | gtfs:locationType | gtfs:Location | skos:Concept | ex:stop/{stop_id} | - | - | - | locationTypeSKOS 0 -> `http://transport.linkeddata.es/kos/location-type/stop` <br> 1 -> `http://transport.linkeddata.es/kos/location-type/station` <br> 2 -> `http://transport.linkeddata.es/kos/location-type/entrance-exit` <br> 3 -> `http://transport.linkeddata.es/kos/location-type/generic-node` <br> 4 -> `http://transport.linkeddata.es/kos/location-type/boarding-area` |
| parent_station | gtfs:parentStation | gtfs:Stop | gtfs:Station | ex:stop/{stop_id} | parent_station=stop_id | - | - | - |
| wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Stop/gtfs:Station/gtfs:StationEntrance | skos:Concept | ex:stop/{stop_id} | - | - | - | wheelchairBoardingSKOS 0 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information` <br> 1 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible` <br>  2 -> `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |
