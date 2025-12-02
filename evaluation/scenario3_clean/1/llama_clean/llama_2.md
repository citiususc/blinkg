| XML Path | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /entry/id | :hasID | :ProcurementObject |  | uuid() |  | string |  | <uuid> |
| /entry/summary | :hasDescription | :ProcurementObject |  | concat("Summary: ", /entry/summary) |  | string |  | |
| /entry/title | :hasTitle | :ProcurementObject |  | /entry/title |  | string |  |  |
| /entry/updated | :hasDispatchDate | :Document |  | /entry/updated |  | dateTime |  | |
| /cac-place-ext:ContractFolderStatus/cbc:ContractFolderID | :hasID | :ContractFolder |  | /cac-place-ext:ContractFolderStatus/cbc:ContractFolderID |  |  |  | |
| /cac-place-ext:ContractFolderStatus/cbc-place-ext:ContractFolderStatusCode | :hasStatusCode | :ContractFolderStatus | :ContractFolder | /cac-place-ext:ContractFolderStatus/cbc-place-ext:ContractFolderStatusCode |  |  |  | |
| /cac-place-ext:LocatedContractingParty/cbc:ContractingPartyTypeCode | :hasTypeCode | :ContractingParty | :LocatedContractingParty | /cac-place-ext:LocatedContractingParty/cbc:ContractingPartyTypeCode |  |  |  | |
| /cac-place-ext:LocatedContractingParty/cac:Party/cbc:ID | :hasID | :Party | :LocatedContractingParty | /cac-place-ext:LocatedContractingParty/cac:Party/cbc:ID |  |  |  | |
| /cac-place-ext:LocatedContractingParty/cac:Party/cbc:Name | :hasName | :Party | :LocatedContractingParty | /cac-place-ext:LocatedContractingParty/cac:Party/cbc:Name |  |  |  |  |
| /cac-place-ext:LocatedContractingParty/cac:PostalAddress/cbc:CityName | :hasCityName | :PostalAddress | :LocatedContractingParty | /cac-place-ext:LocatedContractingParty/cac:PostalAddress/cbc:CityName |  |  |  |  |
| /cac-place-ext:LocatedContractingParty/cac:PostalAddress/cbc:PostalZone | :hasPostalZone | :PostalAddress | :LocatedContractingParty | /cac-place-ext:LocatedContractingParty/cac:PostalAddress/cbc:PostalZone |  |  |  |  |
| /cac-place-ext:LocatedContractingParty/cac:Country/cbc:IdentificationCode | :hasCountryCode | :Country | :LocatedContractingParty | /cac-place-ext:LocatedContractingParty/cac:Country/cbc:IdentificationCode |  | string |  | country_code |
| /cac-place-ext:ParentLocatedParty/cac:PartyName/cbc:Name | :hasName | :Party | :ParentLocatedParty | /cac-place-ext:ParentLocatedParty/cac:PartyName/cbc:Name |  |  |  |  |
| /cac:ProcurementProject/cbc:Name | :hasName | :ProcurementProject |  | /cac:ProcurementProject/cbc:Name |  | string |  |  |
| /cac:ProcurementProject/cbc:TypeCode | :hasTypeCode | :ProcurementProject |  | /cac:ProcurementProject/cbc:TypeCode |  | string |  | |
| /cac:BudgetAmount/cbc:EstimatedOverallContractAmount | :hasEstimatedAmount | :BudgetAmount | :ProcurementProject | /cac:BudgetAmount/cbc:EstimatedOverallContractAmount |  |  |  | |
| /cac:RequiredCommodityClassification/cbc:ItemClassificationCode | :hasItemClassificationCode | :RequiredCommodityClassification | :ProcurementProject | /cac:RequiredCommodityClassification/cbc:ItemClassificationCode |  |  |  | |
| /cac:RealizedLocation/cbc:CountrySubentity | :hasCountrySubentity | :RealizedLocation | :ProcurementProject | /cac:RealizedLocation/cbc:CountrySubentity |  |  |  | |
| /cac:RealizedLocation/cbc:CountrySubentityCode | :hasCountrySubentityCode | :RealizedLocation | :ProcurementProject | /cac:RealizedLocation/cbc:CountrySubentityCode |  |  |  | |
| /cac:TenderResult/cbc:ResultCode | :hasResultCode | :TenderResult | :ProcurementProject | /cac:TenderResult/cbc:ResultCode |  |  |  | |
| /cac:TenderResult/cbc:AwardDate | :hasAwardDate | :TenderResult | :ProcurementProject | /cac:TenderResult/cbc:AwardDate |  | dateTime |  | |
| /cac:WinningParty/cac:PartyIdentification/cbc:ID | :hasID | :WinningParty | :TenderResult | /cac:WinningParty/cac:PartyIdentification/cbc:ID |  |  |  | |
| /cac:WinningParty/cac:PartyName/cbc:Name | :hasName | :WinningParty | :TenderResult | /cac:WinningParty/cac:PartyName/cbc:Name |  |  |  |  |
| /cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount | :hasTaxExclusiveAmount | :AwardedTenderedProject | :TenderResult | /cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount |  |  |  | |
| /cac:TenderingTerms/cbc:RequiredCurriculaIndicator | :hasRequiredCurriculaIndicator | :TenderingTerms | :ProcurementProject | /cac:TenderingTerms/cbc:RequiredCurriculaIndicator |  |  |  |  |
| /cac:TenderingProcess/cbc:ProcedureCode | :hasProcedureCode | :TenderingProcess | :ProcurementProject | /cac:TenderingProcess/cbc:ProcedureCode |  | |  | code |
| /cac-place-ext:ValidNoticeInfo/cbc-place-ext:NoticeTypeCode | :hasNoticeTypeCode | :ValidNoticeInfo | :ProcurementProject | /cac-place-ext:ValidNoticeInfo/cbc-place-ext:NoticeTypeCode |  | string |  |  |
