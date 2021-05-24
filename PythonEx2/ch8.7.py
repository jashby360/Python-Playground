def getNumber(uppercaseLetter):
    num = 0
    if uppercaseLetter >= 'W':
        num = 9
    elif uppercaseLetter >= 'T':
        num = 8
    elif uppercaseLetter >= 'P':
        num = 7
    elif uppercaseLetter >= 'M':
        num = 6
    elif uppercaseLetter >= 'J':
        num = 5
    elif uppercaseLetter >= 'G':
        num = 4
    elif uppercaseLetter >= 'D':
        num = 3
    elif uppercaseLetter >= 'A':
        num = 2
    return num


def main():
    number = input("Enter a string(word): ").upper()
    for i in range(len(number)):
        j = number[i]
        k = getNumber(j)
        if k == 0:
            print(j, end="")
        else:
            print(k, end="")


main()
