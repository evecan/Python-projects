# name = "efeng"

try:
    print(name)
except:  # there are different types of error for example NameError
    print("this variable name has not been define yet!")

number = input("enter a number")
try:
    number = int(number)
    print(number, "is a valid number")
except ValueError:
    print("you did not enter a number!")
