def count(s, ch):
    counter = 0
    for i in s:
        if i == ch:
            counter += 1
    return counter


def main():
    string = input("Enter a string(word): ").upper()
    char = input("enter a single character: ").upper()

    print(count(string, char))


main()
