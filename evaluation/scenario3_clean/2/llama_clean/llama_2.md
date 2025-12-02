| XML Path | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /entry/id | :hasID | :ProcurementObject | - | https://contrataciondelestado.es/sindicacion/licitacionesPerfilContratante/{id} | - | xsd:string | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cbc:ContractFolderID | :hasID | :Lot | :ProcurementObject | https://contrataciondelestado.es/sindicacion/licitacionesPerfilContratante/{id}/lot/{lotID} | :hasProcurementScopeDividedIntoLot | - | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cbc:ContractingPartyTypeCode | :hasProcurementScopeDividedIntoLot | :ProcurementObject | :Lot | - | :hasProcurementScopeDividedIntoLot | - | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cbc:Name | :playedByOrganisation | :Buyer | :ProcurementObject | https://contrataciondelestado.es/organisations/{organisationID} | :playedByOrganisation | - | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cbc:Name | :describesLot | :LotAwardOutcome | :Lot | - | :describesLot | - | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cac:RequiredCommodityClassification/cbc:ItemClassificationCode | :hasID | :Lot | - | https://contrataciondelestado.es/classifications/{classificationCode} | - | xsd:string | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cbc:ResultCode | :hasCountryCode | :LotAwardOutcome | - | - | - | xsd:string | mapResultCodeToCountryCode | {countryCode} |
| /entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cbc:AwardDate | :hasAwardDecisionDate | :LotAwardOutcome | - | - | - | xsd:date | - | - |
| /entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cac:WinningParty/cac:PartyIdentification/cbc:ID | :playedBy | :AgentInRole | :LotAwardOutcome | https://contrataciondelestado.es/agents/{agentID} | :playedBy | - | - | - |
