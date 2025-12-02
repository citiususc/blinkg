| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /entry/id | :hasID | :ProcurementObject |  | concat("https://contrataciondelestado.es/sindicacion/licitacionesPerfilContratante/", ./id) |  | string |  | "https://contrataciondelestado.es/sindicacion/licitacionesPerfilContratante/6854467" |
| /entry/summary | :describesLot | :LotAwardOutcome | :Lot | ./summary | ./lot = ./summary/@lot | string |  | "Suministro de piezas de recambio originales para equipos mecánicos y eléctricos de EMAYA." |
| /entry/title | :hasIdentifierValue | :Identifier | :ProcurementObject | ./title | ./title = ./procurementObject/@title | string |  | "Suministro de piezas de recambio originales para equipos mecánicos y eléctricos de EMAYA." |
| /entry/updated | :hasDispatchDate | :Document | :Notice | ./updated | ./updated = ./notice/@updated | dateTime |  | "2021-01-07T10:47:01.782+01:00" |
| /cac-place-ext:ContractFolderStatus/cbc:ContractFolderID | :hasID | :ProcurementObject |  | ./cbc:ContractFolderID |  | string |  | "942P LOTE 2" |
| /cac-place-ext:ContractFolderStatus/cbc-place-ext:ContractFolderStatusCode | :hasProcurementScopeDividedIntoLot | :Procedure | :Lot | ./cbc-place-ext:ContractFolderStatusCode | ./procedure = ./lot/@procedure | string |  | "RES" |
| /cac-place-ext:LocatedContractingParty/cbc:ContractingPartyTypeCode | :playedByOrganisation | :Buyer | :Organization | ./cbc:ContractingPartyTypeCode | ./buyer = ./organization/@buyer | string | getBuyerType | "5" |
| /cac-place-ext:LocatedContractingParty/cac:Party/cbc:WebsiteURI | :address | :Organization |  | ./cbc:WebsiteURI |  | string |  | "http://www.emaya.es" |
| /cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyIdentification/cbc:ID | :hasIdentifierValue | :Identifier | :Organization | ./cbc:ID | ./organization = ./identifier/@organization | string |  | "A07000029" |
| /cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyName/cbc:Name | :hasIdentifierValue | :Identifier | :Organization | ./cbc:Name | ./organization = ./identifier/@organization | string |  | "Gerencia de EMAYA, Empresa Municipal d'Aigües i Clavegueram, S.A." |
| /cac-place-ext:LocatedContractingParty/cac:PostalAddress/cbc:CityName | :address | :Organization |  | ./cbc:CityName |  | string |  | "Palma" |
| /cac-place-ext:LocatedContractingParty/cac:PostalAddress/cbc:PostalZone | :address | :Organization |  | ./cbc:PostalZone |  | string |  | "07010" |
| /cac-place-ext:LocatedContractingParty/cac:Country/cbc:IdentificationCode | :hasCountryCode | :Country | :Organization | ./cbc:IdentificationCode | ./country = ./organization/@country | string | getCountryCode | "ES" |
| /cac-place-ext:LocatedContractingParty/cac:Contact/cbc:Name | :playedBy | :AgentInRole | :Contact | ./cbc:Name | ./contact = ./agentInRole/@contact | string |  | "Gerencia de EMAYA, Empresa Municipal d'Aigües i Clavegueram, S.A." |
| /cac-place-ext:ParentLocatedParty/cac:PartyName/cbc:Name | :playedBy | :AgentInRole | :Contact | ./cbc:Name | ./contact = ./agentInRole/@contact | string |  | "EMAYA, Empresa Municipal d'Aigües i Clavegueram, S.A." |
| /cac:ProcurementProject/cbc:Name | :hasIdentifierValue | :Identifier | :ProcurementObject | ./cbc:Name | ./procurementObject = ./identifier/@procurementObject | string |  | "Suministro de piezas de recambio originales para equipos mecánicos y eléctricos de EMAYA." |
| /cac:ProcurementProject/cbc:TypeCode | :hasProcedureType | :Procedure | :ProcurementObject | ./cbc:TypeCode | ./procedure = ./procurementObject/@procedure | string | getProcedureType | "1" |
| /cac:BudgetAmount/cbc:EstimatedOverallContractAmount | :hasReceivedTenders | :SubmissionStatisticalInformation | :Lot | ./cbc:EstimatedOverallContractAmount | ./submission = ./lot/@submission | decimal |  | "115989.14" |
| /cac:RequiredCommodityClassification/cbc:ItemClassificationCode | :concernsSubmissionsForLot | :SubmissionStatisticalInformation | :Lot | ./cbc:ItemClassificationCode | ./submission = ./lot/@submission | string | getItemClassification | "31681000" |
| /cac:RealizedLocation/cbc:CountrySubentity | :hasCountryCode | :Country | :Organization | ./cbc:CountrySubentity | ./country = ./organization/@country | string | getCountrySubentity | "Mallorca" |
| /cac:PlannedPeriod/cbc:DurationMeasure | :hasDispatchDate | :Document | :Notice | ./cbc:DurationMeasure | ./notice = ./document/@notice | integer |  | "1" |
| /cac:TenderResult/cbc:ResultCode | :hasAwardDecisionDate | :LotAwardOutcome | :Lot | ./cbc:ResultCode | ./lotAwardOutcome = ./lot/@lotAwardOutcome | string | getAwardDecision | "8" |
| /cac:TenderResult/cbc:AwardDate | :hasAwardDecisionDate | :LotAwardOutcome | :Lot | ./cbc:AwardDate | ./lotAwardOutcome = ./lot/@lotAwardOutcome | dateTime |  | "2021-01-04" |
| /cac:TenderResult/cac:Contract/cbc:ID | :hasID | :ProcurementObject |  | ./cbc:ID |  | string |  | "ID 2534" |
| /cac:WinningParty/cac:PartyIdentification/cbc:ID | :hasIdentifierValue | :Identifier | :Organization | ./cbc:ID | ./organization = ./identifier/@organization | string |  | "A28388023" |
| /cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount | :hasReceivedTenders | :SubmissionStatisticalInformation | :Lot | ./cbc:TaxExclusiveAmount | ./submission = ./lot/@submission | decimal |  | "96657.62" |
| /cac:TenderingTerms/cbc:RequiredCurriculaIndicator | :usesTechnique | :TechniqueUsage | :Procedure | ./cbc:RequiredCurriculaIndicator | ./technique = ./procedure/@technique | boolean |  | "false" |
| /cac:TenderingTerms/cac:ProcurementLegislationDocumentReference/cbc:ID | :hasProcedureType | :Procedure | :ProcurementObject | ./cbc:ID | ./procedure = ./procurementObject/@procedure | string | getProcurementLegislation | "2014/24/EU" |
| /cac:TenderingProcess/cbc:ProcedureCode | :hasProcedureType | :Procedure | :ProcurementObject | ./cbc:ProcedureCode | ./procedure = ./procurementObject/@procedure | string | getProcedureCode | "1" |
| /cac-place-ext:ValidNoticeInfo/cbc-place-ext:NoticeTypeCode | :refersToRole | :ResultNotice | :Notice | ./cbc-place-ext:NoticeTypeCode | ./resultNotice = ./notice/@resultNotice | string | getNoticeType | "DOC_CAN_ADJ" |
