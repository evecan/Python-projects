user_choice = input("enter l(login) or q(quit): ")


# while user_choice != "q":
#     if user_choice == "l":
#         print("logging in...")
#         break #stops the infinite loop
#     else:
#         user_choice = input("enter either l(login) or q(quit): ")
# # forces you to say yes
# answer = input("yes or yes: ")
# while answer != "yes":
#     answer =input("yes or yes: ")


def get_user_choice():
    # print("type l(login) s(sign_up) q (quit): ")
    user_choice = input("choose [l/s/q]: ").lower()
    if user_choice == "l":
        print("logging in ...")
    elif user_choice == "s":
        print("signing you up...")
    return user_choice


while get_user_choice() != "q":
    get_user_choice()
else:
    print("quitting...")
