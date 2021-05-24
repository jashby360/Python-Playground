weight = float(input("Enter weight for package 1: "))
price = float(input("Enter price for package 1: "))
weight1 = float(input("Enter weight for package 2: "))
price1 = float(input("Enter weight for package 2: "))

if price > price1:
    print("Package 2 has the best price")
elif price == price1:
    print("Both package are equal in price")
else:
    print("Package 1 has the best price")
