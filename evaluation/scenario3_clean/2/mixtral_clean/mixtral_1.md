| XML Path | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| id | hasID | Procurement Object | Identifier | URI(prefix, input.id) |  | - |  |  |
| link | address | Procurement Object | Address | URI(prefix, input.link) |  | - |  |  |
| summary/text | hasAwardDecisionDate | LotAwardOutcome | Date | f.parseDate(input.summary.text) | f.matches('Órgano de Contratación: (.+); Importe: (.+) EUR; Estado: (.+)', input.summary.text) | Date | - | - |
| summary/text | hasProcurementScopeDividedIntoLot | Procedure | Lot | input.id | f.matches('Órgano de Contratación: (.+); Importe: (.+) EUR; Estado: (.+)', input.summary.text) | - |  |  |
| summary/text | hasReceivedTenders | SubmissionStatisticalInformation | Integer | (input.summary.text, 'Importe: (.+) EUR') | f.matches('Órgano de Contratación: (.+); Importe: (.+) EUR; Estado: (.+)', input.summary.text) | Integer | -|  |
| title |  |  |  |  |  |  |  |  |
| updated | hasDispatchDate | Procurement Object | Date | f.parseDate(input.updated) | true | Date | - | -|
| cac:place-ext:ContractFolderStatus/cbc:ContractFolderID |  |  |  |  |  |  |  |  |
| cac:place-ext:ContractFolderStatus/cbc-place-ext:ContractFolderStatusCode |  |  |  |  |  |  |  |  |
| cac:Contract/cbc:ID | hasProcedureType | Procedure | Identifier |  | input.id | - |  |  |
| cac:Party/cac:PartyIdentification/cbc:ID[@schemeName='DIR3'] | hasID | PrimaryRole | Identifier |  |  | - |  |  |
| cac:Party/cac:PartyIdentification/cbc:ID[@schemeName='NIF'] | hasID | PrimaryRole | Identifier |  |  | - |  |  |
| cac:Party/cac:PartyName/cbc:Name |  |  |  |  |  |  |  |  |
| cac:Party/cac:PostalAddress/cbc:CityName | address | Address | Country | URI(prefix, input.party.address.cityName) | f.matches('ódigo de país: (.+)', input.party.address.country.identificationCode) | - |  | - |
| cac:Party/cac:PostalAddress/cbc:PostalZone |  |  |  |  |  |  |  |  |
| cac:Party/cac:PostalAddress/cac:AddressLine/cbc:Line |  |  |  |  |  |  |  |  |
| cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode | hasCountryCode | Country | Identifier | input.party.address.country.identificationCode | f.matches('ódigo de país: (.+)', input.party.address.country.identificationCode) | - |  | - |
| cac:Party/cac:PostalAddress/cac:Country/cbc:Name |  |  |  |  |  |  |  |  |
| cac:ProcurementProject/cbc:Name |  |  |  |  |  |  |  |  |
| cac:ProcurementProject/cbc:TypeCode |  |  |  |  |  |  |  |  |
| cac:ProcurementProject/cbc:SubTypeCode | hasProcurementObjectType | Procurement Object | Identifier | URI(prefix, input.project.typeCode) | f.matches('Tipo: (.+)', input.project.typeCode) | - |  |  |
| cac:BudgetAmount/cbc:EstimatedOverallContractAmount |  |  |  |  |  |  |  |  |
| cac:BudgetAmount/cbc:TotalAmount |  |  |  |  |  |  |  |  |
| cac:BudgetAmount/cbc:TaxExclusiveAmount |  |  |  |  |  |  |  |  |
| cac:BudgetAmount/cbc:Currency |  |  |  |  |  |  |  |  |
| cac:BudgetAmount/cbc:EstimatedOverallContractAmount | hasEstimatedValue | Procurement Object | Decimal | input.project.budget.estimatedOverallContractAmount |  | Decimal |  |  |
| cac:BudgetAmount/cbc:TotalAmount | hasActualValue | Procurement Object | Decimal | input.project.budget.totalAmount |  | Decimal |  |  |
| cac:BudgetAmount/cbc:TaxExclusiveAmount |  |  |  |  |  |  |  |  |
| cac:ProcurementProject/cac:RequiredCommodityClassification/cbc:ItemClassificationCode | hasCPVcode | Procurement Object | Identifier | URI(prefix, input.project.cpvCode) | f.matches('- (.+)', input.project.cpvCode) | - |  | - |
| cac:ProcurementProject/cac:RequiredCommodityClassification/... | hasCPVcode | Procurement Object | Identifier | input.project.cpvCode | f.matches('- (.+)', input.project.cpvCode) | - |  | - |
| cac:P |  |  |  |  |  |  |  |  |
| cbc:F |  |  |  |  |  |  |  |  |
| cbc:CityName | address | Address | Country | URI(prefix, input.project.location.cityName) | f.matches('Código de país: (.+)', input.project.location.country.identificationCode) | - |  | - |
| cac:PostalZone |  |  |  |  |  |  |  |  |
| cac:Country/cbc:IdentificationCode | hasCountryCode | Country | Identifier | input.project.location.country.identificationCode | f.matches('Código de país: (.+)', input.project.location.country.identificationCode) | - |  | - |
							
