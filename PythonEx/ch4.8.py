import turtle

radius = int(input("Enter the radius: "))

turtle.pensize(4)
turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(radius)

turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(radius)

turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(radius)

turtle.color("green")
turtle.penup()
turtle.goto(55, -85)
turtle.pendown()
turtle.circle(radius)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -85)
turtle.pendown()
turtle.circle(radius)

turtle.mainloop()
