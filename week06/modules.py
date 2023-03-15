import random
import string
import time

random_number = random.randint(0, 100)  # generate a random number between what ever u want
print("random number: ", random_number)

letters = string.ascii_letters  # alphabet letters upper & lowercase
digits = string.digits  # numbers from 0-9
symbol = string.punctuation  # all special characters/symbols
character = letters + digits + symbol  # all the above

# ===========================================================================================
print("letters: ", letters)
print("digits: ", digits)
print("symbol: ", symbol)
print("characters: ", character)

random_letters = random.choice(letters)  # pick a random letters
random_digits = random.choice(digits)  # pick a random digit
random_symbol = random.choice(symbol)  # pick a random symbol
random_character = random.choice(character)  # all the above
# =======================================================================================
print("random letter: ", random_letters)
print("random digit: ", random_digits)
print("random symbol: ", random_symbol)
print("random character: ", random_character)

character_limit = 50
my_word = ""
for char in range(character_limit):
    my_word += random.choice(character)
print("words: ", my_word)

print("i'm quick")
time.sleep(1)  # delay
print("3")
time.sleep(2)
print("2")
time.sleep(3)
print("1")
time.sleep(3)
print("i'm taking my time")
print("please wait this will take a while")

print("processing", end="")
for i in range(10):
    time.sleep(1)
    print(f"\r {(i * 10) + 10}%",
          end="")  # print("\r", i, end="")#print(f".", end="")#print(f"\r {(i*10)+10}%", end="")
print("\ncomplete!")
