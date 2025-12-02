| XML Path | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
|----------|-------------------|--------------|-----------------------|--------------------|----------------|----------|----------------|------------------|
| entry/id | :hasID | :Procedure | :Identifier | http://data.example.org/procurement/entry/id | ||  ||
| entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyIdentification[cbc:ID@schemeName='NIF']/cbc:ID | :hasID | org:Organization | :Identifier | http://data.example.org/organization/NIF | | | | |
| entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cbc:Name | rdfs:label | :Procedure | | http://data.example.org/procurement/entry/id | | xsd:string | | |
| entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cac:BudgetAmount/cbc:EstimatedOverallContractAmount | schema:estimatedCost | :Procedure | | http://data.example.org/procurement/entry/id | | xsd:decimal | | |
| entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cac:RequiredCommodityClassification/cbc:ItemClassificationCode | schema:category | :Procedure | | http://data.example.org/procurement/entry/id | | | | |
| entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProjectLot/cbc:ID | :hasID | :Lot | :Identifier | http://data.example.org/lot/lot_id | |  | | |
| entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProjectLot/cac:ProcurementProject/cbc:Name | rdfs:label | :Lot | | http://data.example.org/lot/lot_id | | xsd:string | | |
| entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cac:AwardedTenderedProject/cbc:ProcurementProjectLotID | :describesLot | :LotAwardOutcome | :Lot | http://data.example.org/award/lot_id | link using lot_id | | | |
| entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cbc:AwardDate | :hasAwardDecisionDate | :LotAwardOutcome | | http://data.example.org/award/lot_id | | xsd:date | | |
| entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cbc:ReceivedTenderQuantity | :hasReceivedTenders | :SubmissionStatisticalInformation | | http://data.example.org/stat/lot_id | | xsd:integer | | |
