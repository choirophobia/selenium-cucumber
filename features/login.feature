Feature: User Authentication
  As a registered user
  I want to log in to access the dashboard

#   @smoke
#   Scenario: Successful login
#     Given I navigate to the login page
#     When I enter valid credentials
#     And I submit the form
#     Then I should see the inventory dashboard

  @negative
  Scenario Outline: Failed login
    Given I navigate to the login page
    When I enter username "<username>" and password "<password>"
    And I submit the form
    Then I should see error "<message>"


    Examples:
      | username           | password         | message                          |
      | locked_out_user    | secret_sauce     | Epic sadface: Sorry, this user has been locked out. |