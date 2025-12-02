| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **agency.csv** |  |  |  |  |  |  |  |  |
| agency_id | gtfs:id | gtfs:Agency |  | `ex:Agency_{agency_id}` |  | xsd:string |  | `ex:Agency_CRTM` |
| agency_name | gtfs:name | gtfs:Agency |  | `ex:Agency_{agency_id}` |  | foaf:name |  |  |
| agency_url | gtfs:url | gtfs:Agency |  | `ex:Agency_{agency_id}` |  | foaf:page |  |  |
| agency_timezone | gtfs:timezone | gtfs:Agency |  | `ex:Agency_{agency_id}` |  | xsd:string |  |  |
| agency_lang | gtfs:language | gtfs:Agency |  | `ex:Agency_{agency_id}` |  | xsd:string |  |  |
| agency_phone | gtfs:phoneNumber | gtfs:Agency |  | `ex:Agency_{agency_id}` |  | foaf:phone |  |  |
| agency_fare_url | gtfs:fareUrl | gtfs:Agency |  | `ex:Agency_{agency_id}` |  | foaf:page |  |  |
| **routes.csv** |  |  |  |  |  |  |  |  |
| route_id | gtfs:id | gtfs:Route |  | `ex:Route_{route_id}` |  | xsd:string |  | `ex:Route_4__1___` |
| agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | `ex:Route_{route_id}` | `agency.agency_id` = `routes.agency_id` |  |  |  |
| route_short_name | gtfs:shortName | gtfs:Route |  | `ex:Route_{route_id}` |  | xsd:string |  |  |
| route_long_name | gtfs:longName | gtfs:Route |  | `ex:Route_{route_id}` |  | xsd:string |  |  |
| route_desc | gtfs:desc | gtfs:Route |  | `ex:Route_{route_id}` |  | xsd:string |  |  |
| route_type | gtfs:routeType | gtfs:Route | skos:Concept | `ex:Route_{route_id}` |  |  | `map_route_type` | `http://transport.linkeddata.es/kos/route-type/subway`, `http://transport.linkeddata.es/kos/route-type/bus`, etc. |
| route_url | gtfs:url | gtfs:Route |  | `ex:Route_{route_id}` |  | foaf:page |  |  |
| route_color | gtfs:color | gtfs:Route |  | `ex:Route_{route_id}` |  | xsd:string |  |  |
| route_text_color | gtfs:textColor | gtfs:Route |  | `ex:Route_{route_id}` |  | xsd:string |  |  |
