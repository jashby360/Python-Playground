import turtle


def drawChessboard(startx, endx, starty, endy):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(startx, starty)
    turtle.pendown()
    turtle.color("black")

    for i in range(4):
        turtle.forward(240)
        turtle.left(90)

    drawRectangle(startx, endx, starty, endy)
    drawRectangle(startx + 30, endx, starty + 30, endy)


def drawRectangle(startx, endx, starty, endy):
    turtle.color("black")
    for j in range(starty, endy, 60):
        for i in range(startx, endx, 60):
            drawAllRectangles(i, j)


def drawAllRectangles(i, j):
    turtle.penup()
    turtle.goto(i, j)
    turtle.pendown()
    turtle.begin_fill()
    for k in range(4):
        turtle.forward(30)
        turtle.left(90)
    turtle.end_fill()


def main():
    drawChessboard(-260, -20, -120, 120)
    drawChessboard(20, 260, -120, 120)

    turtle.done()


main()
