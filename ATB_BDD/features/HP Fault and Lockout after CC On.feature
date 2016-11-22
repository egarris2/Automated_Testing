Feature: HP Fault and Lockout after CC On

Scenario: High Pressure Fault is introduced after Compressor has turned on
	Given test 1 initial conditions
		When High pressure goes out of bounds
		Then HP is open and L is on
