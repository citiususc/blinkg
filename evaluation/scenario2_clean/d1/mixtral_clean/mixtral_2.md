| CSV Column        | Ontology Property | Entity Class | Related Entity Class | Subject Generation                              | Join                         | Datatype | Function Name   | Function Output|
|-------------------|-------------------|--------------|-----------------------|------------------------------------------------|----------------------------------------|----------|-----------------|-----------------------------------------------------|
| agency_id         | gtfs:id           | gtfs:Agency  | -                     | `http://transport.linkeddata.es/agency/{id}` | -| string   | | |
| agency_name       | gtfs:name         | gtfs:Agency  | -                     | `http://transport.linkeddata.es/agency/{id}` | -| string   | | |
| agency_url        | gtfs:url          | gtfs:Agency  | -                     | `http://transport.linkeddata.es/agency/{id}` | -|       | | |
| agency_timezone   | gtfs:timezone     | gtfs:Agency  | -                     | `http://transport.linkeddata.es/agency/{id}` | -| string   | | |
| agency_lang       | gtfs:language     | gtfs:Agency  | -                     | `http://transport.linkeddata.es/agency/{id}` | -| string   | | |
| agency_phone      | gtfs:phoneNumber  | gtfs:Agency  | -                     | `http://transport.linkeddata.es/agency/{id}` | -| phone    | | |
| agency_fare_url   | gtfs:fareUrl      | gtfs:Agency  | -                     | `http://transport.linkeddata.es/agency/{id}` | -|       | | |
| route_id          | gtfs:id           | gtfs:Route   | -                     | `http://transport.linkeddata.es/route/{id}`  | -| string   | | |
| agency_id         | gtfs:agency       | gtfs:Route   | gtfs:Agency           | `http://transport.linkeddata.es/agency/{id}` | agency.agency_id = route.agency_id     |       | | |
| route_short_name  | gtfs:shortName    | gtfs:Route   | -                     | `http://transport.linkeddata.es/route/{id}`  | -| string   | stringValue     | OriginalStringValue (e.g., "1")                     |
| route_long_name   | gtfs:longName     | gtfs:Route   | -                     | `http://transport.linkeddata.es/route/{id}`  | -| string   | stringValue     | OriginalStringValue (e.g., "Pinar de Chamartín-Valdecarros") |
| route_desc        | gtfs:desc         | gtfs:Route   | -                     | `http://transport.linkeddata.es/route/{id}`  | -| string   | | |
| route_type        | gtfs:routeType    | gtfs:Route   | -                     | `http://transport.linkeddata.es/route/{id}`  | -|       | uri             | URI (e.g., http://transport.linkeddata.es/route/type/Subway) |
