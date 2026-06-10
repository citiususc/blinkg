| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agency.csv agency_id | gtfs:id | gtfs:Agency | - | ex:agency/{agency_id} | - | xsd:string | - | - |
| agency.csv agency_name | gtfs:name | gtfs:Agency | - | ex:agency/{agency_id} | - | foaf:name | - | - |
| agency.csv agency_url | gtfs:url | gtfs:Agency | - | ex:agency/{agency_id} | - | foaf:page | - | - |
| agency.csv agency_timezone | gtfs:timezone | gtfs:Agency | - | ex:agency/{agency_id} | - | xsd:string | - | - |
| agency.csv agency_lang | gtfs:language | gtfs:Agency | - | ex:agency/{agency_id} | - | xsd:string | - | - |
| agency.csv agency_phone | gtfs:phoneNumber | gtfs:Agency | - | ex:agency/{agency_id} | - | foaf:phone | - |  |
| agency.csv agency_fare_url | gtfs:fareUrl | gtfs:Agency | - | ex:agency/{agency_id} | - | foaf:page | - | - |
| routes.csv route_id | gtfs:id | gtfs:Route | - | ex:route/{route_id} | - | xsd:string | - | - |
| routes.csv agency_id | gtfs:agency | gtfs:Route | gtfs:Agency | ex:route/{route_id} | routes.agency_id = agency.agency_id | - | - | - |
| routes.csv route_short_name | gtfs:shortName | gtfs:Route | - | ex:route/{route_id} | - | xsd:string | capitalize | Input string in capital format |
| routes.csv route_long_name | gtfs:longName | gtfs:Route | - | ex:route/{route_id} | - | xsd:string | capitalize | Input string in capital format |
| routes.csv route_desc | gtfs:desc | gtfs:Route | - | ex:route/{route_id} | - | xsd:string | - | - |
| routes.csv route_type | gtfs:routeType | gtfs:Route | skos:Concept | ex:route/{route_id} | - | - | routeTypeSKOS | 0->http://transport.linkeddata.es/kos/route-type/tram <br> 1 -> http://transport.linkeddata.es/kos/route-type/subway <br> 2 -> http://transport.linkeddata.es/kos/route-type/rail <br> 3 -> http://transport.linkeddata.es/kos/route-type/bus <br> 4 -> http://transport.linkeddata.es/kos/route-type/ferry <br> 5 -> http://transport.linkeddata.es/kos/route-type/cable-tram <br> 6 -> http://transport.linkeddata.es/kos/route-type/aerial-lift 7 -> http://transport.linkeddata.es/kos/route-type/funicular <br> 11 -> http://transport.linkeddata.es/kos/route-type/trolleybus <br> 12 -> http://transport.linkeddata.es/kos/route-type/monorail |
| routes.csv route_url | gtfs:url | gtfs:Route | - | ex:route/{route_id} | - | foaf:page | - | - |
| routes.csv route_color | gtfs:color | gtfs:Route | - | ex:route/{route_id} | - | xsd:string | - | - |
| routes.csv route_text_color | gtfs:textColor | gtfs:Route | - | ex:route/{route_id} | - | xsd:string | - | - |
| shapes.csv shape_id | gtfs:id | gtfs:Shape | - | ex:shape/{shape_id} | - | xsd:string | - |  |
| shapes.csv shape_pt_lat | gtfs:latitude | gtfs:ShapePoint | - | ex:shape/{shape_id}_{shape_pt_sequence} | - | geo:lat | - |  |
| shapes.csv shape_pt_lon | gtfs:longitude | gtfs:ShapePoint | - | ex:shape/{shape_id}_{shape_pt_sequence} | - | geo:lon | - |  |
| shapes.csv shape_pt_sequence | gtfs:pointSequence | gtfs:ShapePoint | - | ex:shape/{shape_id}_{shape_pt_sequence} | - | xsd:nonNegativeInteger | - |  |
| shapes.csv shape_dist_traveled | gtfs:distanceTraveled | gtfs:Shape | - | ex:shape/{shape_id} | - | gtfs:nonNegativeFloat | - |  |
| shapes.csv shape_id | gtfs:shapePoint | gtfs:Shape | gtfs:ShapePoint | ex:shape/{shape_id} | shapes.shape_id = shapes.shape_id | - | - |  |
| stops.csv stop_id | gtfs:id | gtfs:Location | - | ex:stop/{stop_id} | - | xsd:string | - |  |
| stops.csv stop_code | gtfs:code | gtfs:Location | - | ex:stop/{stop_id} | - | xsd:string | - |  |
| stops.csv stop_name | gtfs:name | gtfs:Location | - | ex:stop/{stop_id} | - | foaf:name | - |  |
| stops.csv stop_desc | gtfs:desc | gtfs:Location | - | ex:stop/{stop_id} | - | xsd:string | - |  |
| stops.csv stop_lat | gtfs:latitude | gtfs:Stop/gtfs:Station/gtfs:StationEntrance | - | ex:stop/{stop_id} | - | geo:lat | - |  |
| stops.csv stop_lon | gtfs:longitude | gtfs:Stop/gtfs:Station/gtfs:StationEntrance | - | ex:stop/{stop_id} | - | geo:lon | - |  |
| stops.csv stop_url | gtfs:url | gtfs:Location | - | ex:stop/{stop_id} | - | foaf:page | - |  |
| stops.csv stop_timezone | gtfs:timezone | gtfs:Location | - | ex:stop/{stop_id} | - | xsd:string | - |  |
| stops.csv location_type | gtfs:locationType | gtfs:Location | skos:Concept | ex:stop/{stop_id} | - | - | locationTypeSKOS | 0 -> http://transport.linkeddata.es/kos/location-type/stop <br> 1 -> http://transport.linkeddata.es/kos/location-type/station <br> 2 -> http://transport.linkeddata.es/kos/location-type/entrance-exit <br> 3 -> http://transport.linkeddata.es/kos/location-type/generic-node <br> 4 -> http://transport.linkeddata.es/kos/location-type/boarding-area |
| stops.csv parent_station | gtfs:parentStation | gtfs:Stop | gtfs:Station | ex:stop/{stop_id} | parent_station=stop_id | - | - |  |
| stops.csv wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Stop/gtfs:Station/gtfs:StationEntrance | skos:Concept | ex:stop/{stop_id} | - | - | wheelchairBoardingSKOS | 0 -> http://transport.linkeddata.es/kos/wheelchair-accesible/no-information <br> 1 -> http://transport.linkeddata.es/kos/wheelchair-accesible/accesible <br>  2 -> http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible |
| calendar.csv service_id | gtfs:id | gtfs:Service | - | ex:service/{service_id} | - | xsd:string | - | - |
| calendar.csv service_id | gtfs:serviceRule | gtfs:Service | gtfs:ServiceRule | ex:service/{service_id} | calendar.service_id=calendar.service_id or calendar_date.service_id=calendar_date.service_id | xsd:string | - | - |
| calendar.csv monday | gtfs:monday | gtfs:CalendarRule | skos:Concept | ex:rule/{service_id} | - | - | mapDayAvailability | 1 → <http://transport.linkeddata.es/kos/day/available><br>0 → <http://transport.linkeddata.es/kos/day/not-available> |
| calendar.csv tuesday | gtfs:tuesday | gtfs:CalendarRule | skos:Concept | ex:rule/{service_id} | - | - | mapDayAvailability | Same as above |
| calendar.csv wednesday | gtfs:wednesday | gtfs:CalendarRule | skos:Concept | ex:rule/{service_id} | - | - | mapDayAvailability | Same as above |
| calendar.csv thursday | gtfs:thursday | gtfs:CalendarRule | skos:Concept | ex:rule/{service_id} | - | - | mapDayAvailability | Same as above |
| calendar.csv friday | gtfs:friday | gtfs:CalendarRule | skos:Concept | ex:rule/{service_id} | - | - | mapDayAvailability | Same as above |
| calendar.csv saturday | gtfs:saturday | gtfs:CalendarRule | skos:Concept | ex:rule/{service_id} | - | - | mapDayAvailability | Same as above |
| calendar.csv sunday | gtfs:sunday | gtfs:CalendarRule | skos:Concept | ex:rule/{service_id} | - | - | mapDayAvailability | Same as above |
| calendar.csv start_date | gtfs:startDate | gtfs:CalendarRule | - | ex:rule/{service_id} | - | schema:startDate | - | - |
| calendar.csv end_date | gtfs:endDate | gtfs:CalendarRule | - | ex:rule/{service_id} | - | schema:endDate | - | - |
| calendar_dates.csv date | gtfs:date | gtfs:CalendarDateRule | - | ex:rule/{service_id}_{date} | - | xsd:date | - | - |
| calendar_dates.csv exception_type | gtfs:exceptionType | gtfs:CalendarDateRule | skos:Concept | ex:rule/{service_id}_{date} | - | - | mapExceptionType | 1 → <http://transport.linkeddata.es/kos/exception-type/removed><br>2 → <http://transport.linkeddata.es/kos/exception-type/added> |
| frequencies.csv trip_id | gtfs:trip | gtfs:Frequency | gtfs:Trip | ex:frequency/{trip_id}_{start_time} | trips.trip_id=frequency.trip_id | xsd:string | - | - |
| frequencies.csv start_time | gtfs:startTime | gtfs:Frequency | - | ex:frequency/{trip_id}_{start_time} | - | schema:startTime | - | - |
| frequencies.csv end_time | gtfs:endTime | gtfs:Frequency | - | ex:frequency/{trip_id}_{start_time} | - | schema:endTime | - | - |
| frequencies.csv headway_secs | gtfs:headwaySeconds | gtfs:Frequency | - | ex:frequency/{trip_id}_{start_time} | - | xsd:positiveInteger | - | - |
| frequencies.csv exact_times | gtfs:usesExactTimes | gtfs:Frequency | skos:Concept | ex:frequency/{trip_id}_{start_time} | - | - | directionSKOS | 0 -> http://transport.linkeddata.es/kos/direction/one-direction <br> 1 -> http://transport.linkeddata.es/kos/direction/opposite-direction |
| trips.csv trip_id | gtfs:id | gtfs:Trip | - | ex:trip/{trip_id} | - | xsd:string | - | - |
| trips.csv trip_headsign | gtfs:headsign | gtfs:Trip | - | ex:trip/{trip_id} | - | xsd:string | capitalize | Input string in capital format |
| trips.csv trip_short_name | gtfs:shortName | gtfs:Trip | - | ex:trip/{trip_id} | - | foaf:name | capitalize | Input string in capital format |
| trips.csv direction_id | gtfs:direction | gtfs:Trip | skos:Concept | ex:trip/{trip_id} | - | - | directionSKOS | 0 -> http://transport.linkeddata.es/kos/direction/one-direction <br> 1 -> http://transport.linkeddata.es/kos/direction/opposite-direction |
| trips.csv wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | ex:trip/{trip_id} | - | - | wheelchairBoardingSKOS | 0 -> http://transport.linkeddata.es/kos/wheelchair-accesible/no-information <br> 1 -> http://transport.linkeddata.es/kos/wheelchair-accesible/accesible <br>  2 -> http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible |
| trips.csv route_id | gtfs:route | gtfs:Trip | gtfs:Route | ex:trip/{trip_id} | trips.route_id=routes.route_id | xsd:string | - | - |
| trips.csv service_id | gtfs:service | gtfs:Trip | gtfs:Service | ex:trip/{trip_id} | trips.service_id=calendar.service_id or trips.service_id=calendar_dates.service_id | xsd:string | - | - |
| trips.csv trip_id | gtfs:id | gtfs:Trip | - | ex:trip/{trip_id} | - | xsd:string | - | - |
| trips.csv trip_headsign | gtfs:headsign | gtfs:Trip | - | ex:trip/{trip_id} | - | xsd:string | capitalize | Input string in capital format |
| trips.csv trip_short_name | gtfs:shortName | gtfs:Trip | - | ex:trip/{trip_id} | - | xsd:string | capitalize | Input string in capital format |
| trips.csv direction_id | gtfs:direction | gtfs:Trip | skos:Concept | ex:trip/{trip_id} | - | - | directionSKOS | 0 -> http://transport.linkeddata.es/kos/direction/one-direction <br> 1 -> http://transport.linkeddata.es/kos/direction/opposite-direction |
| trips.csv wheelchair_boarding | gtfs:wheelchairAccessible | gtfs:Trip | skos:Concept | ex:trip/{trip_id} | - | - | wheelchairBoardingSKOS | 0 -> http://transport.linkeddata.es/kos/wheelchair-accesible/no-information <br> 1 -> http://transport.linkeddata.es/kos/wheelchair-accesible/accesible <br>  2 -> http://transport.linkeddata.es/kos/wheelchair-accesible/inaccesible |
| stop_times.csv trip_id | gtfs:trip | gtfs:StopTime | gtfs:Trip | ex:stoptimes/{trip_id}_{stop_sequence} | stop_times.trip_id=trips.trip_id | - | - | - |
| stop_times.csv arrival_time | gtfs:arrivalTime | gtfs:StopTime | - | ex:stoptimes/{trip_id}_{stop_sequence} | - | schema:Time | - | - |
| stop_times.csv stop_sequence | gtfs:departureTime | gtfs:StopTime | - | ex:stoptimes/{trip_id}_{stop_sequence} | - | schema:Time | - | - |
| stop_times.csv stop_id | gtfs:stop | gtfs:StopTime | gtfs:Stop | ex:stoptimes/{trip_id}_{stop_sequence} | stop_times.stop_id=stops.stop_id | - | - |  |
| stop_times.csv departure_time | gtfs:stopSequence | gtfs:StopTime | - | ex:stoptimes/{trip_id}_{stop_sequence} | - | xsd:nonNegativeInteger | - | - |
| stop_times.csv stop_headsign | gtfs:headsign | gtfs:StopTime | - | ex:stoptimes/{trip_id}_{stop_sequence} | - | xsd:string | capitalize | Input string in capital format |
| stop_times.csv shape_dist_traveled | gtfs:distancedTraveled | gtfs:StopTime | - | ex:stoptimes/{trip_id}_{stop_sequence} | - | xsd:nonNegativeFloat | - | - |
| stop_times.csv pickup_type | gtfs:pickupType | gtfs:StopTime | skos:Concept | ex:stoptimes/{trip_id}_{stop_sequence} | - | - | pickupSKOS | 0 -> http://transport.linkeddata.es/kos/pickup/available <br> 1 -> http://transport.linkeddata.es/kos/pickup/not-avaliable <br>  2 -> http://transport.linkeddata.es/kos/pickup/must-phone <br> 3 -> http://transport.linkeddata.es/kos/pickup/coordinate-with-driver |
| stop_times.csv drop_off_type | gtfs:dropOffType | gtfs:StopTime | skos:Concept | ex:stoptimes/{trip_id}_{stop_sequence} | - | - | dropOffSKOS | 0 -> http://transport.linkeddata.es/kos/drop-off/available <br> 1 -> http://transport.linkeddata.es/kos/drop-off/not-available <br>  2 -> http://transport.linkeddata.es/kos/drop-off/must-phone <br> 3 -> http://transport.linkeddata.es/kos/drop-off/coordinate-with-driver |
