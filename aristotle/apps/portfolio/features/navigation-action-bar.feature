Feature: Portfolio App Navigation Action Bar Default Display
    In order to display the default app view for the Navigation Action Bar
    As users
    the Portfolio App displays a Navigation Action Bar

    Scenario: Display Portfolio App Navigation Action Bar
        Given I have the default Portfolio App with a nav-action-bar
        When I access the Portfolio App
        Then I see Portfolio App Navigation Action Bar

    Scenario: Display Portfolio App Navigation Action Bar Icon
        Given I access the Portfolio App with a nav-action-bar
        When I see the Portfolio App Navigation Action Bar
        Then I see the Portfolio App has an icon

    Scenario: Display Portfolio App Navigation Action Bar Title
        Given I access the Portfolio App with a nav-action-bar
        When I see the Portfolio App Navigation Action Bar
        Then Isee the title of App Portfolio

    Scenario: Display Institution Logo in the Navigation Action Bar
        Given I access the Portfolio App with a nav-action-bar
        When I see the Portfolio App Navigation Action Bar
        Then I see the Institution logo

    Scenario: Display Views button in the Navigation Action Bar
        Given I access the Portfolio App with a nav-action-var
        When I see the Portfolio App Navigation Action Bar
        Then I see the Views button




    



