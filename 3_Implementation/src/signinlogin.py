#def details():
#    print("Please Enter the required details before we show you the menu")
#    myage = input("Age:")
#    mygender = input("Gender:")
#    myweight = input("Weight(kg):")
#    myheight = input("Height(in cm):")
#    print("We ll get the bmr ratio and user progress using these details")
    #print(myage + "and" + mygender + myweight + myheight)
from datetime import datetime
now = datetime.now()
if now.hour >= 0 and now.hour < 12:
    print("     Good Morning Welcome to our GS Companion")
    print("         ..Always by your side..\n")
elif now.hour >= 12 and now.hour <= 16:
    print("     Good Afternoon Welcome to our GS Companion")
    print("         ..Always by your side..\n")
elif now.hour >= 17 and now.hour <= 19:
    print("     Good Evening Welcome to our GS Companion")
    print("         ..Always by your side..\n")
else:
    print("     Hope you had a Great Day Welcome to our GS Companion")
    print("         ..Always by your side..\n")

def register():
    my_db = open("file.txt", "r")
    my_name = input("    Create Username:")
    my_new_password = input("    Create Password:")
    my_confirm_password = input("    Confirm Password:")
    U = []
    P = []
    for i in my_db:
        u, p = i.split(", ")
        p = p.strip()
        U.append(u)
        P.append(p)
    data = dict(zip(U, P))
    #print(data)

    if my_new_password != my_confirm_password:
        print("    Password dont match, Restart\n")
        register()
    else:
        if len(my_new_password) < 8:
            print("    Password too short minimum length is 8, Restart\n")
            register()
        elif my_name in U:
            print("    Sorry User already exist\n")
            register()
        else:
            my_db = open("file.txt", "a")
            my_db.write(my_name+", "+my_new_password+"\n")
            my_db.close()
            print("    Sucess! "+ my_name +" Your Account has been created sucessfully")
            print("    Now login to your account\n")
            home()

def access():
    my_db = open("file.txt", "r")
    my_name = input("   Username:")
    my_new_password = input("   Password:")

    if not len(my_name or my_new_password) < 1:
        U = []
        P = []
        for i in my_db:
            u, p = i.split(", ")
            p = p.strip()
            U.append(u)
            P.append(p)
        data = dict(zip(U, P))

        try:
            if data[my_name]:
                try:
                    if my_new_password == data[my_name]:
                        print("    ..Login Success..\n")
                        print("    Hi "+ my_name +" We are at your service")
                    else:
                        print("    Password or Username is Incorrect\n")
                        home()
                except:
                    print("    Incorrect Password or Username\n")
                    home()
            else:
                print("    Username doesnt exist\n")
                home()
        except:
            print("    Username doesn't exist Request you to create account\n")
            home()
    else:
        print("    Please Enter a value\n")
        home()

def home(option=None):
    print("        Enter required option")
    print("        A.Signup")
    print("        B.Login")
    option = input("        Option:")
    if option == 'A':
        register()
    elif option == 'B':
        access()
    else:
        print("    Please enter proper option\n")
        home()
home()
