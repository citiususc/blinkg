| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency_id | gtfs:id | gtfs:Agency |  | http://example.org/agency/{id} |  | xsd:string |  |  |
| agency_name | gtfs:name | gtfs:Agency |  |  |  | foaf:name | @es |  |
| agency_url | gtfs:url | gtfs:Agency |  |  |  | foaf:page |  |  |
| agency_timezone | gtfs:timezone | gtfs:Agency |  |  |  | xsd:string |  |  |
| agency_lang | gtfs:language | gtfs:Agency |  |  |  | xsd:string |  |  |
| agency_phone | gtfs:phoneNumber | gtfs:Agency |  |  |  | foaf:phone |  |  |
| agency_fare_url | gtfs:fareUrl | gtfs:Agency |  |  |  | foaf:page |  |  |
| route_id | gtfs:id | gtfs:Route |  | http://example.org/route/{id} |  | xsd:string |  |  |
| agency_id (routes) | gtfs:agency | gtfs:Route | gtfs:Agency |  | agency_id = agency_id | owl:ObjectProperty |  |  |
| route_short_name | gtfs:shortName | gtfs:Route |  |  |  | xsd:string |  |  |
| route_long_name | gtfs:longName | gtfs:Route |  |  |  | xsd:string |  |  |
| route_type | gtfs:routeType | gtfs:Route | skos:Concept |  |  | owl:ObjectProperty |  | routeTypeMapper <http://transport.linkeddata.es/kos/route-type/subway> |
| route_url | gtfs:url | gtfs:Route |  |  |  | foaf:page |  |  |
| route_color | gtfs:color | gtfs:Route |  |  |  | xsd:string |  |  |
| route_text_color | gtfs:textColor | gtfs:Route |  |  |  | xsd:string |  |  |
