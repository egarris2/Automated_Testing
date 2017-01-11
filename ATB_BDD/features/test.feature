Feature: HP Fault and Lockout after CC On

Scenario: Testing table data
	Given 	Initial Conditions
		| Parameter | State |
		| R			| ON	|
		| WAIT		| 5		|
		| Y1 		| ON	|
		| O 		| OFF	|
		| W1 		| OFF	|
		| HP		| OFF	|
		| LP		| OFF	|
		| FS		| OFF	|
		| CO		| OFF	|
		| LCT		| 88	|
		| DGT		| 188	|
		| DLWT		| 88	|
		| SCT		| 77.5	|
		| WAIT		| 5		|
	
		When Conditions change
			| Parameter | State |
			| R			| ON	|
			| Y1 		| ON	|
			| O 		| OFF	|
			| W1 		| OFF	|
			| HP		| ON	|
			| LP		| OFF	|
			| FS		| OFF	|
			| CO		| OFF	|
			| LCT		| 88	|
			| DGT		| 188	|
			| DLWT		| 88	|
			| SCT		| 77.5	|
			| WAIT		| 40	|
			
		Then Check final conditions
			| Parameter | State |
			| L			| ON	|
			| CC 		| OFF	|
			| A 		| OFF	|
			| O 		| OFF	|
			| W2		| OFF	|
			| HWG		| OFF	|
			

