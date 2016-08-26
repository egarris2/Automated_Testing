Feature: Lockout shuts down compressor

Scenario: Flow is lost
  Given FS is on
    When Flow stops
    Then FS is off
    When Flow starts again
    Then FS is on
