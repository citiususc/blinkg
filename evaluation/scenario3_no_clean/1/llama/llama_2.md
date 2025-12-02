| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /entry/id | :hasID | :ProcurementObject |  | uuid() |  | string |  | urn:uuid:<uuid> |
| /entry/summary | :hasDescription | :ProcurementObject |  | concat("Summary: ", /entry/summary) |  | string |  | Summary: <text> |
| /entry/title | :hasTitle | :ProcurementObject |  | /entry/title |  | string |  | <text> |
| /entry/updated | :hasDispatchDate | :Document |  | /entry/updated |  | dateTime |  | <datetime> |
| /cac-place-ext:ContractFolderStatus/cbc:ContractFolderID | :hasID | :ContractFolder |  | /cac-place-ext:ContractFolderStatus/cbc:ContractFolderID |  | string |  | <id> |
| /cac-place-ext:ContractFolderStatus/cbc-place-ext:ContractFolderStatusCode | :hasStatusCode | :ContractFolderStatus | :ContractFolder | /cac-place-ext:ContractFolderStatus/cbc-place-ext:ContractFolderStatusCode |  | string |  | <code> |
| /cac-place-ext:LocatedContractingParty/cbc:ContractingPartyTypeCode | :hasTypeCode | :ContractingParty | :LocatedContractingParty | /cac-place-ext:LocatedContractingParty/cbc:ContractingPartyTypeCode |  | string |  | <code> |
| /cac-place-ext:LocatedContractingParty/cac:Party/cbc:ID | :hasID | :Party | :LocatedContractingParty | /cac-place-ext:LocatedContractingParty/cac:Party/cbc:ID |  | string |  | <id> |
| /cac-place-ext:LocatedContractingParty/cac:Party/cbc:Name | :hasName | :Party | :LocatedContractingParty | /cac-place-ext:LocatedContractingParty/cac:Party/cbc:Name |  | string |  | <name> |
| /cac-place-ext:LocatedContractingParty/cac:PostalAddress/cbc:CityName | :hasCityName | :PostalAddress | :LocatedContractingParty | /cac-place-ext:LocatedContractingParty/cac:PostalAddress/cbc:CityName |  | string |  | <city> |
| /cac-place-ext:LocatedContractingParty/cac:PostalAddress/cbc:PostalZone | :hasPostalZone | :PostalAddress | :LocatedContractingParty | /cac-place-ext:LocatedContractingParty/cac:PostalAddress/cbc:PostalZone |  | string |  | <zip> |
| /cac-place-ext:LocatedContractingParty/cac:Country/cbc:IdentificationCode | :hasCountryCode | :Country | :LocatedContractingParty | /cac-place-ext:LocatedContractingParty/cac:Country/cbc:IdentificationCode |  | string |  | <country_code> |
| /cac-place-ext:ParentLocatedParty/cac:PartyName/cbc:Name | :hasName | :Party | :ParentLocatedParty | /cac-place-ext:ParentLocatedParty/cac:PartyName/cbc:Name |  | string |  | <name> |
| /cac:ProcurementProject/cbc:Name | :hasName | :ProcurementProject |  | /cac:ProcurementProject/cbc:Name |  | string |  | <name> |
| /cac:ProcurementProject/cbc:TypeCode | :hasTypeCode | :ProcurementProject |  | /cac:ProcurementProject/cbc:TypeCode |  | string |  | <code> |
| /cac:BudgetAmount/cbc:EstimatedOverallContractAmount | :hasEstimatedAmount | :BudgetAmount | :ProcurementProject | /cac:BudgetAmount/cbc:EstimatedOverallContractAmount |  | decimal |  | <amount> |
| /cac:RequiredCommodityClassification/cbc:ItemClassificationCode | :hasItemClassificationCode | :RequiredCommodityClassification | :ProcurementProject | /cac:RequiredCommodityClassification/cbc:ItemClassificationCode |  | string |  | <code> |
| /cac:RealizedLocation/cbc:CountrySubentity | :hasCountrySubentity | :RealizedLocation | :ProcurementProject | /cac:RealizedLocation/cbc:CountrySubentity |  | string |  | <subentity> |
| /cac:RealizedLocation/cbc:CountrySubentityCode | :hasCountrySubentityCode | :RealizedLocation | :ProcurementProject | /cac:RealizedLocation/cbc:CountrySubentityCode |  | string |  | <code> |
| /cac:TenderResult/cbc:ResultCode | :hasResultCode | :TenderResult | :ProcurementProject | /cac:TenderResult/cbc:ResultCode |  | string |  | <code> |
| /cac:TenderResult/cbc:AwardDate | :hasAwardDate | :TenderResult | :ProcurementProject | /cac:TenderResult/cbc:AwardDate |  | dateTime |  | <datetime> |
| /cac:WinningParty/cac:PartyIdentification/cbc:ID | :hasID | :WinningParty | :TenderResult | /cac:WinningParty/cac:PartyIdentification/cbc:ID |  | string |  | <id> |
| /cac:WinningParty/cac:PartyName/cbc:Name | :hasName | :WinningParty | :TenderResult | /cac:WinningParty/cac:PartyName/cbc:Name |  | string |  | <name> |
| /cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount | :hasTaxExclusiveAmount | :AwardedTenderedProject | :TenderResult | /cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount |  | decimal |  | <amount> |
| /cac:TenderingTerms/cbc:RequiredCurriculaIndicator | :hasRequiredCurriculaIndicator | :TenderingTerms | :ProcurementProject | /cac:TenderingTerms/cbc:RequiredCurriculaIndicator |  | boolean |  | true/false |
| /cac:TenderingProcess/cbc:ProcedureCode | :hasProcedureCode | :TenderingProcess | :ProcurementProject | /cac:TenderingProcess/cbc:ProcedureCode |  | string |  | <code> |
| /cac-place-ext:ValidNoticeInfo/cbc-place-ext:NoticeTypeCode | :hasNoticeTypeCode | :ValidNoticeInfo | :ProcurementProject | /cac-place-ext:ValidNoticeInfo/cbc-place-ext:NoticeTypeCode |  | string |  | <code> |
