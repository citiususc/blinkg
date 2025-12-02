| CSV Column          | Ontology Property     | Entity Class | Related Entity Class | Subject Generation                              | Join | Datatype     | Function Name | Function Output                                           |
|---------------------|-----------------------|--------------|-----------------------|-------------------------------------------------|----------------|--------------|---------------|-----------------------------------------------------------|
| agency_id           | gtfs:id               | gtfs:Agency  |                       | http://transport.linkeddata.es/agency/{agency_id} |                | xsd:string   |               | |
| agency_name         | gtfs:name             | gtfs:Agency  |                       | http://transport.linkeddata.es/agency/{agency_id} |                | xsd:string   |               | |
| agency_url          | gtfs:url              | gtfs:Agency  |                       | http://transport.linkeddata.es/agency/{agency_id} |                | xsd:string   |               | |
| agency_timezone     | gtfs:timezone         | gtfs:Agency  |                       | http://transport.linkeddata.es/agency/{agency_id} |                | xsd:string   |               | |
| agency_lang         | gtfs:language         | gtfs:Agency  |                       | http://transport.linkeddata.es/agency/{agency_id} |                | xsd:string   |               | |
| agency_phone        | gtfs:phoneNumber      | gtfs:Agency  |                       | http://transport.linkeddata.es/agency/{agency_id} |                | xsd:string   |               | |
| agency_fare_url     | gtfs:fareUrl          | gtfs:Agency  |                       | http://transport.linkeddata.es/agency/{agency_id} |                | xsd:string   |               | |
| route_id            | gtfs:id               | gtfs:Route   | gtfs:Agency           | http://transport.linkeddata.es/route/{route_id}   | agency_id      | xsd:string   |               | |
| agency_id           | gtfs:agency           | gtfs:Route   | gtfs:Agency           | http://transport.linkeddata.es/route/{route_id}   | agency_id      | xsd:string   |               | |
| route_short_name    | gtfs:shortName        | gtfs:Route   |                       | http://transport.linkeddata.es/route/{route_id}   |                | xsd:string   |               |{route_short_name}  |
| route_long_name     | gtfs:longName         | gtfs:Route   |                       | http://transport.linkeddata.es/route/{route_id}   |                | xsd:string   |               | {route_long_name} |
| route_type          | gtfs:routeType        | gtfs:Route   |                       | http://transport.linkeddata.es/route/{route_id}   |                | xsd:string   | getRouteType  | http://transport.linkeddata.es/kos/route-type/{route_type} |
| route_url           | gtfs:url              | gtfs:Route   |                       | http://transport.linkeddata.es/route/{route_id}   |                | xsd:string   |               | |
| route_desc          | gtfs:desc             | gtfs:Route   |                       | http://transport.linkeddata.es/route/{route_id}   |                | xsd:string   |               | |
| route_color         | gtfs:color            | gtfs:Route   |                       | http://transport.linkeddata.es/route/{route_id}   |                | xsd:string   |               | |
| route_text_color    | gtfs:textColor        | gtfs:Route   |                       | http://transport.linkeddata.es/route/{route_id}   |                | xsd:string   |               | |
