Feature: Accommodation of textual data, linked data with URIs instead of text, and both
   In order for a bibliographic framework to accommodate textual data, linked data with URI instead of text, and both
   As a system
   It needs to be able to store URI, text, and both

   Scenario: Store textual data about bibliographic record
      Given a chunk of textual data from a bibliographic record
      When a user stores the data
      Then the data is stored
      
   Scenario: Store URI data about bibliographic record
      Given a URI from a bibliographic record
      When a user stores the data
      Then the data is stored
