Feature: Inventory Management

  @smoke
  Scenario: Add to chart 1 item
    Given I navigate to the login page
    When I enter valid credentials
    And I submit the form
    Then I should see the inventory dashboard
    Then I click add to cart for the first item