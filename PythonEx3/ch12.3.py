class Account:
    def __init__(self, id=0, balance=100):
        self.__id = id
        self.__balance = balance

    def getId(self):
        return self.__id

    def getBalance(self):
        return format(self.__balance, ".2f")

    def setId(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance


def menuDisplay():
    print()
    print("Main menu")
    print("1: check balance")
    print("2: withdraw")
    print("3: deposit")
    print("4: exit")


def main():
    lst = []
    for i in range(10):
        lst.append(Account(i, 100))

    while True:

        try:
            idNum = int(input("Enter an account id: "))
        except ValueError:
            print("Enter a integer [ex: 1 or 5]!! Not a float[ex: 1.1 or 6.5]\n")
            continue

        if 0 <= idNum <= 9:
            menuDisplay()
            choice = eval(input("Enter a choice: "))

            while choice != 4:
                if choice == 1:
                    user = lst[idNum].getBalance()
                    print("The balance is " + str(user))
                    menuDisplay()
                    choice = eval(input("Enter a choice: "))
                elif choice == 2:
                    take = eval(input("Enter an amount to withdraw: "))
                    lst[idNum].withdraw(take)
                    menuDisplay()
                    choice = eval(input("Enter a choice: "))
                elif choice == 3:
                    insert = eval(input("Enter an amount to deposit: "))
                    lst[idNum].deposit(insert)
                    menuDisplay()
                    choice = eval(input("Enter a choice: "))
                elif choice == 4:
                    break
        else:
            print("\nInvalid ID input.. Enter a ID between [0-9]\n")


main()
