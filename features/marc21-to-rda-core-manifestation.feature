Feature: Map MARC21 fields to RDA Core Manifestation
    In order to share bibliographic information across multiple platforms
    As catalogers
    we need to map MARC21 fields to their RDA Core Manifestation counterparts
    
    Scenario: Extracting RDA Manifestation Applied Material 
       Given we have a MARC record
       When "<code>" field subfield "<subfield>" exists
       | code | subfield | 
       | 245  | a        |
       | 245  | c        |
       | 245  | n        |
       | 245  | p        | 
       Then the AppliedMaterial property of rdaManifestation is set

    Scenario: Extracting RDA Manifestation Carrier Type
       Given we have a MARC record
       When "<code>" field subfield "<subfield>" exists
       | code | subfield | 
       | 338  | c        |       
       Then the CarrierType property of rdaManifestation is set
       
    Scenario: Extracting RDA Manifestation Copyright Date
       Given we have a MARC record
       When "<code>" field subfield "<subfield>" exists
       | code | subfield | 
       | 542  | g        |
       | 260  | c        |
       Then the CopyrightDate property of rdaManifestation is set
       
       
