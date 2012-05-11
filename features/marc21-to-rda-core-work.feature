Feature: Map MARC21 fields to rdaWork Core
    In order to share bibliographic information across multiple platforms
    As catalogers
    we need to map MARC21 fields to their rdaWork Core counterparts
    
    Scenario: Extracting rdaWork Cataloguers Note
       Given we have a MARC record
       When "<code>" field subfield "<subfield>" exists
       | code | subfield | 
       Then the CataloguersNote property of rdaWork is set
       
    Scenario: Extracting rdaWork Coordinates Of Cartographic Content
       Given we have a MARC record
       When "<code>" field subfield "<subfield>" exists
       | code | subfield |
       Then the CoordinatesOfCartographicContent property of rdaWork is set
     
    Scenario: Extracting rdaWork Title Of Work
       Given we have a MARC record
       When "<code>" field subfield "<subfield>" exists
       | code | subfield | 
       | 245  | a        |
       | 245  | c        |
       | 245  | n        |
       | 245  | p        | 
       Then the TitleOfWork property of rdaWork is set
