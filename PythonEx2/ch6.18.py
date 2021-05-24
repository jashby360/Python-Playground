import random


def printMatrix(n):
    for i in range(0, n):
        for j in range(0, n):
            matrix2DArray = random.randint(0, 1)
            print(matrix2DArray, end=" ")
        print()


def main():
    num = int(input("Enter n: "))
    printMatrix(num)


main()
