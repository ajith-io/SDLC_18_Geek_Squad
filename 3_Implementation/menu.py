def menu():
    
 print ("[1] : FITNESS ")
 print ("[2] : FINANCE ")
 print ("[3] : EVENT CALENDER ")
 print ("[4] : EXIT THE ASSISTANT ")


def fitness_menu():
    print ("[1] : Exercise" )
    print ("[2]: Calorie Track" )
    print  ("[3]: Go to main menu")   
    
def finance_menu():
    print ("[1]:Revenue")
    print ("[2]: Expense")
    print ("[3]: Summary")
    print ("[4]: GO to Main Menu")

def event_calender_menu():
    print ("[1]: Set Reminder")
    print("[2]: Check Calender")
    print ("{3]: Go to Main Menu")



menu()
option = int (input("Enter Your Option"))

while option!=0:
 if option==1:
    
    fitness_menu()
 elif option==2:
     
  finance_menu()
 elif option==3:
     
    event_calender_menu()
 else:
     print("invalid option")         