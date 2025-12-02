| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency_id (agency) | gtfs:id | gtfs:Agency | - | http://example.org/agency/{id} | - | xsd:string | - | URI Template http://example.org/agency/CRTM |
| agency_name | gtfs:name | gtfs:Agency | - | - | - | xsd:string | @es | - "Consorcio Regional de Transportes de Madrid"@es |
| agency_url | gtfs:url | gtfs:Agency | - | - | - | xsd:anyURI | - | - "http://www.crtm.es" |
| agency_timezone | gtfs:timezone | gtfs:Agency | - | - | - | xsd:string | - | - "Europe/Madrid" |
| agency_lang | gtfs:language | gtfs:Agency | - | - | - | xsd:string | - | - "es" |
| agency_phone | gtfs:phoneNumber | gtfs:Agency | - | - | - | xsd:string | - | - "012" |
| agency_fare_url | gtfs:fareUrl | gtfs:Agency | - | - | - | xsd:anyURI | - | - "https://www.crtm.es/billetes-y-tarifas" |
| route_id | gtfs:id | gtfs:Route | - | http://example.org/route/{id} | - | xsd:string | - | URI Template http://example.org/route/4__1___ |
| agency_id (routes) | gtfs:agency | gtfs:Route | gtfs:Agency | - | agency_id = agency_id | owl:NamedIndividual | - | Join by agency_id <http://example.org/agency/CRTM> |
| route_short_name | gtfs:shortName | gtfs:Route | - | - | - | xsd:string | @es | - "1"@es |
| route_long_name | gtfs:longName | gtfs:Route | - | - | - | xsd:string | @es | - "Pinar de Chamartín-Valdecarros"@es |
| route_type | gtfs:routeType | gtfs:Route | skos:Concept | - | - | owl:NamedIndividual | - | map_route_type <http://transport.linkeddata.es/kos/route-type/subway> |
| route_url | gtfs:url | gtfs:Route | - | - | - | xsd:anyURI | - | - "http://www.crtm.es/tu-transporte-publico/metro/lineas/4__1___.aspx" |
| route_color | gtfs:color | gtfs:Route | - | - | - | xsd:string | - | - "2DBEF0" |
| route_text_color | gtfs:textColor | gtfs:Route | - | - | - | xsd:string | - | - "FFFFFF" |
