#      UML Diagram
#       Stock
# ---------------------------
# -symbol: str
# -name: str
# -prevPrice: float
# -curPRice: float
# --------------------------- Constructs Object
# getName(): str
# getSymbol(): str
# getPrev(): float
# getCur(): float
# setName(name: str): None
# setSymbol(symbol: str): None
# setPrev(prevPrice: float): None
# setCur(curPrice: float): None
# getChangePercent(): int


class Stock:
    def __init__(self, symbol, name, prevPrice, curPrice):
        self.__symbol = symbol
        self.__name = name
        self.__prevPrice = prevPrice
        self.__curPrice = curPrice

    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

    def getPrev(self):
        return self.__prevPrice

    def getCur(self):
        return self.__curPrice

    def setName(self, name):
        self.__name = name

    def setSymbol(self, symbol):
        self.__symbol = symbol

    def setPrev(self, prevPrice):
        self.__prevPrice = prevPrice

    def setCur(self, curPrice):
        self.__curPrice = curPrice

    def getChangePercent(self):
        return (self.__curPrice - self.__prevPrice) / self.__prevPrice * 100


def main():
    stock = Stock("INTL", "Intel Corporation", 20.5, 20.35)
    print("Stock Information:")
    print("Stock Symbol:", stock.getSymbol())
    print("Company Name:", stock.getName())
    print("Previous Price:", stock.getPrev())
    print("Current Price:", stock.getCur())
    print("Price Change:", format(stock.getChangePercent(), ".3f") + "%")


main()
