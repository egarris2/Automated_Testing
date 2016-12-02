Feature: HP Fault and Lockout after CC On

Scenario: Testing table data
	Given 	Initial Conditions
		| Parameter | State |
		| R			| ON	|
		| Y1 		| ON	|
		| O 		| OFF	|
		| W1 		| OFF	|
		| HP		| OFF	|
		| LP		| OFF	|
		| FS		| OFF	|
		| CO		| OFF	|
		| LCT		| 458	|
		| DGT		| 132	|
		| DLWT		| 457	|
		| SCT		| 511	|
	
		When High pressure goes out of bounds
		Then HP is open and CC is off

