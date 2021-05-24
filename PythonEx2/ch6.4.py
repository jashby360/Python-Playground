def reverse(number):
    integer = 0
    while number > 0:
        num = number % 10
        integer = integer * 10 + num
        number //= 10
    return integer


def main():
    num = int(input("Enter an integer: "))
    print("The reverse number is:", reverse(num))


main()
