Feature: Continuation of maintenance of MARC until no longer necessary. Compatibility with MARC-based records. Provision of transformation from MARC 21 to a new bibliographic environment
    In order for a bibliographic framework to be compatibile with MARC-based records
    As a system
    It must be able to ingest and extract MARC21 records
    
   Scenario: Ingest a MARC21 record
       Given an existing MARC21 record
       When a user ingests the MARC21 record into the Redis datastore
       Then the user can access the MARC21 brane 

   Scenario: Extract a MARC21 record
       Given a native FRBR WEMI cube in the Redis datastore
       When a user extracts MARC21 brane
       Then the user will have a MARC21 record    
