Feature: HP Fault and Lockout after CC On

Scenario: Testing table data
	Given 	Initial Conditions
		| Parameter | State |
		| R			| ON	|
		| WAIT		| 5		|
		| O1 		| ON	|
		| Y1 		| ON	|
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
			| O1 		| ON	|
			| W1 		| OFF	|
			| HP		| OFF	|
			| LP		| OFF	|
			| FS		| OFF	|
			| CO		| OFF	|
			| LCT		| 88	|
			| DGT		| 100	|
			| DLWT		| 110	|
			| SCT		| 77.5	|
			| WAIT		| 60	|
			
		Then Check final conditions
			| Parameter | State |
			| L			| OFF	|
			| CC 		| ON	|
			| A 		| ON	|
			| O 		| ON	|
			| W2		| OFF	|
			| HWG		| ON	|
			

