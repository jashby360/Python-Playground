#      UML Diagram
#       Rectangle
# ---------------------------
# width: float
# height: float
# --------------------------- Constructs Object
# getArea(): float
# getPerimeter(): float

class Rectangle:
    def __init__(self, width=1.0, height=2.0):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)


def main():
    width = 4
    print("The width of the rectangle is: " + str(width))
    height = 40
    print("The height of the rectangle is: " + str(height))

    rect = Rectangle(width, height)
    print("The area of the rectangle is:", rect.getArea())
    print("The perimeter of the rectangle is:", rect.getPerimeter())
    print()

    width = 3.5
    print("The width of the rectangle is: " + str(width))
    height = 35.7
    print("The height of the rectangle is: " + str(height))

    rect = Rectangle(width, height)
    print("The area of the rectangle is:", rect.getArea())
    print("The perimeter of the rectangle is:", rect.getPerimeter())


main()
