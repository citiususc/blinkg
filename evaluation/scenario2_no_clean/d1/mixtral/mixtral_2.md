| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency_id | gtfs:id | gtfs:Agency | - | "http://transport.linkeddata.es/agency/" + value | - | string | upperCamelCase | UpperCamelCase (e.g., CRTM) |
| agency_name | gtfs:name | gtfs:Agency | - | "http://transport.linkeddata.es/agency/" + value | - | string | stringValue | OriginalStringValue (e.g., "CRTM") |
| agency_url | gtfs:url | gtfs:Agency | - | "http://transport.linkeddata.es/agency/" + value | - | URI | uri | URI (e.g., http://www.crtm.es) |
| agency_timezone | gtfs:timezone | gtfs:Agency | - | "http://transport.linkeddata.es/agency/" + value | - | string | stringValue | OriginalStringValue (e.g., "Europe/Madrid") |
| agency_lang | gtfs:language | gtfs:Agency | - | "http://transport.linkeddata.es/agency/" + value | - | string | stringValue | OriginalStringValue (e.g., "es") |
| agency_phone | gtfs:phoneNumber | gtfs:Agency | - | "http://transport.linkeddata.es/agency/" + value | - | phone | stringValue | OriginalStringValue (e.g., "012") |
| agency_fare_url | gtfs:fareUrl | gtfs:Agency | - | "http://transport.linkeddata.es/agency/" + value | - | URI | uri | URI (e.g., https://www.crtm.es) |
| route_id | gtfs:id | gtfs:Route | - | "http://transport.linkeddata.es/route/" + value | - | string | upperCamelCase | UpperCamelCase (e.g., 4__1____) |
| agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | "http://transport.linkeddata.es/agency/" + value | agency.agency_id = route.agency_id | URI | uri | URI (e.g., http://transport.linkeddata.es/agency/CRTM) |
| route_short_name | gtfs:shortName | gtfs:Route | - | "http://transport.linkeddata.es/route/" + value | - | string | stringValue | OriginalStringValue (e.g., "1") |
| route_long_name | gtfs:longName | gtfs:Route | - | "http://transport.linkeddata.es/route/" + value | - | string | stringValue | OriginalStringValue (e.g., "Pinar de Chamartín-Valdecarros") |
| route_desc | gtfs:desc | gtfs:Route | - | "http://transport.linkeddata.es/route/" + value | - | string | stringValue | OriginalStringValue (e.g., "") |
| route_type | gtfs:routeType | gtfs:Route | - | "http://transport.linkeddata.es/route/" + value | - | URI | uri | URI (e.g., http://transport.linkeddata.es/route/type/Subway) |
