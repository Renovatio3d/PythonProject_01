Sys_User_Name = "Jeffnah"
Sys_Password = "1229"

Attempts = 3
while True:
    User_Name = input("Please enter user name: ")
    User_Password = input("Please enter your password: ")
if User_Name != Sys_User_Name and User_Password == Sys_Password:
    print("Wrong user name..")
    Attempts = -1
elif User_Name == Sys_User_Name and User_Password != Sys_Password:
    print("Wrong password..")
    Attempts =-1
elif User_Name != Sys_User_Name and User_Password != Sys_Password:
    print("Wrong user name and password..")
    Attempts =-1

