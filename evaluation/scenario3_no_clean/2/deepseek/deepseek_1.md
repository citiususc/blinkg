| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `/entry/id` | `dcterms:identifier` | `:ResultNotice` |  | Value of `/entry/id` |  | `xsd:anyURI` |  |  |
| `/entry/updated` | `:hasDispatchDate` | `:ResultNotice` |  | Value of `/entry/id` |  | `xsd:dateTime` |  |  |
| `//cbc:ContractFolderID` | `:hasID` | `:Procedure` |  | `concat("https://contrataciondelestado.es/procedure/", text())` |  |  |  |  |
| `//cbc-place-ext:ContractFolderStatusCode` | `:hasProcedureType` | `:Procedure` |  | `concat("https://contrataciondelestado.es/procedure/", ../cbc:ContractFolderID)` |  |  | `mapStatusCode` | SKOS concept from `procurement-procedure-type` scheme |
| `//cac:Party/cbc:Name` | `foaf:name` | `org:Organization` |  | `concat("http://data.europa.eu/a4g/agent/", PartyIdentification[1]/cbc:ID)` |  | `xsd:string` |  |  |
| `//cac:Party/cac:PartyIdentification[cbc:ID/@schemeName="DIR3"]/cbc:ID` | `:hasIdentifierValue` | `:Identifier` |  | `concat("http://data.europa.eu/a4g/agent/id/", text())` | Linked to org via `:hasID` | `xsd:string` |  |  |
| `//cac:PostalAddress/cac:Country/cbc:IdentificationCode` | `:hasCountryCode` | `locn:Address` |  | `concat(../../(parent Party)/PartyIdentification[1]/cbc:ID, "-address")` | Linked to org via `:registeredAddress` |  | `mapCountryCode` | `http://publications.europa.eu/resource/authority/country/{uppercase(code)}` |
| `//cac:ProcurementProject/cbc:Name` | `dcterms:title` | `:Procedure` |  | `concat("https://contrataciondelestado.es/procedure/", ../cbc:ContractFolderID)` |  | `xsd:string` |  |  |
| `//cac:ProcurementProjectLot/cbc:ID` | `:hasID` | `:Lot` |  | `concat("https://contrataciondelestado.es/lot/", text())` | Linked to Procedure via `:hasProcurementScopeDividedIntoLot` |  |  |  |
| `//cac:ProcurementProjectLot/cac:ProcurementProject/cbc:Name` | `dcterms:description` | `:Lot` |  | `concat("https://contrataciondelestado.es/lot/", ../cbc:ID)` |  | `xsd:string` |  |  |
| `//cac:TenderResult/cbc:ReceivedTenderQuantity` | `:hasReceivedTenders` | `:SubmissionStatisticalInformation` |  | `concat("https://contrataciondelestado.es/statistics/", cac:AwardedTenderedProject/cbc:ProcurementProjectLotID)` | Linked to Lot via `:concernsSubmissionsForLot` | `xsd:integer` |  |  |
| `//cac:TenderResult/cbc:AwardDate` | `:hasAwardDecisionDate` | `:LotAwardOutcome` |  | `concat("https://contrataciondelestado.es/award/", cac:Contract/cbc:ID, "-", cac:AwardedTenderedProject/cbc:ProcurementProjectLotID)` | Linked to Lot via `:describesLot` | `xsd:date` |  |  |
| `//cac:WinningParty/cac:PartyName/cbc:Name` | `foaf:name` | `org:Organization` |  | `concat("http://data.europa.eu/a4g/agent/", ../cac:PartyIdentification/cbc:ID)` |  | `xsd:string` |  |  |
| `//cac:BudgetAmount/cbc:EstimatedOverallContractAmount` | `:hasEstimatedValue` | `:Procedure` |  | `concat("https://contrataciondelestado.es/procedure/", ../../cbc:ContractFolderID)` |  | `xsd:decimal` |  |  |
| `//cac:RequiredCommodityClassification/cbc:ItemClassificationCode` | `:hasMainClassification` | `:Procedure`/`:Lot` |  | For Procedure: Use Procedure URI; For Lot: Use Lot URI |  |  | `mapCPV` | SKOS concept from CPV ontology (external) |
| `//cac:TenderingProcess/cbc:ProcedureCode` | `:usesTechnique` | `:Procedure` | `:FrameworkAgreementTechniqueUsage` | `concat("https://contrataciondelestado.es/procedure/", ../cbc:ContractFolderID)` |  |  | `mapProcedureCode` | SKOS concept from `procurement-procedure-type` scheme |
| `//cac-place-ext:ValidNoticeInfo/cbc-place-ext:NoticeTypeCode` | `dcterms:type` | `:ResultNotice` |  | Value of `/entry/id` |  |  | `mapNoticeType` | SKOS concept (custom mapping) |
