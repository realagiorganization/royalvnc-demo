Feature: Session settings
  The demo app should persist session settings that affect connection behavior.

  Scenario: Toggle view-only mode
    Given a VNC session settings screen is open
    When the user enables "View Only"
    Then the setting "view-only" is stored as "enabled"
    And the next connection runs in "view-only" mode

  Scenario: Change color depth
    Given a VNC session settings screen is open
    When the user selects color depth "24-bit"
    Then the setting "color-depth" is stored as "24-bit"
    And the next connection requests "24-bit" pixels
