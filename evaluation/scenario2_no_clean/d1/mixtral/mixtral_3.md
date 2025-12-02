| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency_id | gtfs:id | gtfs:Agency | - | CONCAT("http://transport.linkeddata.es/agency/", agency_id) | Not applicable | xsd:string | - | Identifier for agency in the form of a URL |
| agency_name | gtfs:name | gtfs:Agency | - | Not applicable | Not applicable | foaf:name | - | Name of the agency |
| agency_url | gtfs:url | gtfs:Agency | - | Not applicable | Not applicable | foaf:page | - | URL for the agency |
| agency_timezone | gtfs:timezone | gtfs:Agency | - | Not applicable | Not applicable | xsd:string | - | Timezone for the agency |
| agency_lang | gtfs:language | gtfs:Agency | - | Not applicable | Not applicable | xsd:string | - | Language used by the agency |
| agency_phone | gtfs:phoneNumber | gtfs:Agency | - | Not applicable | Not applicable | foaf:phone | - | Phone number for the agency |
| agency_fare_url | gtfs:fareUrl | gtfs:Agency | - | Not applicable | Not applicable | foaf:page | - | URL for fare information for the agency |
| route_id | gtfs:id | gtfs:Route | - | CONCAT("http://transport.linkeddata.es/route/", route_id) | Not applicable | xsd:string | - | Identifier for route in the form of a URL |
| agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | CONCAT("http://transport.linkeddata.es/agency/", agency_id) | WHERE route_agency_id = agency_id | xsd:string | - | Identifier for agency representing the agency of the route |
| route_short_name | gtfs:shortName | gtfs:Route | - | Not applicable | Not applicable | xsd:string | - | Short name of the route |
| route_long_name | gtfs:longName | gtfs:Route | - | Not applicable | Not applicable | xsd:string | - | Long name of the route |
| route_desc | gtfs:desc | gtfs:Route | - | Not applicable | Not applicable | xsd:string | - | Description for the route |
| route_type | gtfs:routeType | gtfs:Route | skos:Concept | CONCAT("http://transport.linkeddata.es/route-type/", route_type) | WHERE route_type = skos:notation | skos:notation | - | Concept representing the type of route |
| route_url | gtfs:url | gtfs:Route | - | Not applicable | Not applicable | foaf:page | - | URL for the route |
| route_color | gtfs:color | gtfs:Route | - | Not applicable | Not applicable | xsd:string | - | Hexadecimal color (without #) of the route |
| route_text_color | gtfs:textColor | gtfs:Route | - | Not applicable | Not applicable | xsd:string | - | Text color for the route |
