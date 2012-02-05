Feature: Provision for types of data that logically accompany or support bibliographic description
   In order for a bibliographic framework to provision type of data that logically accompany or support bibliographic description
   As a system
   It needs to be able to store bibliographic metadata for an entity

   Scenario: Ingest a MODS record
       Given an existing MODS XML record
       When a user ingest a MODS XML record into the Redis datastore
       Then the user can access the MODS brane of the FRBR WEMI cube

   Scenario: Ingest a Dublin Core record
       Given an existing DC XML record
       When a user ingest a DC XML record into the Redis datastore
       Then the user can access the DC brane of the FRBR WEMI cube
       
   Scenario: Ingest a VRA Core record
       Given an existing VRACore XML record
       When a user ingest a VRACore XML record into the Redis datastore
       Then the user can access the VRACore brane of the FRBR WEMI cube
  
      
      

