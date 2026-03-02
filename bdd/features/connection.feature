Feature: Connect to a VNC host
  The demo app should establish a connection to a VNC host and show connection state.

  Scenario: Connect with saved host entry
    Given a saved VNC host "demo.local" on port "5900"
    And the demo app is on the connection list
    When the user selects the host entry
    Then the app attempts a VNC connection to "demo.local:5900"
    And the connection status becomes "connecting"
    And the status transitions to "connected"

  Scenario: Disconnect from an active session
    Given an active VNC session to "demo.local:5900"
    When the user taps "Disconnect"
    Then the session ends cleanly
    And the status becomes "disconnected"
