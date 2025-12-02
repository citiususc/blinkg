| XML Path | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| id | :hasID | :ProcurementObject | :Identifier | id_value | N/A | - | - | - |
| link/@href | owl:sameAs | :ProcurementObject | :Document | get_document_uri(id_value) | N/A | - | - | - |
| title | :name | :Lot | rdfs:Literal | concatenate(subject, "/name") | N/A | xsd:string | - | - |
| summary/cbc:ContractFolderID | :description | :Lot | rdfs:Literal | concatenate(subject, "/lot/description") | N/A | xsd:string | - | - |
| cac:ContractingParty/cbc:ContractingPartyTypeCode | :typeCode | :Buyer | rdfs:Literal | concatenate(subject, "/buyer/typeCode") | N/A | xsd:string | - | - |
| cac:Party/cbc:WebsiteURI | :website | :Buyer | xsd:anyURI | N/A | N/A | xsd:anyURI | - | - |
| cac:Party/cac:PartyIdentification/cbc:ID | :identifierValue | :Identifier | rdfs:Literal | N/A | Equality with skos:topConceptOf in skos.ttl | xsd:string | - | - |
| cac:Party/cac:PartyName/cbc:Name | :name | :Buyer | rdfs:Literal | concatenate(subject, "/buyer/name") | N/A | xsd:string | - | - |
| cac:PostalAddress/cbc:PostalZone | :postalCode | :Address | rdfs:Literal | N/A | N/A | xsd:string | - | - |
| cac:PostalAddress/cac:AddressLine/cbc:Line | :streetAddress | :Address | rdfs:Literal | N/A | N/A | xsd:string | - | - |
| cac:PostalAddress/cac:Country/cbc:IdentificationCode | :countryCode | :Address | rdfs:Literal | N/A | Equality with skos:topConceptOf in skos.ttl | | get_country_code | Returns the country code |
| cac:Contact/cbc:ElectronicMail | :electronicMailAddress | :Buyer | rdfs:Literal | N/A | N/A | xsd:string | - | - |

