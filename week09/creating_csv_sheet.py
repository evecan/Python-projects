product_name = input("enter a product name")
product_price = input("enter the price")
stock = input("enter how many stock")
file_in = open("data.csv", "r")
file_out = open("data.csv", "a")
header = "product name,price,stock\n"
if header not in file_in:# if not header add it
    file_in.close()
    file_out.write(header) #headers
else:
    file_in.close()
file_out.write(f"{product_name},{product_price},{stock}\n")
file_out.close()




