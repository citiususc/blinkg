| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency_id | gtfs:id | gtfs:Agency |  | `ex:agency/{agency_id}` |  | xsd:string | None | formatAgencyId ex:agency/CRTM |
| agency_name | gtfs:name | gtfs:Agency |  | `ex:agency/{agency_id}` |  | foaf:name | None |  Direct mapping |
| agency_url | gtfs:url | gtfs:Agency |  | `ex:agency/{agency_id}` |  | foaf:page | None |  Direct mapping |
| agency_timezone | gtfs:timezone | gtfs:Agency |  | `ex:agency/{agency_id}` |  | xsd:string | None |  Direct mapping |
| agency_lang | gtfs:language | gtfs:Agency |  | `ex:agency/{agency_id}` |  | xsd:string | None | languageFormat Must capitalize: `Es` |
| agency_phone | gtfs:phoneNumber | gtfs:Agency |  | `ex:agency/{agency_id}` |  | foaf:phone | None | phoneFormat Format to international if needed, e.g., `+34 012` |
| agency_fare_url | gtfs:fareUrl | gtfs:Agency |  | `ex:agency/{agency_id}` |  | foaf:page | None |  Direct mapping |
| route_id | gtfs:id | gtfs:Route |  | `ex:route/{route_id}` |  | xsd:string | None | formatRouteId ex:route/4__1___ |
| agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | `ex:route/{route_id}` | `routes.agency_id = agency.agency_id` | URI reference | None | linkAgencyToRoute Object property linking `ex:route/{route_id}` → `ex:agency/{agency_id}` |
| route_short_name | gtfs:shortName | gtfs:Route |  | `ex:route/{route_id}` |  | xsd:string | None |  Direct mapping |
| route_long_name | gtfs:longName | gtfs:Route |  | `ex:route/{route_id}` |  | xsd:string | None |  Direct mapping |
| route_desc | gtfs:desc | gtfs:Route |  | `ex:route/{route_id}` |  | xsd:string | None |  Direct mapping (nullable) |
| route_type | gtfs:routeType | gtfs:Route | skos:Concept | `ex:route/{route_id}` |  | URI | None | mapRouteTypeToSKOS Map integer value:<br>0 → `tram`<br>1 → `subway`<br>2 → `rail`<br>3 → `bus`<br>4 → `ferry`<br>5 → `cable-tram`<br>6 → `aerial-lift`<br>7 → `funicular`<br>11 → `trolleybus`<br>12 → `monorail` |
| route_url | gtfs:url | gtfs:Route |  | `ex:route/{route_id}` |  | foaf:page | None |  Direct mapping |
| route_color | gtfs:color | gtfs:Route |  | `ex:route/{route_id}` |  | xsd:string | None | hexColorFormat Remove `#` if present; 6 characters |
| route_text_color | gtfs:textColor | gtfs:Route |  | `ex:route/{route_id}` |  | xsd:string | None | hexColorFormat Remove `#` if present; 6 characters |
