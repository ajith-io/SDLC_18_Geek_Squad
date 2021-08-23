from src import workoutplan as w
from src import BMR_calorie_calculator as bmi
try:
    x=bmi.bmi_value()
    print(x)
    if(x<18.5):
        w.printf("Underweight")
        w.workout_1()
    elif (x>=18.5 and x<=24.9):
        w.printf(" Normal")
        w.workout_2()        
    
    elif (x>=25.0 and x<=29.9):
        w.printf(" Overweight")
        w.workout_3()
        
    
    elif (x>=30.0 and x<=34.9):
        w.printf("Obese")
        w.workout_4()
        
    elif(x>34.9):
        w.printf("Extremely obese") 
        w.workout_5()
    else:
        w.printf("We got only 1 to 5 workout plans")
except:
    w.printf("We got only 1 to 5 workout plans")