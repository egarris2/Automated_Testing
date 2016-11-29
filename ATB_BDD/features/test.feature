Feature: HP Fault and Lockout after CC On

Scenario: High Pressure Fault is introduced after Compressor has turned on
	Given test 1 initial conditions
		When High pressure goes out of bounds
		Then HP is open and CC is off
			When 30 seconds pass
			Then HP is open and CC and A are off. L is on
