import math


side = float(input("Enter the number of sides: "))
length = float(input("Enter the length of a side: "))

area = (side * length ** 2)/(4 * math.tan(math.pi/side))

print("The area of the polygon is", area)
