def formats(number, width):
    num = str(number)
    i = width - len(num)
    return '0' * i + num


def main():
    number = eval(input("Enter an integer: "))
    width = eval(input("Enter the width: "))

    print("The formatted number is:", formats(number, width))


main()
