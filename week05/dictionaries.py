my_dictionary = {"firstname": "john",
                 "lastname": "Smith",
                 "postcode": 2000,
                 "age": 40,
                 "country": "Australia"}

keys = my_dictionary.keys()
print(keys)  # the keys of a dictionary

value = my_dictionary.values()
print(value)  # the value of a dictionary

items = my_dictionary.items()
print(items)  # the items of a dictionary

the_one = my_dictionary["firstname"]
print(the_one)  # the value of a specific key in a dictionary

# add a new item(pair) to the dictionary
my_dictionary["phone"] = "040506070809"
print(my_dictionary)

# use for loop with .items() to neatly display keys n values of the dictionary
for my_keys, my_value in my_dictionary.items():
    print(my_keys, my_value, sep=": ")

print(my_dictionary["postcode"])
# variable =
# print(type(variable))
