| XML Path | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /entry/id | :hasID | :Document | :Identifier | URI of the document | - || | |
| /entry/summary[@type='text'] | :title | :Document | rdfs:Literal | Concatenate '/entry/' and the value of the @id attribute | - | string | | |
| /entry/summary/cbc:ContractFolderID | :hasID | :ProcurementObject | :Identifier | Concatenate '/entry/' and the value of the @id attribute | - || | |
| /entry/summary/cbc:ContractFolderID | :hasID | :Identifier | - | Concatenate '/entry/' and the value of the @id attribute | - | string | | |
| /entry/summary/cbc:ContractFolderStatusCode/@listURI | :hasPublicationStatus | :ResultNotice | rdfs:Literal | Concatenate '/entry/' and the value of the @id attribute | The value of @listURI is a URI naming a property specifying the status of the notice ||||
| /entry/summary/cbc:ItemClassificationCode/@listURI | :hasProcurementMethod | :ResultNotice | rdfs:Literal | Concatenate '/entry/' and the value of the @id attribute | The value of @listURI is a URI naming a property specifying the method used for the procurement ||||
| /entry/cac:TenderingProcess/cbc:ProcedureCode/@listURI | :hasProcurementScope | :ResultNotice | rdfs:Literal | Concatenate '/entry/' and the value of the @id attribute | The value of @listURI is a URI naming a property specifying the scope of the procurement || | |
		
