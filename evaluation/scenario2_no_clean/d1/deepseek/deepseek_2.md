| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency.csv/agency_id | gtfs:id | gtfs:Agency | - | http://example.org/agency/{value} | - | xsd:string (CRTM) | - | URI Template http://example.org/agency/CRTM |
| agency_name | gtfs:name | gtfs:Agency | - | - | - | xsd:string | @es | - "Consorcio Regional de Transportes de Madrid"@es |
| agency_url | gtfs:url | gtfs:Agency | - | - | - | foaf:page (URI) | - | - <http://www.crtm.es> |
| agency_timezone | gtfs:timezone | gtfs:Agency | - | - | - | xsd:string | - | - "Europe/Madrid"^^xsd:string |
| agency_lang | gtfs:language | gtfs:Agency | - | - | - | xsd:string | - | Language Code Validation "es"^^xsd:string |
| agency_phone | gtfs:phoneNumber | gtfs:Agency | - | - | - | foaf:phone | - | - "012"^^foaf:phone |
| agency_fare_url | gtfs:fareUrl | gtfs:Agency | - | - | - | foaf:page (URI) | - | - <https://www.crtm.es/billetes-y-tarifas> |
| routes.csv/route_id | gtfs:id | gtfs:Route | - | http://example.org/route/{value} | - | xsd:string | - | URI Template e.g., http://example.org/route/4__1___ |
| agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | - | agency.agency_id = {value} | owl:ObjectProperty | - | Join <http://example.org/agency/CRTM> |
| route_short_name | gtfs:shortName | gtfs:Route | - | - | - | xsd:string | - | - "1"^^xsd:string |
| route_long_name | gtfs:longName | gtfs:Route | - | - | - | xsd:string | - | - "Pinar de Chamartín-Valdecarros"^^xsd:string |
| route_type | gtfs:routeType | gtfs:Route | skos:Concept | - | - | owl:ObjectProperty | - | Route Type Mapping <http://transport.linkeddata.es/kos/route-type/subway> |
| route_url | gtfs:url | gtfs:Route | - | - | - | foaf:page (URI) | - | - <http://www.crtm.es/tu-transporte-publico/metro/lineas/4__1___.aspx> |
| route_color | gtfs:color | gtfs:Route | - | - | - | xsd:string | - | Hex Validation "2DBEF0"^^xsd:string |
| route_text_color | gtfs:textColor | gtfs:Route | - | - | - | xsd:string | - | Hex Validation "FFFFFF"^^xsd:string |
