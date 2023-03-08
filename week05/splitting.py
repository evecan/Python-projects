"""you can use the split() method to extract data based on a seperator (like space)"""

record = "john 045796589"
name, phone = record.split(" ")
print("hi", name, "your number is", phone)
