| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency_id | gtfs:id | gtfs:Agency |  | http://transport.linkeddata.es/agency/{agency_id} |  | xsd:string |  | http://transport.linkeddata.es/agency/{agency_id} |
| agency_name | gtfs:name | gtfs:Agency |  | http://transport.linkeddata.es/agency/{agency_id} |  | xsd:string |  | {agency_name} |
| agency_url | gtfs:url | gtfs:Agency |  | http://transport.linkeddata.es/agency/{agency_id} |  | xsd:string |  | {agency_url} |
| agency_timezone | gtfs:timezone | gtfs:Agency |  | http://transport.linkeddata.es/agency/{agency_id} |  | xsd:string |  | {agency_timezone} |
| agency_lang | gtfs:language | gtfs:Agency |  | http://transport.linkeddata.es/agency/{agency_id} |  | xsd:string |  | {agency_lang} |
| agency_phone | gtfs:phoneNumber | gtfs:Agency |  | http://transport.linkeddata.es/agency/{agency_id} |  | xsd:string |  | {agency_phone} |
| agency_fare_url | gtfs:fareUrl | gtfs:Agency |  | http://transport.linkeddata.es/agency/{agency_id} |  | xsd:string |  | {agency_fare_url} |
| route_id | gtfs:id | gtfs:Route | gtfs:Agency | http://transport.linkeddata.es/route/{route_id} | agency_id | xsd:string |  | http://transport.linkeddata.es/route/{route_id} |
| agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | http://transport.linkeddata.es/route/{route_id} | agency_id | xsd:string |  | http://transport.linkeddata.es/agency/{agency_id} |
| route_short_name | gtfs:shortName | gtfs:Route |  | http://transport.linkeddata.es/route/{route_id} |  | xsd:string |  | {route_short_name} |
| route_long_name | gtfs:longName | gtfs:Route |  | http://transport.linkeddata.es/route/{route_id} |  | xsd:string |  | {route_long_name} |
| route_desc | gtfs:desc | gtfs:Route |  | http://transport.linkeddata.es/route/{route_id} |  | xsd:string |  | {route_desc} |
| route_type | gtfs:routeType | gtfs:Route |  | http://transport.linkeddata.es/route/{route_id} |  | xsd:string | getRouteType | http://transport.linkeddata.es/kos/route-type/{route_type} |
| route_url | gtfs:url | gtfs:Route |  | http://transport.linkeddata.es/route/{route_id} |  | xsd:string |  | {route_url} |
| route_color | gtfs:color | gtfs:Route |  | http://transport.linkeddata.es/route/{route_id} |  | xsd:string |  | {route_color} |
| route_text_color | gtfs:textColor | gtfs:Route |  | http://transport.linkeddata.es/route/{route_id} |  | xsd:string |  | {route_text_color} |
