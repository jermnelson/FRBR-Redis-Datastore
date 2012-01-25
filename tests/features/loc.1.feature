Feature: Broad accommodation of content rules and data models
   In order for a bibliographic framework to accommodate RDA, AACR2, DACS, VRA Core and CCO
   As a system
   It needs to be able to represent and manipulate content rules and data models for RDA, AACR2, DACS, VRA Core and CCO
   
   Scenario: Represent RDA carrier types for FRBR Manifestation as a content rule
       Given a microfiche FRBR Manifestation entity in the datastore
       When the entity has a RDA carrierTypeManifestation
       Then the carrierTypeManifestation value will be microfiche
   
   
   Scenario: Represent AACR2 MARC21 007 as a content rule 
   
   
   Scenario: Represent DACS content rule
   
   
   Scenario: Represent VRA Core content rule
   
   
   Scenario: CCO as a content rule 




