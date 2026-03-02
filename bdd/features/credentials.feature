Feature: Credentials validation
  The demo app should prompt for credentials and handle invalid login attempts.

  Scenario: Successful authentication
    Given the user opens the credentials prompt
    When the user enters username "demo" and password "correct-horse"
    Then the app submits credentials to the VNC server
    And the authentication result is "accepted"

  Scenario: Failed authentication
    Given the user opens the credentials prompt
    When the user enters username "demo" and password "wrong-pass"
    Then the app submits credentials to the VNC server
    And the authentication result is "rejected"
    And an error message "Authentication failed" is shown
