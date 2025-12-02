| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /entry/id | :hasID | :Identifier | :ProcurementObject | Concatenate 'id/' + value | - | - |  | <http://data.europa.eu/a4g/id/XXX> |
| /entry/link/@href | :refersTo | :ResultNotice | :Procedure | Concatenate 'proc/' + value | - | - |  | <http://data.europa.eu/a4g/proc/XXX> |
| /entry/summary/@type | :hasType | :ContextSpecificDescription | - | Concatenate 'type/' + value | - | - |  | <http://data.europa.eu/a4g/type/XXX> |
| /entry/title | :hasTitle | :ResultNotice | - | Concatenate 'title/' + value | - | - |  | <http://data.europa.eu/a4g/title/XXX> |
| /entry/updated | :hasDispatchDate | :ResultNotice | - | XML value | - | format_date |  | YYYY-MM-DDThh:mm:ss.ssZ |
| /entry/cbc:ContractFolderID | :hasID | :Lot | :ProcurementObject | Concatenate 'lot/' + value | - | - |  | <http://data.europa.eu/a4g/lot/XXX> |
| /entry/cbc-place-ext:ContractFolderStatusCode | :hasID | :Identifier | :ProcurementObject | Concatenate 'stat/' + value | - | - |  | <http://data.europa.eu/a4g/stat/XXX> |
| /entry/cac:Party/cac:PartyIdentification/cbc:ID | :hasIdentifierValue | :Identifier | :AgentInRole | XML value | - | - |  | XXX |
| /entry/cac:Party/cac:PartyName/cbc:Name | :hasName | :PrimaryRole | org:Organization | XML value | - | - |  | XXX |
| /entry/cac:Party/cac:Contact/cbc:Telephone | :hasPhone | :PrimaryRole | org:Organization | XML value | - | - |  | XXX |
| /entry/cac:Party/cac:Contact/cbc:Telefax | :hasFax | :PrimaryRole | org:Organization | XML value | - | - |  | XXX |
| /entry/cac:Party/cac:Contact/cbc:ElectronicMail | :hasEmail | :PrimaryRole | org:Organization | XML value | - | - |  | XXX |
| /entry...... |  |  |  |  |  |  |  |  |
