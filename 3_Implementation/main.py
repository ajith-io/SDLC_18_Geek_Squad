from src import workoutplan as w
from src import BMR_calorie_calculator as bmi
from src import menu as m
import databas as d
from src import signinlogin as si
try:
    si.start()
    si.home()
    option=m.menu()
    if option==1:
    
        b=m.fitness_menu()
        if(b==1):
            bmi.bmi_value()
            w.assign()


    elif option==2:
        
        m.finance_menu()
    elif option==3:
        
        m.event_calender_menu()
    else:
        w.printf("invalid option")    
    
    
except:
    w.printf("We got only 1 to 5 workout plans")

