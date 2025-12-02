| XML Path | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /entry/id | :hasID | :ProcurementObject | :ID | Concatenate baseEntityURI and "/" and the value of id | N/A | String | None | - |
| /entry/link/@href | :hasID | :Document | :ID | Concatenate baseEntityURI and the value of href | N/A | String | None | - |
| /entry/summary/@type | :hasType | :Document | :DocumentType | Map "text" to a URI representing the type "text" in the ontology | N/A | String | None | - |
| /entry/summary | :hasDescription | :Document | String | N/A | N/A | String | None | - |
| /entry/title | :hasName | :Document | String | N/A | N/A | String | None | - |
| /entry/updated | :hasDispatchDate | :Document | Date | Convert the date to the xsd:dateTime format compatible with the ontology | N/A | xsd:dateTime | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cbc:ContractFolderID | :hasID | :ProcurementObject | :ID | Concatenate baseEntityURI and "/" and the value of ContractFolderID | N/A | String | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cbc-place-ext:ContractFolderStatusCode/@listURI | :hasDocumentStatusType | :Document | :CodelistValue | Map the listURI to the corresponding URI in the ontology using a function to transform a URI string to a URI | N/A | - | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cbc-place-ext:ContractFolderStatusCode | :hasDocumentStatusCode | :Document | :CodelistValue | Map the value of ContractFolderStatusCode to the corresponding URI in the ontology using a function to transform a string to a URI | N/A | - | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cbc:ContractingPartyTypeCode/@listURI | :hasLegalFormType | :Buyer | :CodelistValue | Map the listURI to the corresponding URI in the ontology using a function to transform a URI string to a URI | N/A | - | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cbc:ContractingPartyTypeCode | :hasLegalForm | :Buyer | :CodelistValue | Map the value of ContractingPartyTypeCode to the corresponding URI in the ontology using a function to transform a string to a URI | N/A | - | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cbc:WebsiteURI | :hasWebsite | :Buyer | - | N/A | N/A | - | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyIdentification/cbc:ID[@schemeName="DIR3"] | :hasDirectoryCode | :Buyer | :Identifier | Concatenate baseEntityURI and "/" and the value of ID | N/A | String | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyIdentification/cbc:ID[@schemeName="NIF"] | :hasTaxID | :Buyer | String | N/A | N/A | String | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyName/cbc:Name | :hasName | :Buyer | String | N/A | N/A | String | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PostalAddress/cbc:CityName | :hasCityName | :Address | String | N/A | N/A | String | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PostalAddress/cbc:PostalZone | :hasPostalZipCode | :Address | String | N/A | N/A | String | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PostalAddress/cac:AddressLine/cbc:Line | :hasStreetName | :Address | String | N/A | N/A | String | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode | :hasCountryCode | :Address | :CountryCode | Map the value of IdentificationCode to the corresponding URI in the ontology using a function to transform a string to a URI | N/A | - | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:Contact/cbc:Name | :hasContactName | :ContactPoint | String | N/A | N/A | String | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:Contact/cbc:Telephone | :hasTelephone | :ContactPoint | String | N/A | N/A | String | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:Contact/cbc:Telefax | :hasFaxNumber | :ContactPoint | String | N/A | N/A | String | None | - |
| /entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:Contact/cbc:ElectronicMail | :hasEmail | :ContactPoint | String | N/A | N/A | String | None | - |
