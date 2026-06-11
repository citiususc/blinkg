| Data Reference           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency.csv agency_id | gtfs:id | gtfs:Agency | - | http://example.org/agency/{agency_id} | - | xsd:string | - | - |
| agency.csv agency_name | gtfs:name | gtfs:Agency | - | http://example.org/agency/{agency_id} | - | foaf:name | - | - |
| agency.csv agency_url | gtfs:url | gtfs:Agency | - | http://example.org/agency/{agency_id} | - | foaf:page | - | - |
| agency.csv agency_timezone | gtfs:timezone | gtfs:Agency | - | http://example.org/agency/{agency_id} | - | xsd:string | - | - |
| agency.csv agency_lang | gtfs:language | gtfs:Agency | - | http://example.org/agency/{agency_id} | - | xsd:string | - | - |
| agency.csv agency_phone | gtfs:phoneNumber | gtfs:Agency | - | http://example.org/agency/{agency_id} | - | foaf:phone | - |  |
| agency.csv agency_fare_url | gtfs:fareUrl | gtfs:Agency | - | http://example.org/agency/{agency_id} | - | foaf:page | - | - |
| routes.csv route_id | gtfs:id | gtfs:Route | - | http://example.org/route/{route_id} | - | xsd:string | - | - |
| routes.csv agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | http://example.org/route/{route_id} | routes.csv agency_id = agency.csv agency_id | - | - | - |
| routes.csv route_short_name | gtfs:shortName | gtfs:Route | - | http://example.org/route/{route_id} | - | xsd:string | capitalize | Input string in capital format |
| routes.csv route_long_name | gtfs:longName | gtfs:Route | - | http://example.org/route/{route_id} | - | xsd:string | capitalize | Input string in capital format |
| routes.csv route_desc | gtfs:desc | gtfs:Route | - | http://example.org/route/{route_id} | - | xsd:string | - | - |
| routes.csv route_type | gtfs:routeType | gtfs:Route | skos:Concept | http://example.org/route/{route_id} | - | - | routeTypeSKOS | 0->http://transport.linkeddata.es/kos/route-type/tram <br> 1 -> http://transport.linkeddata.es/kos/route-type/subway <br> 2 -> http://transport.linkeddata.es/kos/route-type/rail <br> 3 -> http://transport.linkeddata.es/kos/route-type/bus <br> 4 -> http://transport.linkeddata.es/kos/route-type/ferry <br> 5 -> http://transport.linkeddata.es/kos/route-type/cable-tram <br> 6 -> http://transport.linkeddata.es/kos/route-type/aerial-lift 7 -> http://transport.linkeddata.es/kos/route-type/funicular <br> 11 -> http://transport.linkeddata.es/kos/route-type/trolleybus <br> 12 -> http://transport.linkeddata.es/kos/route-type/monorail |
| routes.csv route_url | gtfs:url | gtfs:Route | - | http://example.org/route/{route_id} | - | foaf:page | - | - |
| routes.csv route_color | gtfs:color | gtfs:Route | - | http://example.org/route/{route_id} | - | xsd:string | - | - |
| routes.csv route_text_color | gtfs:textColor | gtfs:Route | - | http://example.org/route/{route_id} | - | xsd:string | - | - |
| shapes.csv shape_id | gtfs:id | gtfs:Shape | - | http://example.org/shape/{shape_id} | - | xsd:string | - |  |
| shapes.csv shape_pt_lat | gtfs:latitude | gtfs:ShapePoint | - | http://example.org/shape/{shape_id}_{shape_pt_sequence} | - | geo:lat | - |  |
| shapes.csv shape_pt_lon | gtfs:longitude | gtfs:ShapePoint | - | http://example.org/shape/{shape_id}_{shape_pt_sequence} | - | geo:lon | - |  |
| shapes.csv shape_pt_sequence | gtfs:pointSequence | gtfs:ShapePoint | - | http://example.org/shape/{shape_id}_{shape_pt_sequence} | - | xsd:nonNegativeInteger | - |  |
| shapes.csv shape_dist_traveled | gtfs:distanceTraveled | gtfs:Shape | - | http://example.org/shape/{shape_id} | - | gtfs:nonNegativeFloat | - |  |
| shapes.csv shape_id | gtfs:shapePoint | gtfs:Shape | gtfs:ShapePoint | http://example.org/shape/{shape_id} | shapes.csv shape_id = shapes.csv shape_id | - | - |  |
| stops.csv stop_id | gtfs:id | gtfs:Location | - | http://example.org/stop/{stop_id} | - | xsd:string | - |  |
| stops.csv stop_code | gtfs:code | gtfs:Location | - | http://example.org/stop/{stop_id} | - | xsd:string | - |  |
| stops.csv stop_name | gtfs:name | gtfs:Location | - | http://example.org/stop/{stop_id} | - | foaf:name | - |  |
| stops.csv stop_desc | gtfs:desc | gtfs:Location | - | http://example.org/stop/{stop_id} | - | xsd:string | - |  |
| stops.csv stop_lat | gtfs:latitude | gtfs:Stop/gtfs:Station/gtfs:StationEntrance | - | http://example.org/stop/{stop_id} | - | geo:lat | - |  |
| stops.csv stop_lon | gtfs:longitude | gtfs:Stop/gtfs:Station/gtfs:StationEntrance | - | http://example.org/stop/{stop_id} | - | geo:lon | - |  |
| stops.csv stop_url | gtfs:url | gtfs:Location | - | http://example.org/stop/{stop_id} | - | foaf:page | - |  |
| stops.csv stop_timezone | gtfs:timezone | gtfs:Location | - | http://example.org/stop/{stop_id} | - | xsd:string | - |  |
| stops.csv location_type | gtfs:locationType | gtfs:Location | skos:Concept | http://example.org/stop/{stop_id} | - | - | locationTypeSKOS | 0 -> http://transport.linkeddata.es/kos/location-type/stop <br> 1 -> http://transport.linkeddata.es/kos/location-type/station <br> 2 -> http://transport.linkeddata.es/kos/location-type/entrance-exit <br> 3 -> http://transport.linkeddata.es/kos/location-type/generic-node <br> 4 -> http://transport.linkeddata.es/kos/location-type/boarding-area |
| stops.csv parent_station | gtfs:parentStation | gtfs:Stop | gtfs:Station | http://example.org/stop/{stop_id} | stops.csv parent_station = stops.csv stop_id | - | - |  |
| stops.csv wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Stop/gtfs:Station/gtfs:StationEntrance | skos:Concept | http://example.org/stop/{stop_id} | - | - | wheelchairBoardingSKOS | 0 -> http://transport.linkeddata.es/kos/wheelchair-accesible/no-information <br> 1 -> http://transport.linkeddata.es/kos/wheelchair-accesible/accesible <br>  2 -> http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible |
| calendar.csv service_id | gtfs:id | gtfs:Service | - | http://example.org/service/{service_id} | - | xsd:string | - | - |
| calendar.csv service_id | gtfs:serviceRule | gtfs:Service | gtfs:ServiceRule | http://example.org/service/{service_id} | calendar.csv service_id = calendar.csv service_id or calendar.csv service_id = calendar_dates.csv service_id | xsd:string | - | - |
| calendar.csv monday | gtfs:monday | gtfs:CalendarRule | skos:Concept | http://example.org/rule/{service_id} | - | - | mapDayAvailability | 1 → <http://transport.linkeddata.es/kos/day/available><br>0 → <http://transport.linkeddata.es/kos/day/not-available> |
| calendar.csv tuesday | gtfs:tuesday | gtfs:CalendarRule | skos:Concept | http://example.org/rule/{service_id} | - | - | mapDayAvailability | Same as above |
| calendar.csv wednesday | gtfs:wednesday | gtfs:CalendarRule | skos:Concept | http://example.org/rule/{service_id} | - | - | mapDayAvailability | Same as above |
| calendar.csv thursday | gtfs:thursday | gtfs:CalendarRule | skos:Concept | http://example.org/rule/{service_id} | - | - | mapDayAvailability | Same as above |
| calendar.csv friday | gtfs:friday | gtfs:CalendarRule | skos:Concept | http://example.org/rule/{service_id} | - | - | mapDayAvailability | Same as above |
| calendar.csv saturday | gtfs:saturday | gtfs:CalendarRule | skos:Concept | http://example.org/rule/{service_id} | - | - | mapDayAvailability | Same as above |
| calendar.csv sunday | gtfs:sunday | gtfs:CalendarRule | skos:Concept | http://example.org/rule/{service_id} | - | - | mapDayAvailability | Same as above |
| calendar.csv start_date | gtfs:startDate | gtfs:CalendarRule | - | http://example.org/rule/{service_id} | - | schema:startDate | - | - |
| calendar.csv end_date | gtfs:endDate | gtfs:CalendarRule | - | http://example.org/rule/{service_id} | - | schema:endDate | - | - |
| calendar_dates.csv date | gtfs:date | gtfs:CalendarDateRule | - | http://example.org/rule/{service_id}_{date} | - | xsd:date | - | - |
| calendar_dates.csv exception_type | gtfs:exceptionType | gtfs:CalendarDateRule | skos:Concept | http://example.org/rule/{service_id}_{date} | - | - | mapExceptionType | 1 → <http://transport.linkeddata.es/kos/exception-type/removed><br>2 → <http://transport.linkeddata.es/kos/exception-type/added> |
| frequencies.csv trip_id | gtfs:trip | gtfs:Frequency | gtfs:Trip | http://example.org/frequency/{trip_id}_{start_time} | frequencies.csv trip_id = trips.csv trip_id | xsd:string | - | - |
| frequencies.csv start_time | gtfs:startTime | gtfs:Frequency | - | http://example.org/frequency/{trip_id}_{start_time} | - | schema:startTime | - | - |
| frequencies.csv end_time | gtfs:endTime | gtfs:Frequency | - | http://example.org/frequency/{trip_id}_{start_time} | - | schema:endTime | - | - |
| frequencies.csv headway_secs | gtfs:headwaySeconds | gtfs:Frequency | - | http://example.org/frequency/{trip_id}_{start_time} | - | xsd:positiveInteger | - | - |
| frequencies.csv exact_times | gtfs:usesExactTimes | gtfs:Frequency | skos:Concept | http://example.org/frequency/{trip_id}_{start_time} | - | - | directionSKOS | 0 -> http://transport.linkeddata.es/kos/direction/one-direction <br> 1 -> http://transport.linkeddata.es/kos/direction/opposite-direction |
| trips.csv trip_id | gtfs:id | gtfs:Trip | - | http://example.org/trip/{trip_id} | - | xsd:string | - | - |
| trips.csv trip_headsign | gtfs:headsign | gtfs:Trip | - | http://example.org/trip/{trip_id} | - | xsd:string | capitalize | Input string in capital format |
| trips.csv trip_short_name | gtfs:shortName | gtfs:Trip | - | http://example.org/trip/{trip_id} | - | foaf:name | capitalize | Input string in capital format |
| trips.csv direction_id | gtfs:direction | gtfs:Trip | skos:Concept | http://example.org/trip/{trip_id} | - | - | directionSKOS | 0 -> http://transport.linkeddata.es/kos/direction/one-direction <br> 1 -> http://transport.linkeddata.es/kos/direction/opposite-direction |
| trips.csv wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | http://example.org/trip/{trip_id} | - | - | wheelchairBoardingSKOS | 0 -> http://transport.linkeddata.es/kos/wheelchair-accesible/no-information <br> 1 -> http://transport.linkeddata.es/kos/wheelchair-accesible/accesible <br>  2 -> http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible |
| trips.csv route_id | gtfs:route | gtfs:Trip | gtfs:Route | http://example.org/trip/{trip_id} | trips.csv route_id = routes.csv route_id | xsd:string | - | - |
| trips.csv service_id | gtfs:service | gtfs:Trip | gtfs:Service | http://example.org/trip/{trip_id} | trips.csv service_id = calendar.csv service_id or trips.csv service_id = calendar_dates.csv service_id | xsd:string | - | - |
| trips.csv trip_id | gtfs:id | gtfs:Trip | - | http://example.org/trip/{trip_id} | - | xsd:string | - | - |
| trips.csv trip_headsign | gtfs:headsign | gtfs:Trip | - | http://example.org/trip/{trip_id} | - | xsd:string | capitalize | Input string in capital format |
| trips.csv trip_short_name | gtfs:shortName | gtfs:Trip | - | http://example.org/trip/{trip_id} | - | xsd:string | capitalize | Input string in capital format |
| trips.csv direction_id | gtfs:direction | gtfs:Trip | skos:Concept | http://example.org/trip/{trip_id} | - | - | directionSKOS | 0 -> http://transport.linkeddata.es/kos/direction/one-direction <br> 1 -> http://transport.linkeddata.es/kos/direction/opposite-direction |
| trips.csv wheelchair_accessible | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | http://example.org/trip/{trip_id} | - | - | wheelchairBoardingSKOS | 0 -> http://transport.linkeddata.es/kos/wheelchair-accesible/no-information <br> 1 -> http://transport.linkeddata.es/kos/wheelchair-accesible/accesible <br>  2 -> http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible |
| stop_times.csv trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | http://example.org/stoptimes/{trip_id}_{stop_sequence} | stop_times.csv trip_id = trips.csv trip_id | - | - | - |
| stop_times.csv arrival_time | gtfs:arrivalTime | gtfs:StopTime | - | http://example.org/stoptimes/{trip_id}_{stop_sequence} | - | schema:Time | - | - |
| stop_times.csv departure_time | gtfs:departureTime | gtfs:StopTime | - | http://example.org/stoptimes/{trip_id}_{stop_sequence} | - | schema:Time | - | - |
| stop_times.csv stop_id | gtfs:stop | gtfs:StopTime | gtfs:Stop | http://example.org/stoptimes/{trip_id}_{stop_sequence} | stop_times.csv stop_id = stops.csv stop_id | - | - |  |
| stop_times.csv stop_sequence | gtfs:stopSequence | gtfs:StopTime | - | http://example.org/stoptimes/{trip_id}_{stop_sequence} | - | xsd:nonNegativeInteger | - | - |
| stop_times.csv stop_headsign | gtfs:headsign | gtfs:StopTime | - | http://example.org/stoptimes/{trip_id}_{stop_sequence} | - | xsd:string | capitalize | Input string in capital format |
| stop_times.csv shape_dist_traveled | gtfs:distanceTraveled | gtfs:StopTime | - | http://example.org/stoptimes/{trip_id}_{stop_sequence} | - | xsd:nonNegativeFloat | - | - |
| stop_times.csv pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | http://example.org/stoptimes/{trip_id}_{stop_sequence} | - | - | pickupSKOS | 0 -> http://transport.linkeddata.es/kos/pickup/available <br> 1 -> http://transport.linkeddata.es/kos/pickup/not-avaliable <br>  2 -> http://transport.linkeddata.es/kos/pickup/must-phone <br> 3 -> http://transport.linkeddata.es/kos/pickup/coordinate-with-driver |
| stop_times.csv drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | http://example.org/stoptimes/{trip_id}_{stop_sequence} | - | - | dropOffSKOS | 0 -> http://transport.linkeddata.es/kos/drop-off/available <br> 1 -> http://transport.linkeddata.es/kos/drop-off/not-available <br>  2 -> http://transport.linkeddata.es/kos/drop-off/must-phone <br> 3 -> http://transport.linkeddata.es/kos/drop-off/coordinate-with-driver |
