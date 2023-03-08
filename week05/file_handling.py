#01

file_out = open("file.txt", "w")  # create a file for the purpose of re-writing
file_out.write("hi this is from file_handling.\n ")
file_out.write("hi im pomu\n ")
file_out.write("hi this is rtioywibv\n ")
file_out.write("hi this is wjfvnkwjboo2bv\n ")
file_out.write("hi this is uqgvdivqobvbqoebvqobnvoq\n ")
file_out.close()

#02
# create a file for the purpose of appending (adding to existing content)
# file_out_02 = open("file_append.txt", "a")
# file_out_02.write("hi im pomu\n ")
# file_out_02.write("hi this is rtioywibv\n ")
# file_out_02.write("hi this is wjfvnkwjboo2bv\n ")
# file_out_02.write("hi this is uqgvdivqobvbqoebvqobnvoq\n ")
# file_out_02.close()

#03
# open a file for the purpose of reading
file_in = open("file.txt", "r")
print(file_in.read())
file_in.close()

phonebook_dic = {}
phonebook_file = open("phonebook.txt", "r")


for line in phonebook_file:
    name, phone = line.split(" ")
    phone.rstrip()# use .rstrip() to clean up spaces after each line
    phonebook_dic[name] = phone.rstrip()# add n associate a name with a phonenumber in the dic
phonebook_file.close()

print(phonebook_dic)
print("john's phone number is", phonebook_dic["John"])

for name, phone in phonebook_dic.items():
    # print("name:", name, "- phone:", phone)
    print(f"name: {name:10s} phone: {phone:>10s}")