Feature: Map MARC21 fields to RDA Core Items
    In order to share bibliographic information across multiple platforms
    As catalogers
    we need to map MARC21 fields to their RDA Core Item counterparts
    
    Scenario: Extracting RDA Manifestation Title Proper 
       Given we have a MARC record
       When "<code>" field subfield "<subfield>" exists
       | code | subfield | 
       | 245  | a        |
       | 245  | c        |
       | 245  | n        |
       | 245  | p        | 
       Then the titleProper property of RDA Manifestation is set
