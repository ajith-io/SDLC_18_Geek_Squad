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
                        w.printf("    ..Login Success..\n")
                        w.printf("    Hi "+ my_name +" We are at your service")
                        
                        
                    else:
                        w.printf("    Password or Username is Incorrect\n")
                        home()
                except:
                    w.printf("    Incorrect Password or Username\n")
                    home()
            else:
                w.printf("    Username doesnt exist\n")
                home()
        except:
            w.printf("    Username doesn't exist Request you to create account\n")
            home()
    else:
        w.printf("    Please Enter a value\n")
        home()

def home(option=None):
    w.printf("        Enter required option")
    w.printf("        A.Signup")
    w.printf("        B.Login")
    option = input("        Option:")
    if option == 'A':
        register()
    elif option == 'B':
        access()
    else:
        w.printf("    Please enter proper option\n")
        home()

