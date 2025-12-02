| XML Path | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /entry/id | :hasID | :ProcurementObject |  | concat("https://contrataciondelestado.es/sindicacion/licitacionesPerfilContratante/", ./id) |  | string |  ||
| /entry/summary | :describesLot | :LotAwardOutcome | :Lot | ./summary | ./lot = ./summary/@lot |  |  |  |
| /entry/title | :hasIdentifierValue | :Identifier | :ProcurementObject | ./title | ./title = ./procurementObject/@title | |  |  |
| /entry/updated | :hasDispatchDate | :Document | :Notice | ./updated | ./updated = ./notice/@updated |  |  | |
| /cac-place-ext:ContractFolderStatus/cbc:ContractFolderID | :hasID | :ProcurementObject |  | ./cbc:ContractFolderID |  | string |  | |
| /cac-place-ext:ContractFolderStatus/cbc-place-ext:ContractFolderStatusCode | :hasProcurementScopeDividedIntoLot | :Procedure | :Lot | ./cbc-place-ext:ContractFolderStatusCode | ./procedure = ./lot/@procedure | |  |  |
| /cac-place-ext:LocatedContractingParty/cbc:ContractingPartyTypeCode | :playedByOrganisation | :Buyer | :Organization | ./cbc:ContractingPartyTypeCode | ./buyer = ./organization/@buyer | | getBuyerType | takes a string as input and returns the corresponding buyer type |
| /cac-place-ext:LocatedContractingParty/cac:Party/cbc:WebsiteURI | :address | :Organization |  | ./cbc:WebsiteURI |  |  |  | |
| /cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyIdentification/cbc:ID | :hasIdentifierValue | :Identifier | :Organization | ./cbc:ID | ./organization = ./identifier/@organization |  |  |  |
| /cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyName/cbc:Name | :hasIdentifierValue | :Identifier | :Organization | ./cbc:Name | ./organization = ./identifier/@organization |  |  | |
| /cac-place-ext:LocatedContractingParty/cac:PostalAddress/cbc:CityName | :address | :Organization |  | ./cbc:CityName |  | string |  | |
| /cac-place-ext:LocatedContractingParty/cac:PostalAddress/cbc:PostalZone | :address | :Organization |  | ./cbc:PostalZone |  | string |  | |
| /cac-place-ext:LocatedContractingParty/cac:Country/cbc:IdentificationCode | :hasCountryCode | :Country | :Organization | ./cbc:IdentificationCode | ./country = ./organization/@country | string | getCountryCode | takes a string as input and returns the corresponding country code |
| /cac-place-ext:LocatedContractingParty/cac:Contact/cbc:Name | :playedBy | :AgentInRole | :Contact | ./cbc:Name | ./contact = ./agentInRole/@contact |  |  | |
| /cac-place-ext:ParentLocatedParty/cac:PartyName/cbc:Name | :playedBy | :AgentInRole | :Contact | ./cbc:Name | ./contact = ./agentInRole/@contact |  |  |  |
| /cac:ProcurementProject/cbc:Name | :hasIdentifierValue | :Identifier | :ProcurementObject | ./cbc:Name | ./procurementObject = ./identifier/@procurementObject | | | |
| /cac:ProcurementProject/cbc:TypeCode | :hasProcedureType | :Procedure | :ProcurementObject | ./cbc:TypeCode | ./procedure = ./procurementObject/@procedure | | getProcedureType | takes a string as input and returns the corresponding procedure type |
| /cac:BudgetAmount/cbc:EstimatedOverallContractAmount | :hasReceivedTenders | :SubmissionStatisticalInformation | :Lot | ./cbc:EstimatedOverallContractAmount | ./submission = ./lot/@submission |decimal | | |
| /cac:RequiredCommodityClassification/cbc:ItemClassificationCode | :concernsSubmissionsForLot | :SubmissionStatisticalInformation | :Lot | ./cbc:ItemClassificationCode | ./submission = ./lot/@submission | | | |
| /cac:RealizedLocation/cbc:CountrySubentity | :hasCountryCode | :Country | :Organization | ./cbc:CountrySubentity | ./country = ./organization/@country | | | |
| /cac:PlannedPeriod/cbc:DurationMeasure | :hasDispatchDate | :Document | :Notice | ./cbc:DurationMeasure | ./notice = ./document/@notice | |  | |
| /cac:TenderResult/cbc:ResultCode | :hasAwardDecisionDate | :LotAwardOutcome | :Lot | ./cbc:ResultCode | ./lotAwardOutcome = ./lot/@lotAwardOutcome | string | | |
| /cac:TenderResult/cbc:AwardDate | :hasAwardDecisionDate | :LotAwardOutcome | :Lot | ./cbc:AwardDate | ./lotAwardOutcome = ./lot/@lotAwardOutcome | dateTime	 | |
| /cac:TenderResult/cac:Contract/cbc:ID | :hasID | :ProcurementObject |  | ./cbc:ID |  | string |  | |
| /cac:WinningParty/cac:PartyIdentification/cbc:ID | :hasIdentifierValue | :Identifier | :Organization | ./cbc:ID | ./organization = ./identifier/@organization | |  | |
| /cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount | :hasReceivedTenders | :SubmissionStatisticalInformation | :Lot | ./cbc:TaxExclusiveAmount | ./submission = ./lot/@submission |decimal| | |
| /cac:TenderingTerms/cbc:RequiredCurriculaIndicator | :usesTechnique | :TechniqueUsage | :Procedure | ./cbc:RequiredCurriculaIndicator | ./technique = ./procedure/@technique | | | |
| /cac:TenderingTerms/cac:ProcurementLegislationDocumentReference/cbc:ID | :hasProcedureType | :Procedure | :ProcurementObject | ./cbc:ID | ./procedure = ./procurementObject/@procedure |  | | |
| /cac:TenderingProcess/cbc:ProcedureCode | :hasProcedureType | :Procedure | :ProcurementObject | ./cbc:ProcedureCode | ./procedure = ./procurementObject/@procedure | | getProcedureCode | takes a string as input and returns the corresponding procedure code |
| /cac-place-ext:ValidNoticeInfo/cbc-place-ext:NoticeTypeCode | :refersToRole | :ResultNotice | :Notice | ./cbc-place-ext:NoticeTypeCode | ./resultNotice = ./notice/@resultNotice |  | | |

