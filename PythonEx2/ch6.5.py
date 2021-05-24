def displaySortedNumbers(num1, num2, num3):
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1
    return float(num1), float(num2), float(num3)


def main():
    a, b, c = input("Enter three numbers: ").split()
    print("The sorted numbers are", displaySortedNumbers(a, b, c))


main()
