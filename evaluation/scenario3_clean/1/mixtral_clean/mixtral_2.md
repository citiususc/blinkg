| XML Path | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /entry/id | :hasID | :Identifier | :ProcurementObject | Concatenate 'id/' + value | - | - |  |  |
| /entry/link/@href | :refersTo | :ResultNotice | :Procedure | Concatenate 'proc/' + value | - | - |  |  |
| /entry/summary/@type | :hasType | :ContextSpecificDescription | - | Concatenate 'type/' + value | - | - |  | |
| /entry/title | :hasTitle | :ResultNotice | - | Concatenate 'title/' + value | - | - |  |  |
| /entry/updated | :hasDispatchDate | :ResultNotice | - | XML value | - | format_date |  | |
| /entry/cbc:ContractFolderID | :hasID | :Lot | :ProcurementObject | Concatenate 'lot/' + value | - | - |  |  |
| /entry/cbc-place-ext:ContractFolderStatusCode | :hasID | :Identifier | :ProcurementObject | Concatenate 'stat/' + value | - | - |  |  |
| /entry/cac:Party/cac:PartyIdentification/cbc:ID | :hasIdentifierValue | :Identifier | :AgentInRole | XML value | - | - |  | |
| /entry/cac:Party/cac:PartyName/cbc:Name | :hasName | :PrimaryRole | org:Organization | XML value | - | - |  | |
| /entry/cac:Party/cac:Contact/cbc:Telephone | :hasPhone | :PrimaryRole | org:Organization | XML value | - | - |  | |
| /entry/cac:Party/cac:Contact/cbc:Telefax | :hasFax | :PrimaryRole | org:Organization | XML value | - | - |  | |
| /entry/cac:Party/cac:Contact/cbc:ElectronicMail | :hasEmail | :PrimaryRole | org:Organization | XML value | - | - |  | |
