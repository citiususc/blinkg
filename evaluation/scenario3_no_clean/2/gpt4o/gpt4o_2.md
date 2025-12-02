| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| entry/id | :hasID | :Procedure | :Identifier | concat('proc-', hash(entry/id)) | N/A | IRI | generateProcedureID | proc-[SHA256(entry/id)] |
| cac-place-ext:ContractFolderStatus/cbc:ContractFolderID | :hasID | :Procedure | :Identifier | same as generateProcedureID | entry/id maps to contract folder | string | extractContractFolderID | 561770M |
| cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyIdentification[cbc:ID@schemeName='NIF']/cbc:ID | :hasID | org:Organization | :Identifier | concat('org-', value) | ID@schemeName='NIF' | string | generateOrgID | org-P0200000H |
| cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cbc:TypeCode | :hasProcedureType | :Procedure | skos:Concept | use procedure subject | code mapped to SKOS URI | URI | mapProcedureType | http://publications.europa.eu/resource/authority/procurement-procedure-type/open |
| cac-place-ext:ContractFolderStatus/cac:ProcurementProjectLot/cbc:ID | :hasProcurementScopeDividedIntoLot | :Procedure | :Lot | concat('lot-', procedureID, '-', ID) | ProcedureID from entry | string | generateLotID | lot-proc-[hash]-1 |
| cac:RealizedLocation/cbc:CountrySubentityCode | :hasCountryCode | locn:Address | skos:Concept | concat('addr-', hash(XML path)) | LotID or OrgID | string | mapNUTSRegion | http://publications.europa.eu/resource/authority/country/ESP |
