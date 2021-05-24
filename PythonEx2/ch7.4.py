#      UML Diagram
#       Fan
# ---------------------------
# -speed: int
# -on: bool
# -radius: float
# -color: str
# --------------------------- Constructs Object
# getTurnOn(): bool
# getSpeed(): int
# setSpeed(speed: float): None
# geRadius(): float
# seRadius(radius: float): None
# getColor(): str
# setColor(color: str): None

class Fan:

    def __init__(self, speed=1, on=False, radius=5.0, color="blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    def getTurnOn(self):
        return self.__on

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color


def main():
    fan1 = Fan(3, True, 10, "Yellow")
    print("First fan object: ------")
    print("Speed:", fan1.getSpeed())
    print("Radius:", fan1.getRadius())
    print("Color: " + fan1.getColor())
    print("On/Off:", fan1.getTurnOn())
    print()

    fan2 = Fan(2, False, 5, "Blue")
    print("Second fan object: ------")
    print("Speed:", fan2.getSpeed())
    print("Radius:", fan2.getRadius())
    print("Color: " + fan2.getColor())
    print("On/Off:", fan2.getTurnOn())


main()
