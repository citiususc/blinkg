| CSV Column        | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
|-------------------|-------------------|--------------|-----------------------|--------------------|----------------|----------|---------------|-----------------|
| agency_id         | gtfs:id           | gtfs:Agency  | -                     | CONCAT("http://transport.linkeddata.es/agency/", agency_id) | Not applicable | xsd:string | - | |
| agency_name       | gtfs:name         | gtfs:Agency  | -                     | Not applicable | Not applicable | foaf:name | - | |
| agency_url        | gtfs:url          | gtfs:Agency  | -                     | Not applicable | Not applicable | foaf:page | - | |
| agency_timezone   | gtfs:timezone     | gtfs:Agency  | -                     | Not applicable | Not applicable | xsd:string | - | |
| agency_lang       | gtfs:language     | gtfs:Agency  | -                     | Not applicable | Not applicable | xsd:string | - | |
| agency_phone      | gtfs:phoneNumber  | gtfs:Agency  | -                     | Not applicable | Not applicable | foaf:phone | - | |
| agency_fare_url   | gtfs:fareUrl      | gtfs:Agency  | -                     | Not applicable | Not applicable | foaf:page | - | |
| route_id          | gtfs:id           | gtfs:Route   | -                     | CONCAT("http://transport.linkeddata.es/route/", route_id) | Not applicable | xsd:string | - | |
| agency_id         | gtfs:agency       | gtfs:Route   | gtfs:Agency           | CONCAT("http://transport.linkeddata.es/agency/", agency_id) | WHERE route_agency_id = agency_id | | - | |
| route_short_name  | gtfs:shortName    | gtfs:Route   | -                     | Not applicable | Not applicable | xsd:string | - | Short name of the route |
| route_long_name   | gtfs:longName     | gtfs:Route   | -                     | Not applicable | Not applicable | xsd:string | - | Long name of the route |
| route_desc        | gtfs:desc         | gtfs:Route   | -                     | Not applicable | Not applicable | xsd:string | - | |
| route_type        | gtfs:routeType    | gtfs:Route   | skos:Concept          | CONCAT("http://transport.linkeddata.es/route-type/", route_type) | Not applicable | | - | Concept representing the type of route |
| route_url         | gtfs:url          | gtfs:Route   | -                     | Not applicable | Not applicable | foaf:page | - | |
| route_color       | gtfs:color        | gtfs:Route   | -                     | Not applicable | Not applicable | xsd:string | - | |
| route_text_color  | gtfs:textColor    | gtfs:Route   | -                     | Not applicable | Not applicable | xsd:string | - | |
