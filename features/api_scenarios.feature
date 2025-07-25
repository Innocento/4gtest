Feature: RestCountries API tests

  Scenario: Happy path - Get countries by currency
    Given I query countries using "KES" currency
    Then the response should have status 200
    And I should get at least one country

  Scenario: Unhappy path - Invalid currency
    Given I query countries using "INVALIDCURRENCY"
    Then the response should have status 404
