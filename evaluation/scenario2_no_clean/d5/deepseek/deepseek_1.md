| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id (frequencies) | gtfs:trip | Frequency | Trip | <http://example.org/frequency/{trip_id}+{start_time}> | trip_id = trips.trip_id | xsd:anyURI |  |  |
| start_time | gtfs:startTime | Frequency |  |  |  | schema:Time |  |  |
| end_time | gtfs:endTime | Frequency |  |  |  | schema:Time |  |  |
| headway_secs | gtfs:headwaySeconds | Frequency |  |  |  | xsd:positiveInteger |  |  |
| trip_id (trips) | gtfs:id | Trip |  | <http://example.org/trip/{trip_id}> |  | xsd:string |  |  |
| route_id | gtfs:route | Trip | Route |  | route_id = routes.route_id | xsd:anyURI |  |  <http://example.org/route/{route_id}> |
| service_id | gtfs:service | Trip | Service |  | service_id = calendar.service_id | xsd:anyURI |  |  <http://example.org/service/{service_id}> |
| direction_id | gtfs:direction | Trip |  |  |  | skos:Concept | @en | map_direction 0 → <http://transport.linkeddata.es/kos/direction/one-direction>, 1 → opposite |
| wheelchair_accessible | gtfs:wheelchairAccessible | Trip |  |  |  | skos:Concept | @en | map_wheelchair_accessibility 1 → accesible, 2 → inaccesible, 0 → no-information |
| trip_headsign | gtfs:headsign | Trip |  |  |  | xsd:string (pattern enforced) |  | clean_headsign Capitalized string (e.g., "Valdecarros" → "Valdecarros") |
| trip_short_name | gtfs:shortName | Trip |  |  |  | xsd:string (pattern enforced) |  | format_short_name Validated format (e.g., "Pinar de Chamartin-Valdecarros" → remains) |
| shape_id | gtfs:shape | Trip | Shape |  | shape_id = shapes.shape_id | xsd:anyURI |  |  <http://example.org/shape/{shape_id}> |
| route_short_name | gtfs:shortName | Route |  | <http://example.org/route/{route_id}> |  | xsd:string (pattern enforced) |  | format_route_short Validated uppercase (e.g., "1" → "1") |
| route_long_name | dct:description | Route |  |  |  | xsd:string | @es |  |
| route_url | foaf:page | Route |  |  |  | xsd:anyURI |  |  |
| shape_pt_lat | geo:lat | Shape |  | <http://example.org/shape/{shape_id}> |  | xsd:decimal |  |  |
| shape_pt_lon | geo:long | Shape |  |  |  | xsd:decimal |  |  |
| monday | gtfs:serviceDay | Service |  | <http://example.org/service/{service_id}> |  | xsd:boolean |  |  |
| start_date | dct:valid | Service |  |  |  | xsd:date |  |  |
| exception_type | gtfs:serviceException | Service |  |  |  | xsd:integer |  |  |
