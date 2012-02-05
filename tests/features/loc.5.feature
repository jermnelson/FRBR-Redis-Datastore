Feature: Consideration of the needs of all sizes and types of libraries, from small public to large research.
   In order for a bibliographic framework to consider the needs of all sizes and types of libraries
   As a system
   It must be able to support single and multiple collections for different organizational structures
   
   Scenario: Small video collection of non-profit organization library
       Given a collection for a non-profit organization
       When the collection is ingested
       Then users can access the collection's bibliographic cubes
       
   Scenario: Private library arts college library collection
       Given a collection for a college library
       When the collection is ingested
       Then users can access the collection's bibliographic cubes
            
   Scenario: Small public library collection
       Given a collection for a small-public library
       When the collection is ingested
       Then users can access the collection's bibliographic cubes
       
   Scenario: Large public library collection
       Given a collection for a large-public library
       When the collection is ingested
       Then users can access the collection's bibliographic cubes
       
   Scenario: Large academic library collection
       Given a collection for a large-academic library
       When the collection is ingested
       Then users can access the collection's bibliographic cubes
       
   Scenario: Consortium library collection
       Given a collection for a consortium
       When the collection is ingested
       Then users can access the collection's bibliographic cubes
       
       
    
  
