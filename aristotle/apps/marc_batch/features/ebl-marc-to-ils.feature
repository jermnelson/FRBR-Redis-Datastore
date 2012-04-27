Feature: EBL MARC record customization
    In order to load EBL MARC records into our ILS
    As catalogers
    We need to modify each EBL MARC record with these scenarios
    
    Scenario: Repair 006 defect
       Given we have a MARC record
       When the "<code>" field subfield "<subfield>" is "<value>"
       | code | subfield | value |
       | 007  | 0       | m    |
       | 007  | 1       | \    |
       | 007  | 2       | \    |
       | 007  | 3       | \    |
       | 007  | 4       | \    |
       | 007  | 5       | d    |
       Then the 006 field value is m\\\\\\\\d\\\\\\\\
       
    Scenario: Repair 007 defect
       Given we have a MARC record
       When the "<code>" field subfield "<subfield>" is "<value>"
       | code | subfield | value |
       | 007  | 0        | c     |
       | 007  | 1        | r     |
       | 007  | 2        | PIPE  |
       | 007  | 3        | PIPE  |
       | 007  | 4        | PIPE  |
       | 007  | 5        | PIPE  |
       | 007  | 5        | None  |
       | 007  | 6        | PIPE  |
       | 007  | 6        | None  |
       | 007  | 7        | PIPE  |
       | 007  | 7        | None  |
       | 007  | 8        | PIPE  |
       | 007  | 8        | None  |
       | 007  | 9        | PIPE  |
       | 007  | 9        | None  |
       | 007  | 10       | PIPE  |
       | 007  | 10       | None  |
       | 007  | 11       | PIPE  |
       | 007  | 11       | None  |
       | 007  | 12       | PIPE  |
       | 007  | 12       | None  |
       | 007  | 13       | u     |
       | 007  | 13       | None  |
       Then the 007 field value is cr           a
       
    Scenario: Repair 008 defect
       Given we have a MARC record
       When the "<code>" subfield value is "<value>"
       | code | value |
       | 008  | o     |
       Then the "<code>" subfield value is "<value>"
       | code | value |
       | 008  | \     |
       
    Scenario: Delete 050 second subfield a and modify
        Given we have a MARC record
        When the 050 has a second subfield a
        Then the 050 does not have a second subfield a
        And the "<code>" subfield "<subfield>" ends with "<value>"
        | code | subfield | value |
        | 050  | a        | eb    |
        
    Scenario: Normalize 050 volume in subfield b
        Given we have a MARC record
        When "<code>" subfield "<subfield>" has "<snippet>"
        | code | subfield | snippet |
        | 050  | b        | vol     |
        | 050  | b        | vol.    |
        Then the "<code>" subfield "<subfield>" snippet is now "<value>"
        | code | subfield | value |
        | 050  | b        | v.    |
        
    Scenario: Normalize 050 numbers in subfield b
        Given we have a MARC record
        When "<code>" subfield "<subfield>" has "<snippet>"
        | code | subfield | snippet |
        | 050  | b        | no.\    |
        Then the "<code>" subfield "<subfield>" snippet is now "<value>"
        | code | subfield | value |
        | 050  | b        | no.   |
        And the "<code>" subfield "<subfield>" ends with "<value>"
        | code | subfield | value |
        | 050  | b        | eb    |
        
    Scenario: Normalize 050 band in subfield b
        Given we have a MARC record
        When "<code>" subfield "<subfield>" has "<snippet>"
        | code | subfield | snippet |
        | 050  | b        | Band    |
        | 050  | b        | Band.   |
        | 050  | b        | Bd\     |
        | 050  | b        | Bd.\    |
        Then the "<code>" subfield "<subfield>" snippet is now "<value>"
        | code | subfield | value |
        | 050  | b        | Bd.   |
        And the "<code>" subfield "<subfield>" ends with "<value>"
        | code | subfield | value |
        | 050  | b        | eb    |