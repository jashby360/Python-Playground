import turtle

c = int(input("Enter the radius: "))

turtle.down()
turtle.circle(c)

turtle.penup()
turtle.setposition(-(c * 2), 0)
turtle.pendown()
turtle.circle(c)

turtle.penup()
turtle.setposition(0, -(c * 2))
turtle.pendown()
turtle.circle(c)

turtle.penup()
turtle.setposition(-(c * 2), -(c * 2))
turtle.pendown()
turtle.circle(c)

turtle.mainloop()
