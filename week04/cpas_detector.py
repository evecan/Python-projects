# word = input("enter a word")
# if "n" in word:
#     print("n was found")
#
# caps_count = 0
# for char in word:
#     if


MENU = "L) login, S) Sign up, Q) Quit"
valid_username = "eve"
valid_password = "123"

done = False
while True:
    print(MENU)
    user_choice = input("choose [l/s/q]:").lower()
    if user_choice == "l":
        print("logging you in...")
        entered_username = input("enter your username: ")
        entered_password = input("enter your password: ")
        if entered_username == valid_username and entered_password == valid_password:
            print("successful")
            done = True
        else:
            print("invalid ")
            done = True
    elif user_choice == "s":
        print("signing you up...")
    elif user_choice == "q":
        done = True
        print("quitting the program...")
    else:
        print("invalid")
