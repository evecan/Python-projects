# functions      def=definition

# 01
def my_calculator():
    print(5 * 5)


my_calculator()


# 02
def ask_for_name():
    name = input("enter your name:")
    print("hello", name )


ask_for_name()


# 03
def verify_age():
    age = int(input("enter your age:"))
    if age >= 18:
        print("you are an adult")
    else:
        print("you are a minor")


verify_age()


# 03
def welcome(someone):
    print("welcome", someone, "nice to see you here.")


welcome("eve")


# 04
def is_adult(u_age):
    if u_age >= 18:
        return True
    else:
        return False


if is_adult(10):
    print("welcome")
else:
    print("sorry")

# 05
# number is outside
number = 20


# number is in the function
def multiply_by_five(number):
    return 5 * number


# use number that is outside not the one in the function
print(multiply_by_five(number))


# 06
def is_successful(result):
    if result >= 50:
        return True
    else:
        return False


my_result = int(input("enter your result:"))
if is_successful(my_result):
    print("you passed")
else:
    print("you failed")
