Feature: User Tasks For Work
  In order for a user to find, identify, select, or obtain a work
  As users
  They'll search the Redis datastore for a Work

  Scenario: Find Anatomy of the human body
      Given the user knows the title is Anatomy of the human body
      When the user interacts with the datastore to find the work
      Then the user access the work with the title of Anatomy of the human body
