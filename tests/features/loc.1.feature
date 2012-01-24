Feature: Broad accommodation of content rules and data models
   In order for a bibliographic framework to accommodate MARC21 and MODS formats
   As a system
   It needs to ingest and extract a MARC21 and MODS records

   Scenario: Ingest a MARC21 record
       Given an existing MARC21 record
       When a user ingests the MARC21 record into the Redis datastore
       Then the user can access the MARC21 brane of the FRBR WEMI cube

   Scenario: Extract a MARC21 record
       Given a native FRBR WEMI cube in the Redis datastore
       When a user extracts MARC21 record
       Then the user will have a MARC21 record

   Scenario: Ingest a MODS record
       Given an existing MODS XML record
       When a user ingest a MODS XML record into the Redis datastore
       Then the user can access the MODS brane of the FRBR WEMI cube

   Scenario: Extract a MODS record
       Given a native FRBR WEMI cube in the Redis datastore
       When a user extracts a MODS record
       Then the user will have a MODS XML record
