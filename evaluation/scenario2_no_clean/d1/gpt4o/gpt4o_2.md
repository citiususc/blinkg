| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency_id | gtfs:id | gtfs:Agency | - | `ex:agency/{agency_id}` | - | xsd:string | None | formatAgencyID `ex:agency/CRTM` |
| agency_name | gtfs:name | gtfs:Agency | - | `ex:agency/{agency_id}` | - | xsd:string | @es, @en | - `"Consorcio Regional de Transportes de Madrid"` |
| agency_url | gtfs:url | gtfs:Agency | - | `ex:agency/{agency_id}` | - | foaf:page | None | - `http://www.crtm.es` |
| agency_timezone | gtfs:timezone | gtfs:Agency | - | `ex:agency/{agency_id}` | - | xsd:string | None | - `Europe/Madrid` |
| agency_lang | gtfs:language | gtfs:Agency | - | `ex:agency/{agency_id}` | - | xsd:string | None | formatLanguage `es` |
| agency_phone | gtfs:phoneNumber | gtfs:Agency | - | `ex:agency/{agency_id}` | - | foaf:phone | None | - `012` |
| agency_fare_url | gtfs:fareUrl | gtfs:Agency | - | `ex:agency/{agency_id}` | - | foaf:page | None | - `https://www.crtm.es/billetes-y-tarifas` |
| route_id | gtfs:id | gtfs:Route | - | `ex:route/{route_id}` | - | xsd:string | None | formatRouteID `ex:route/4__1___` |
| agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | `ex:route/{route_id}` | `route.agency_id = agency.agency_id` | URI | None | formatAgencyID `ex:agency/CRTM` |
| route_short_name | gtfs:shortName | gtfs:Route | - | `ex:route/{route_id}` | - | xsd:string | None | - `1`, `10`, `11`, `R`, etc. |
| route_long_name | gtfs:longName | gtfs:Route | - | `ex:route/{route_id}` | - | xsd:string | None | - e.g., `"Pinar de Chamartín-Valdecarros"` |
| route_desc | gtfs:desc | gtfs:Route | - | `ex:route/{route_id}` | - | xsd:string | None | - Empty in dataset (can be omitted) |
| route_type | gtfs:routeType | gtfs:Route | skos:Concept | `ex:route/{route_id}` | - | URI | None | mapRouteType e.g., `http://transport.linkeddata.es/kos/route-type/subway` |
| route_url | gtfs:url | gtfs:Route | - | `ex:route/{route_id}` | - | foaf:page | None | - e.g., `http://www.crtm.es/tu-transporte-publico/metro/lineas/4__1___.aspx` |
| route_color | gtfs:color | gtfs:Route | - | `ex:route/{route_id}` | - | xsd:string | None | formatColor e.g., `2DBEF0` |
| route_text_color | gtfs:textColor | gtfs:Route | - | `ex:route/{route_id}` | - | xsd:string | None | formatColor e.g., `FFFFFF` |

