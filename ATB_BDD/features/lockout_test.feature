Feature: Lockout shuts down compressor

Scenario: Too much water in the condensate drain pan
  Given Y1 is on
    When condensate overflow is closed
    Then ICM sends a lockout signal
