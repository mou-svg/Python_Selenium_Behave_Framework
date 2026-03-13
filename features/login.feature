Feature: Login Functionality
  Scenario: Valid Login
    Given user navigates to login page
    When User enters username "standard_user"
    When user enters password "secret_sauce"
    When user clicks login button
    Then user should see the dashboard