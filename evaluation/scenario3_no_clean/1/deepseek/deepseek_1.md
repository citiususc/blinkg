| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /entry/id | rdf:type | :ResultNotice |  | Value of `<id>` |  |  |  |  |
| /entry/updated | :hasDispatchDate | :ResultNotice |  | Value of `<id>` |  | xsd:dateTime |  |  |
| /entry/cbc:ContractFolderID | :hasID | :Procedure | :Identifier | `http://example.org/procedure/` + split(., " ")[0] | BN generated for Identifier |  | extractProcedureId | "942P" (from "942P LOTE 2") |
| /entry/cbc:ContractFolderID | :hasIdentifierValue | :Identifier (BN) |  | BN for Identifier |  | xsd:string |  |  |
| /entry/cac:TenderingProcess/cbc:ProcedureCode | :hasProcedureType | :Procedure | skos:Concept | `http://example.org/procedure/` + ../cbc:ContractFolderID→split(" ")[0] | `http://publications.europa.eu/resource/authority/procurement-procedure-type/` + mapProcedureCode(.) |  | mapProcedureCode | "open" (for input "1") |
| /entry/cac:TenderingProcess/cbc:ContractingSystemCode | :usesTechnique | :Procedure | :FrameworkAgreementTechniqueUsage | `http://example.org/procedure/` + ../cbc:ContractFolderID→split(" ")[0] | `http://example.org/technique/framework` |  |  |  |
| /entry/cbc:ContractFolderID | :hasProcurementScopeDividedIntoLot | :Procedure | :Lot | `http://example.org/procedure/` + split(., " ")[0] | `http://example.org/lot/` + concat(split(., " ")[0], "-", split(., " ")[2]) |  | generateLotId | "942P-2" (from "942P LOTE 2") |
| /entry/cbc:ContractFolderID | :hasID | :Lot | :Identifier | `http://example.org/lot/` + generateLotId(.) | BN generated for Identifier |  |  |  |
| /entry/cbc:ContractFolderID | :hasIdentifierValue | :Identifier (BN) |  | BN for Identifier |  | xsd:string |  | "942P LOTE 2" |
| /entry/cac:TenderResult/cbc:AwardDate | :hasAwardDecisionDate | :LotAwardOutcome |  | `http://example.org/lot/` + generateLotId(../cbc:ContractFolderID) + "/outcome" |  | xsd:date |  |  |
| /entry/cac:TenderResult/cbc:ReceivedTenderQuantity | :hasReceivedTenders | :SubmissionStatisticalInfo |  | `http://example.org/lot/` + generateLotId(../cbc:ContractFolderID) + "/stats" |  | xsd:integer |  |  |
| /entry/cac:Party/cac:PartyIdentification/cbc:ID | :hasID | org:Organization | :Identifier | `http://example.org/org/` + . | BN generated for Identifier |  |  |  |
| /entry/cac:Party/cac:PartyIdentification/cbc:ID | :hasIdentifierValue | :Identifier (BN) |  | BN for Identifier |  | xsd:string |  |  |
| /entry/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode | :hasCountryCode | locn:Address (BN) | skos:Concept | BN for Address | `http://publications.europa.eu/resource/authority/country/` + countryAlpha2To3(.) |  | countryAlpha2To3 | "ESP" (for input "ES") |
| /entry/cac:Party/cac:PartyName/cbc:Name | :playedByOrganisation | :Buyer | org:Organization | Value of `<id>` + "/buyerRole" | `http://example.org/org/` + ../../cac:PartyIdentification/cbc:ID |  |  |  |
| /entry/cac:Party/cac:Contact/cbc:ElectronicMail | :address | org:Organization | locn:Address (BN) | `http://example.org/org/` + ../../cac:PartyIdentification/cbc:ID | BN for Address |  |  |  |
| /entry/cac:TenderResult/cac:WinningParty/cac:PartyIdentification/cbc:ID | :playedByOrganisation | :Winner | org:Organization | `http://example.org/org/` + . | `http://example.org/org/` + . |  |  |  |
| /entry | :refersToRole | :ResultNotice | :Buyer | Value of `<id>` | Value of `<id>` + "/buyerRole" |  |  |  |
| /entry/cac:TenderResult/cac:WinningParty | :refersToRole | :ResultNotice | :Winner | Value of `<id>` | `http://example.org/org/` + cac:PartyIdentification/cbc:ID |  |  |  |
| /entry/cac:ProcurementProject/cbc:Name | :describesLot | :LotAwardOutcome | :Lot | `http://example.org/lot/` + generateLotId(../cbc:ContractFolderID) + "/outcome" | `http://example.org/lot/` + generateLotId(../cbc:ContractFolderID) |  |  |  |
| /entry/cac:ProcurementProject/cac:BudgetAmount/cbc:TotalAmount | :concernsSubmissionsForLot | :SubmissionStatisticalInfo | :Lot | `http://example.org/lot/` + generateLotId(../../cbc:ContractFolderID) + "/stats" | `http://example.org/lot/` + generateLotId(../../cbc:ContractFolderID) |  |  |  |
