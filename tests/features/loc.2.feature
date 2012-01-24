Feature: Provision for types of data that logically accompany or support bibliographic description
   In order for a bibliographic framework to provision type of data that logically accompany or support bibliographic description
   As a system
   It needs to be able to store title, author, and subject metadata for a work

   Scenario: Store a title for an ebook
      Given a title of an ebook
      When a user stores information about the ebook
      Then the title of the ebook is stored

