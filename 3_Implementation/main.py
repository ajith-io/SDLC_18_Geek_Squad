from src import workoutplan as w
try:
    select = int(input(w.printf("Select a workout plan")))
    #select will get its value from database here for demo choose from 1 to 5 
    if(select==1):
        w.workout_1()
    elif(select==2):
        w.workout_2()
    elif(select==3):
        w.workout_3()
    elif(select==4):
        w.workout_4()
    elif(select==5):
        w.workout_5()
    else:
        w.printf("We got only 1 to 5 workout plans")
except:
    w.printf("We got only 1 to 5 workout plans")