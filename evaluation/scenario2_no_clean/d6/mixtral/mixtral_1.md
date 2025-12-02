| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `trip_id` | `gtfs:trip` | `gtfs:Trip` | - | `http://vocab.gtfs.org/id/{trip_id}` | - | `xsd:string` | - | URI of the Trip |
| `arrival_time` | `gtfs:arrivalTime` | `gtfs:StopTime` | - | Inferred from Trip/Stop combo | `gtfs:trip` | `schema:Time` | - | e.g., `"08:30:00"` |
| `departure_time` | `gtfs:departureTime` | `gtfs:StopTime` | - | Inferred from Trip/Stop combo | `gtfs:trip` | `schema:Time` | - | e.g., `"08:32:00"` |
| `stop_id` | `gtfs:stop` | `gtfs:StopTime` | `gtfs:Stop` | `http://vocab.gtfs.org/id/{stop_id}` | - | `gtfs:Stop` | - | URI of the Stop |
| `stop_sequence` | `gtfs:stopSequence` | `gtfs:StopTime` | - | - | `gtfs:trip` | `xsd:nonNegativeInteger` | - | e.g., `3` |
| `stop_headsign` | `gtfs:headsign` | `gtfs:StopTime` | - | - | `gtfs:trip` | `xsd:string` (pattern) | - | Must match pattern: `^([A-Z][a-z])(\s[A-Z][a-z])*$` |
| `pickup_type` | `gtfs:pickupType` | `gtfs:StopTime` | SKOS Concept | SKOS concept URI | - | `skos:Concept` | `skos_concept_uri` | `http://transport.linkeddata.es/kos/pickup/{pickup_type}` (slugified concept) |
| `drop_off_type` | `gtfs:dropOffType` | `gtfs:StopTime` | SKOS Concept | SKOS concept URI | - | `skos:Concept` | `skos_concept_uri` | `http://transport.linkeddata.es/kos/drop-off/{drop_off_type}` (slugified concept) |
| `shape_dist_traveled` | `gtfs:distanceTraveled` | `gtfs:StopTime` | - | - | - | `gtfs:nonNegativeFloat` | `float` | e.g., `1245.75` |
