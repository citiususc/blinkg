| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency_id | :gtfs:id | gtfs:Agency | - | CONCAT("https://transport.linkeddata.es/agency/", agency_id) | - | xsd:string | - | - |
| agency_name | :gtfs:name | gtfs:Agency | - | CONCAT("https://transport.linkeddata.es/agency/", agency_id) | - | foaf:name | - | - |
| agency_url | :gtfs:url | gtfs:Agency | - | CONCAT("https://transport.linkeddata.es/agency/", agency_id) | - | foaf:page | - | - |
| agency_timezone | :gtfs:timezone | gtfs:Agency | - | CONCAT("https://transport.linkeddata.es/agency/", agency_id) | - | xsd:string | - | - |
| agency_lang | :gtfs:language | gtfs:Agency | - | CONCAT("https://transport.linkeddata.es/agency/", agency_id) | - | xsd:string | - | - |
| agency_phone | :gtfs:phoneNumber | gtfs:Agency | - | CONCAT("https://transport.linkeddata.es/agency/", agency_id) | - | foaf:phone | - | - |
| agency_fare_url | :gtfs:fareUrl | gtfs:Agency | - | CONCAT("https://transport.linkeddata.es/agency/", agency_id) | - | foaf:page | - | - |
| route_id | :gtfs:id | gtfs:Route | - | CONCAT("https://transport.linkeddata.es/route/", route_id) | - | xsd:string | - | - |
| agency_id (routes.csv) | :gtfs:agency | gtfs:Route | gtfs:Agency | CONCAT("https://transport.linkeddata.es/route/", route_id) | routes.csv.route_id = routes.csv.route_id | owl:ObjectProperty | - | URI of the corresponding gtfs:Agency |
| route_short_name | :gtfs:shortName | gtfs:Route | - | CONCAT("https://transport.linkeddata.es/route/", route_id) | - | xsd:string | - | - |
| route_long_name | :gtfs:longName | gtfs:Route | - | CONCAT("https://transport.linkeddata.es/route/", route_id) | - | xsd:string | - | - |
| route_desc | :gtfs:desc | gtfs:Route | - | CONCAT("https://transport.linkeddata.es/route/", route_id) | - | xsd:string | - | - |
| route_type | :gtfs:routeType | gtfs:Route | [skos:Concept] | CONCAT("https://transport.linkeddata.es/route/", route_id) | - | owl:ObjectProperty | map_to_skos_concept | URI of the corresponding skos:Concept |
| route_url | :gtfs:url | gtfs:Route | - | CONCAT("https://transport.linkeddata.es/route/", route_id) | - | foaf:page | - | - |
| route_color | :gtfs:color | gtfs:Route | - | CONCAT("https://transport.linkeddata.es/route/", route_id) | - | xsd:string | - | - |
| route_text_color | :gtfs:textColor | gtfs:Route | - | CONCAT("https://transport.linkeddata.es/route/", route_id) | - | xsd:string | - | - |
