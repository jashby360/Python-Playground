import math

num = float(input("Enter the x-coordinate for point1: "))
num1 = float(input("Enter the y-coordinate for point1: "))
num2 = float(input("Enter the x-coordinate for point2: "))
num3 = float(input("Enter the y-coordinate for point2: "))
num4 = float(input("Enter the x-coordinate for point3: "))
num5 = float(input("Enter the y-coordinate for point3: "))

side1 = math.sqrt(math.pow(num - num2, 2) + math.pow(num1 - num3, 2))
side2 = math.sqrt(math.pow(num2 - num4, 2) + math.pow(num3 - num5, 2))
side3 = math.sqrt(math.pow(num - num4, 2) + math.pow(num1 - num5, 2))

s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s-side1) * (s-side2) * (s-side3))
print("The area of the triangle is", area)
