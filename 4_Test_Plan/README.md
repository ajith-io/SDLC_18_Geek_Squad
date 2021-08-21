# TEST PLAN:

## High level test plan

| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  `H_01`       |Get Proper User Details |  String and integer | User detail stored as string and interger|String and integer stored|Requirement based |
|  `H_02`       |After signing in| String value as mentioned in menu |shows main menu |Select you option A.Fitness B.Finanace C.Event calendar D: Exit the assistant |Scenario based |
|`H_03`  | If you select A.Fitness |**A**|Display another menu |Display A.Exercise B.Calorie Track C: Exit the assistant | Requirement based|
|`H_04`  | If you select B.Finance |**B**|Display another menu |Display A.Revenue B.Expense C.Summary D:Exit the assistant  | Requirement based|
|`H_05`  | If you select C.Events Calendar |**C**| Display another menu| Display A.Set Reminder B.Check Calendar C:exit the assistant | Requirement based|

## Low level test plan

|**Test ID** | **HLT ID** | **Description** | **Exp I/P** | **Exp O/P** | **Actual Out** | **Type of test**|
|--------|--------|-------------|---------|---------|------------|-------------|
|`L_01`  |`H_03`  | When you select A.Exercise |A| Display Fitness Track |  | Requirement based|
|`L_02` | `H_03` | When you select B.Claorie Track |B| Meal and calorie content details| | Requirement based|
|`L_03` | `H_04` | When you select A.Revenue |A| Add in database| | Requirement based|
|`L_04` | `H_04` | When you select B.Expense |B| Add in database| | Requirement based|
|`L_05` | `H_04` | When you select C.Summary |C| Add in database| | Scenario based|
|`L_06` | `H_05` | When you select A.Set a Reminder |A| Reminder Details added in database| | Requirement based|
|`L_07` | `H_05` | When you select B.Check Calendar |B| Display Calendar| | Scenario based|
