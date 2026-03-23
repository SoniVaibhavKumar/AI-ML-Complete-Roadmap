username = input("Enter Username: ")
password = input("Enter password: ")
if (username == "admin" and password == "admin"):
    print("Success")
else :
    if (username != "admin"):
        print("Wrong username")
    else:
        print("wrong password")