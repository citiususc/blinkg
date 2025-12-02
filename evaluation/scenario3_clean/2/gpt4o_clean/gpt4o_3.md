| XML Path  | Ontology Property| Entity Class   | Related Entity Class | Subject Generation | Join   | Datatype   | Function Name | Function Output |
|----------------------|------------------|----------------|----------------------|--------------------------|-----------------------------|------------|------------|-------------------|
| entry/cac-place-ext:ContractFolderStatus/cbc:ContractFolderID   | :hasID | :Procedure| :Identifier| concat('proc_', ContractFolderID)|   |  | | |
| entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cbc:Name  | rdfs:label  | :Procedure|  | concat('proc_', ContractFolderID)|   | xsd:string | | |
| entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cbc:TypeCode   | :hasProcurementScopeDividedIntoLot   | :Procedure| :Lot | concat('proc_', ContractFolderID)| ContractFolderID = Lot.ProcurementProjectID|  | | |
| entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProjectLot/cbc:ID | :hasID | :Lot | :Identifier| concat('lot_', ContractFolderID, '_', ID)  |   | | | |
| entry/cac-place-ext:ContractFolderStatus/cac:LocatedContractingParty/cac:Party/cac:PartyIdentification[schemeName='NIF']/cbc:ID | :hasID    | org:Organization| :Identifier| concat('org_', ID)|   |  | |  |
| entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cac:RequiredCommodityClassification/cbc:ItemClassificationCode | skos:Concept   | :Procedure| skos:Concept| concat('proc_', ContractFolderID)| skos:exactMatch in CPV list ||| |
