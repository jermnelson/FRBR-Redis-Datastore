Feature: Consideration of the needs of all sizes and types of libraries, from small public to large research.
   In order for a bibliographic framework to consider the needs of all sizes and types of libraries
   As a system
   It must be able to support single and multiple collections for different organizational structures
   
   Scenario: Small video collection of non-profit organization library
       Given a small video collection of mixed VHS and DVD videos for a non-profit organization library
       When the collection is ingested
       Then users can access the collection's bibliographic cubes
       
   Scenario: Small public library collection
   
   
   Scenario: Private library arts college library collection
       Given a collection of mixed material including a legacy ILS catalog of MARC records, digital repository, and electronic records
       When the collection is ingested
       Then users can access the collection's bibliographic cubes
       
   Scenario: Large research university collection
   
   
   Scenario: Library consortium collection
       
       
  
