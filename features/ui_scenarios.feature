Feature: SauceDemo UI automation

  Scenario: Happy path - Add product to cart
    Given I open the SauceDemo login page
    When I login with valid credentials
    And I add a product to the cart
    And I go to the cart
    Then I should see the product in the cart

  Scenario: Unhappy path - Invalid login
    Given I open the SauceDemo login page
    When I login with invalid credentials
    Then I should see a login error message
