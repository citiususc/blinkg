| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    |Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency.csv agency_id | gtfs:id | gtfs:Agency | - | ex:agency/{agency_id} | - | xsd:string | - | - |
| agency.csv agency_name | gtfs:name | gtfs:Agency | - | ex:agency/{agency_id} | - | foaf:name | - | - |
| agency.csv agency_url | gtfs:url | gtfs:Agency | - | ex:agency/{agency_id} | - | foaf:page | - | - |
| agency.csv agency_timezone | gtfs:timezone | gtfs:Agency | - | ex:agency/{agency_id} | - | xsd:string | - | - |
| agency.csv agency_lang | gtfs:language | gtfs:Agency | - | ex:agency/{agency_id} | - | xsd:string | - | - |
| agency.csv agency_phone | gtfs:phoneNumber | gtfs:Agency | - | ex:agency/{agency_id} | - | foaf:phone | - | - |
| agency.csv agency_fare_url | gtfs:fareUrl | gtfs:Agency | - | ex:agency/{agency_id} | - | foaf:page | - | - |
| routes.csv route_id | gtfs:id | gtfs:Route | - | ex:route/{route_id} | - | xsd:string | - | - |
| routes.csv agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | ex:route/{route_id} | routes.agency_id = agency.agency_id | - | - | - |
| routes.csv route_short_name | gtfs:shortName | gtfs:Route | - | ex:route/{route_id} | - | xsd:string | capitalize | Input string in capital format |
| routes.csv route_long_name | gtfs:longName | gtfs:Route | - | ex:route/{route_id} | - | xsd:string | capitalize | Input string in capital format |
| routes.csv route_desc | gtfs:desc | gtfs:Route | - | ex:route/{route_id} | - | xsd:string | - | - |
| routes.csv route_type | gtfs:routeType | gtfs:Route | skos:Concept | ex:route/{route_id} | - | - | routeTypeSKOS | 0->`http://transport.linkeddata.es/kos/route-type/tram` <br> 1 -> `http://transport.linkeddata.es/kos/route-type/subway` <br> 2 -> `http://transport.linkeddata.es/kos/route-type/rail` <br> 3 -> `http://transport.linkeddata.es/kos/route-type/bus` <br> 4 -> `http://transport.linkeddata.es/kos/route-type/ferry` <br> 5 -> `http://transport.linkeddata.es/kos/route-type/cable-tram` <br> 6 -> `http://transport.linkeddata.es/kos/route-type/aerial-lift` 7 -> `http://transport.linkeddata.es/kos/route-type/funicular` <br> 11 -> `http://transport.linkeddata.es/kos/route-type/trolleybus` <br> 12 -> `http://transport.linkeddata.es/kos/route-type/monorail` |
| routes.csv route_url | gtfs:url | gtfs:Route | - | ex:route/{route_id} | - | foaf:page | - | - |
| routes.csv route_color | gtfs:color | gtfs:Route | - | ex:route/{route_id} | - | xsd:string | - | - |
| routes.csv route_text_color | gtfs:textColor | gtfs:Route | - | ex:route/{route_id} | - | xsd:string | - | - |
