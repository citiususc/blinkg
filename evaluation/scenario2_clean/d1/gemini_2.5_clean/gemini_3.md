| CSV Column | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| agency_id | gtfs:id | gtfs:Agency | | http://transport.linkeddata.es/madrid/agency/{agency_id} | | xsd:string | | |
| agency_name | gtfs:name | gtfs:Agency | | | | foaf:name | | |
| agency_url | gtfs:url | gtfs:Agency | | | | foaf:page | | |
| agency_timezone | gtfs:timezone | gtfs:Agency | | | | xsd:string | | |
| agency_lang | gtfs:language | gtfs:Agency | | | | xsd:string | | |
| agency_phone | gtfs:phoneNumber | gtfs:Agency | | | | foaf:phone | | |
| agency_fare_url | gtfs:fareUrl | gtfs:Agency | | | | foaf:page | | |
| route_id | gtfs:id | gtfs:Route | | http://transport.linkeddata.es/madrid/route/{route_id} | | xsd:string | | |
| agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | | `routes.csv`.`agency_id` == `agency.csv`.`agency_id` | | | |
| route_short_name | gtfs:shortName | gtfs:Route | | | | xsd:string | | |
| route_long_name | gtfs:longName | gtfs:Route | | | | xsd:string | | |
| route_desc | gtfs:desc | gtfs:Route | | | | xsd:string | | |
| route_url | gtfs:url | gtfs:Route | | | | foaf:page | | |
| route_color | gtfs:color | gtfs:Route | | | | xsd:string | | |
| route_text_color | gtfs:textColor | gtfs:Route | | | | xsd:string | | |
| route_type | gtfs:routeType | gtfs:Route | skos:Concept | | | | `map_route_type` | `http://transport.linkeddata.es/kos/route-type/{output}` where output can be: `tram`, `subway`, `rail`, `bus`, `ferry`, `cable-tram`, `aerial-lift`, `funicular`, `trolleybus`, `monorail` |
