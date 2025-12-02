| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **agency.csv** |  |  |  |  |  |  |  |  |
| agency_id | gtfs:id | gtfs:Agency |  | http://transport.linkeddata.es/madrid/agency/{agency_id} |  | xsd:string |  |  |
| agency_name | gtfs:name | gtfs:Agency |  | http://transport.linkeddata.es/madrid/agency/{agency_id} |  | foaf:name |  |  |
| agency_url | gtfs:url | gtfs:Agency |  | http://transport.linkeddata.es/madrid/agency/{agency_id} |  | foaf:page |  |  |
| agency_timezone | gtfs:timezone | gtfs:Agency |  | http://transport.linkeddata.es/madrid/agency/{agency_id} |  | xsd:string |  |  |
| agency_lang | gtfs:language | gtfs:Agency |  | http://transport.linkeddata.es/madrid/agency/{agency_id} |  | xsd:string |  |  |
| agency_phone | gtfs:phoneNumber | gtfs:Agency |  | http://transport.linkeddata.es/madrid/agency/{agency_id} |  | foaf:phone |  |  |
| agency_fare_url | gtfs:fareUrl | gtfs:Agency |  | http://transport.linkeddata.es/madrid/agency/{agency_id} |  | foaf:page |  |  |
| **routes.csv** |  |  |  |  |  |  |  |  |
| route_id | gtfs:id | gtfs:Route |  | http://transport.linkeddata.es/madrid/route/{route_id} |  | xsd:string |  |  |
| agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | http://transport.linkeddata.es/madrid/route/{route_id} | agency.agency_id = routes.agency_id | owl:ObjectProperty |  | http://transport.linkeddata.es/madrid/agency/{agency_id} |
| route_short_name | gtfs:shortName | gtfs:Route |  | http://transport.linkeddata.es/madrid/route/{route_id} |  | xsd:string |  |  |
| route_long_name | gtfs:longName | gtfs:Route |  | http://transport.linkeddata.es/madrid/route/{route_id} |  | xsd:string |  |  |
| route_desc | gtfs:desc | gtfs:Route |  | http://transport.linkeddata.es/madrid/route/{route_id} |  | xsd:string |  |  |
| route_type | gtfs:routeType | gtfs:Route | skos:Concept | http://transport.linkeddata.es/madrid/route/{route_id} |  | owl:ObjectProperty | map_route_type | http://transport.linkeddata.es/kos/route-type/{value} |
| route_url | gtfs:url | gtfs:Route |  | http://transport.linkeddata.es/madrid/route/{route_id} |  | foaf:page |  |  |
| route_color | gtfs:color | gtfs:Route |  | http://transport.linkeddata.es/madrid/route/{route_id} |  | xsd:string |  |  |
| route_text_color | gtfs:textColor | gtfs:Route |  | http://transport.linkeddata.es/madrid/route/{route_id} |  | xsd:string |  |  |
