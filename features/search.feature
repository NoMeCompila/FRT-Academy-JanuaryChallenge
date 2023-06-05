Feature: Searching on Wikipedia

  Scenario Outline: Search for an element
    Given I am on the Wikipedia home page
    When I search for "<element>"
    Then I should see the search results for "<element>"

    Examples:
    | element  |
    | Python   |
    | Selenium |
