| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /entry/id | :hasID | :ResultNotice | :Identifier | `CONCAT("https://contrataciondelestado.es/notice/", SUBSTRING_AFTER(/, 'licitacionesPerfilContratante/'))` | Identifier.value = id text | - | - | - |
| /entry/id | :hasIdentifierValue | :Identifier | - | `CONCAT(notice_uri, "#identifier")` | - | xsd:anyURI | - | - |
| /entry/updated | :hasDispatchDate | :ResultNotice | - | notice_uri | - | xsd:dateTime | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cbc:ContractFolderID | :hasID | :Lot | :Identifier | `CONCAT(notice_uri, "#lot")` | Identifier.value = ContractFolderID text | - | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cbc:ContractFolderID | :hasIdentifierValue | :Identifier | - | `CONCAT(lot_uri, "#id")` | - | xsd:string | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cac:TenderingProcess/cbc:ProcedureCode | :hasProcedureType | :Procedure | skos:Concept | `CONCAT(notice_uri, "#procedure")` | - | - | MapProcedureCode | `"http://publications.europa.eu/resource/authority/procurement-procedure-type/open"` (1→open) |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyIdentification/cbc:ID | :hasID | org:Organization | :Identifier | `CONCAT("http://example.com/org/", @schemeName, "/", text())` | Identifier.value = ID text | - | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyName/cbc:Name | foaf:name | org:Organization | - | org_uri | - | xsd:string | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode | :hasCountryCode | org:Organization | skos:Concept | org_uri | - | - | MapCountryCode | `"http://publications.europa.eu/resource/authority/country/ESP"` (ES→ESP) |
| /entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cbc:AwardDate | :hasAwardDecisionDate | :LotAwardOutcome | - | `CONCAT(notice_uri, "#award")` | - | xsd:date | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cbc:ReceivedTenderQuantity | :hasReceivedTenders | :SubmissionStatisticalInformation | - | `CONCAT(notice_uri, "#stats")` | - | xsd:integer | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cbc:Name | dcterms:title | :Lot | - | lot_uri | - | xsd:string | - | - |
| - | :refersToRole | :ResultNotice | :Buyer | notice_uri | Buyer.organization = org_uri | - | - | - |
| - | :playedByOrganization | :Buyer | org:Organization | `CONCAT(notice_uri, "#buyer-role")` | - | - | - | - |
| - | :hasProcurementScopeDividedIntoLot | :Procedure | :Lot | procedure_uri | - | - | - | - |
| - | :describesLot | :LotAwardOutcome | :Lot | award_uri | - | - | - | - |
| - | :concernsSubmissionsForLot | :SubmissionStatisticalInformation | :Lot | stats_uri | - | - | - | - |
