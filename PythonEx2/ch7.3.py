#      UML Diagram
#       Account
# ---------------------------
# -id: int
# -balance: float
# -annualIR: float
# --------------------------- Constructs Object
# getId(): int
# getBalance(): float
# getAnnualIR(): float
# getCur(): float
# getMonthlyInterestRate(): float
# getMonthlyInterest(): float
# setId(id: float): None
# setBalance(balance: float): None
# setAnnualIR(annualIR: float): None
# deposit(amount: float): float
# withdraw(amount: float): str, float

class Account:
    def __init__(self, id=0, balance=100.0, annualIR=0.0):
        self.__id = id
        self.__balance = balance
        self.__annualIR = annualIR

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualIR(self):
        return self.__annualIR

    def getMonthlyInterestRate(self):
        return (self.__annualIR/100) / 12

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def setId(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance

    def setAnnualIR(self, annualIR):
        self.__annualIR = annualIR

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Invalid Transaction"
        self.__balance -= amount
        return self.__balance


def main():
    account = Account(1122, 20000, 4.5)
    account.withdraw(2500)
    account.deposit(3000)
    print("Bank Information:")
    print("Bank Id:", account.getId())
    print("Bank Balance: " + "$" + str(account.getBalance()))
    print("Bank Monthly IR:", account.getMonthlyInterestRate())
    print("Monthly Interest:", account.getMonthlyInterest())


main()
