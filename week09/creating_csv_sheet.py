product_name = input("enter a product name")
product_price = input("enter the price")
stock = input("enter how many stock")
# header
header = "product name,price,stock\n"

file_out = open("data.csv", "a")
# ensure that the header does not exist before you write them
file_in = open("data.csv", "r")
if header not in file_in.readlines()[0]:  # if the first line does not match my headers
    file_in.close()
    file_out.write(header)  # headers
else:
    file_in.close()
# writes data
file_out.write(f"{product_name},{product_price},{stock}\n")
file_out.close()
