| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `trip_id` | `gtfs:trip` | `gtfs:StopTime` | `gtfs:Trip` | `http://transport.linkeddata.es/trip/{trip_id}` | - | `http://transport.linkeddata.es/trip/4_I12-001_2016I12_1_1_4___` |
| `arrival_time` | `gtfs:arrivalTime` | `gtfs:StopTime` | - | `http://transport.linkeddata.es/stopTime/{stop_id}/{trip_id}` | `formatTime` | `08:15:00` |
| `pickup_type` | `gtfs:pickupType` | `gtfs:StopTime` | - | same as above | `mapPickupType` | `http://transport.linkeddata.es/kos/pickup/must-phone` |
| `drop_off_type` | `gtfs:dropOffType` | `gtfs:StopTime` | - | same as above | `mapDropOffType` | `http://transport.linkeddata.es/kos/drop-off/available` |
| `wheelchair_boarding` | `gtfs:wheelchairAccessible` | `gtfs:Stop` | - | `http://transport.linkeddata.es/stop/{stop_id}` | `mapWheelchairBoarding` | `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information` |
| `direction_id` | `gtfs:direction` | `gtfs:Trip` | - | `http://transport.linkeddata.es/trip/{trip_id}` | `mapDirection` | `http://transport.linkeddata.es/kos/direction/opposite-direction` |
| `wheelchair_accessible` | `gtfs:wheelchairAccessible` | `gtfs:Trip` | - | `http://transport.linkeddata.es/trip/{trip_id}` | `mapWheelchairAccessible` | `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible` |

| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `http://transport.linkeddata.es/kos/pickup/available` |
| 1 | `http://transport.linkeddata.es/kos/pickup/not-available` |
| 2 | `http://transport.linkeddata.es/kos/pickup/must-phone` |
| 3 | `http://transport.linkeddata.es/kos/pickup/coordinate-with-driver` |

| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `http://transport.linkeddata.es/kos/drop-off/available` |
| 1 | `http://transport.linkeddata.es/kos/drop-off/not-available` |
| 2 | `http://transport.linkeddata.es/kos/drop-off/must-phone` |
| 3 | `http://transport.linkeddata.es/kos/drop-off/coordinate-with-driver` |

| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `http://transport.linkeddata.es/kos/wheelchair-accesible/no-information` |
| 1 | `http://transport.linkeddata.es/kos/wheelchair-accesible/accesible` |
| 2 | `http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible` |

| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `http://transport.linkeddata.es/kos/direction/one-direction` |
| 1 | `http://transport.linkeddata.es/kos/direction/opposite-direction` |
