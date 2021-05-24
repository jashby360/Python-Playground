from math import sqrt


#      UML Diagram                          UML Diagram
#    GeometricObject                          Triangle
# ---------------------------        ---------------------------
# -color: str                              -side1: float
# -filled: bool                            -side2: float
#                                          -side3: float
#      Constructs Object                  Constructs Object
# ---------------------------        ---------------------------
# getColor(): str                          getSide1(): float
# setColor(color: str): None               getSide2(): float
# isFilled(): bool                         getSide3(): float
# setFilled(filled: bool): None            getArea(): float
#                                          getPerimeter(): float

class GeometricObject:

    def __init__(self, color="blue", filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        "color: " + self.__color + " and filled: " + str(self.__filled)


class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def getArea(self):
        perimeter = self.getPerimeter() / 2
        p1 = perimeter - self.__side1
        p2 = perimeter - self.__side2
        p3 = perimeter - self.__side3
        return sqrt(perimeter * p1 * p2 * p3)

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(
            self.__side3)


if __name__ == '__main__':
    side1 = float(input("Enter side1: "))
    side2 = float(input("Enter side2: "))
    side3 = float(input("Enter side3: "))
    color = input("Enter a color: ")
    filled = input("Enter filled (ex: True or False): ")
    triangle = Triangle(side1, side2, side3)
    triangle.setColor(color)
    triangle.setFilled(filled)

    print()
    print("Area: " + str(triangle.getArea()))
    print("Perimeter: " + str(triangle.getPerimeter()))
    print("Color: " + triangle.getColor())
    print("IsFilled?: " + str(triangle.isFilled()))
