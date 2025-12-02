| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency_id | gtfs:id | gtfs:Agency | - | ex:agency/{agency_id} | agency_id in both CSVs | xsd:string | None | generateAgencyID ex:agency/{agency_id} (e.g., ex:agency/CRTM) |
| agency_name | gtfs:name | gtfs:Agency | - | Same as agency_id | Same as agency_id | foaf:name | @es, @en | - Direct mapping (e.g., "Consorcio Regional de Transportes de Madrid") |
| agency_url | gtfs:url | gtfs:Agency | - | Same as agency_id | Same as agency_id | foaf:page | None | - Direct mapping (e.g., http://www.crtm.es) |
| agency_timezone | gtfs:timezone | gtfs:Agency | - | Same as agency_id | Same as agency_id | xsd:string | None | - Direct mapping (e.g., Europe/Madrid) |
| agency_lang | gtfs:language | gtfs:Agency | - | Same as agency_id | Same as agency_id | xsd:string | None | - Direct mapping (e.g., es) |
| agency_phone | gtfs:phoneNumber | gtfs:Agency | - | Same as agency_id | Same as agency_id | foaf:phone | None | - Direct mapping (e.g., 012) |
| agency_fare_url | gtfs:fareUrl | gtfs:Agency | - | Same as agency_id | Same as agency_id | foaf:page | None | - Direct mapping (e.g., https://www.crtm.es/billetes-y-tarifas) |
| route_id | gtfs:id | gtfs:Route | - | ex:route/{route_id} | route_id in routes.csv | xsd:string | None | generateRouteID ex:route/{route_id} (e.g., ex:route/4__1___) |
| agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | Same as route_id | agency_id in both CSVs | ObjectProperty | None | linkAgencyToRoute Link route ex:route/{route_id} to agency ex:agency/{agency_id} |
| route_short_name | gtfs:shortName | gtfs:Route | - | Same as route_id | Same as route_id | xsd:string | @es, @en | - Direct mapping (e.g., 1, 10) |
| route_long_name | gtfs:longName | gtfs:Route | - | Same as route_id | Same as route_id | xsd:string | @es, @en | - Direct mapping (e.g., Pinar de Chamartín-Valdecarros) |
| route_desc | gtfs:desc | gtfs:Route | - | Same as route_id | Same as route_id | xsd:string | @es, @en | - Direct mapping (empty for your sample, but placeholder available) |
| route_type | gtfs:routeType | gtfs:Route | skos:Concept | Same as route_id | Same as route_id | ObjectProperty | None | mapRouteType Maps route_type code to SKOS URI, e.g., 1 → http://transport.linkeddata.es/kos/route-type/subway |
| route_url | gtfs:url | gtfs:Route | - | Same as route_id | Same as route_id | foaf:page | None | - Direct mapping (e.g., http://www.crtm.es/tu-transporte-publico/metro/lineas/4__1___.aspx) |
| route_color | gtfs:color | gtfs:Route | - | Same as route_id | Same as route_id | xsd:string | None | - Direct mapping (e.g., 2DBEF0) |
| route_text_color | gtfs:textColor | gtfs:Route | - | Same as route_id | Same as route_id | xsd:string | None | - Direct mapping (e.g., FFFFFF) |
