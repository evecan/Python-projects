MENU = "l) Login, q) Quit"
# MENU is in caps, and it means it's a CONSTANT
# The CONSTANT is a variable that never changes its value

print(MENU)
valid_username ="eve"
valid_password ="123"
user_choice = input("Choose [l/q]: ")

if user_choice == "l":
    print(input("enter your name:"))
    print("logging in....")
    entered_username = input("enter your username: ")
    entered_password = input("enter your password: ")
#we use *and* so that you need both username and password to successfull login
# if we use *or* you only need to get either username or password one of them to login
    if entered_username == valid_username and entered_password == valid_password:
        print("WELCOME")
    else:
        print("error")

elif user_choice == "q":
    print("quitting program...")
else:
    print("please enter l or q" )






