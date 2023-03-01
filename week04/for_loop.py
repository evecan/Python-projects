#01
cars = ["BMW", "Mercedes", "Ford"]

for car in cars:
    print("Car:", car)
#02
# goes vertically
for times in range(3):
    print("hello\nHow are you?")  # \n=enter

# goes horrizontally
for letter in range(10):
    # can add something behind x by typing in end
    print("x", end="")

word = input("\nenter a word:")

#ctrl+- = minimize only works for def(definition)
def a_to_h():
    if letter == "a":
        print("the letter a was found in you word")
    elif letter == "b":
        print("the letter b was found in you word")
    elif letter == "c":
        print("the letter c was found in you word")
    elif letter == "d":
        print("the letter d was found in you word")
    elif letter == "e":
        print("the letter e was found in you word")
    elif letter == "f":
        print("the letter f was found in you word")
    elif letter == "g":
        print("the letter g was found in you word")
    elif letter == "h":
        print("the letter h was found in you word")


for letter in word:
    a_to_h()
