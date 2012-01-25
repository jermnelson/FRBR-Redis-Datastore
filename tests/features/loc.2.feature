Feature: Provision for types of data that logically accompany or support bibliographic description
   In order for a bibliographic framework to provision type of data that logically accompany or support bibliographic description
   As a system
   It needs to be able to store bibliographic metadata for an entity

   Scenario: Ingest a MODS record
       Given an existing MODS XML record
       When a user ingest a MODS XML record into the Redis datastore
       Then the user can access the MODS brane of the FRBR WEMI cube

   Scenario: Extract a MODS record
       Given a native FRBR WEMI cube in the Redis datastore
       When a user extracts a MODS record
       Then the user will have a MODS XML record

   Scenario: Store a title for an ebook
      Given a title of an ebook
      When a user stores information about the ebook
      Then the title of the ebook is stored
      
      

