| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| id | :hasID | :ProcurementObject | :Identifier | id_value | N/A | xsd:string | get_id_value | Returns the id value |
| link/@href | owl:sameAs | :ProcurementObject | :Document | get_document_uri(id_value) | N/A | xsd:anyURI | get_document_uri | Constructs the document URI |
| title | :name | :Lot | rdfs:Literal | concatenate(subject, "/name") | N/A | xsd:string | concatenate | Returns the fully qualified name property |
| summary/cbc:ContractFolderID | :description | :Lot | rdfs:Literal | concatenate(subject, "/lot/description") | N/A | xsd:string | concatenate | Returns the fully qualified description |
| cac:ContractingParty/cbc:ContractingPartyTypeCode | :typeCode | :Buyer | rdfs:Literal | concatenate(subject, "/buyer/typeCode") | N/A | xsd:string | concatenate | Returns the fully qualified type code |
| cac:Party/cbc:WebsiteURI | :website | :Buyer | xsd:anyURI | N/A | N/A | xsd:anyURI | get_website_uri | Returns the website URI |
| cac:Party/cac:PartyIdentification/cbc:ID | :identifierValue | :Identifier | rdfs:Literal | N/A | Equality with skos:topConceptOf in skos.ttl | xsd:string | get_identifier_value | Returns the identifier value |
| cac:Party/cac:PartyName/cbc:Name | :name | :Buyer | rdfs:Literal | concatenate(subject, "/buyer/name") | N/A | xsd:string | concatenate | Returns the fully qualified name property |
| cac:PostalAddress/cbc:PostalZone | :postalCode | :Address | rdfs:Literal | N/A | N/A | xsd:string | get_postal_code | Returns the postal code |
| cac:PostalAddress/cac:AddressLine/cbc:Line | :streetAddress | :Address | rdfs:Literal | N/A | N/A | xsd:string | get_street_address | Returns the street address |
| cac:PostalAddress/cac:Country/cbc:IdentificationCode | :countryCode | :Address | rdfs:Literal | N/A | Equality with skos:topConceptOf in skos.ttl | xsd:string | get_country_code | Returns the country code |
| cac:Contact/cbc:ElectronicMail | :electronicMailAddress | :Buyer | rdfs:Literal | N/A | N/A | xsd:string | get_email_address | Returns the electronic mail address |
