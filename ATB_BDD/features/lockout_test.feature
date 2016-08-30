Feature: High Pressure Fault Scenario

Scenario: High Pressure Fault
	Given HP is closed and L is off
		When High pressure goes out of bounds
		Then HP is open and L is on
