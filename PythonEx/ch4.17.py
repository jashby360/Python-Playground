import math
import turtle

radius = int(input("Enter the radius of the bounding circle: "))

corner = radius * math.sin(math.radians(72)), radius * math.cos(math.radians(72))
corner1 = radius * math.sin(math.radians(0)), radius * math.cos(math.radians(0))
corner2 = radius * math.sin(math.radians(288)), radius * math.cos(math.radians(288))
corner3 = radius * math.sin(math.radians(216)), radius * math.cos(math.radians(216))
corner4 = radius * math.sin(math.radians(144)), radius * math.cos(math.radians(144))

print(corner, '\n', corner1, '\n', corner2, '\n', corner3, '\n', corner4)

turtle.forward(100)
turtle.left(72.5)
turtle.write(corner)

turtle.forward(100)
turtle.left(72.5)
turtle.write(corner1)

turtle.forward(100)
turtle.left(72.5)
turtle.write(corner2)

turtle.forward(100)
turtle.left(72.5)
turtle.write(corner3)

turtle.forward(100)
turtle.left(72.5)
turtle.write(corner4)

turtle.mainloop()
