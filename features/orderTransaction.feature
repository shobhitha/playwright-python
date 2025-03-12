Feature: Order Transaction
  Tests related to order transactions


  Scenario Outline: : Verify Order success message shown in details page
    Given Place the item order with <username> and <password>
    And the user is on landing page
    When I login to portal with <username> and <password>
    And navigate to Orders page
    And Select the orderID
    Then Order message is successfully displayed
    Examples:
        |username              | password   |
        |rahulshetty@gmail.com | Iamking@000|

