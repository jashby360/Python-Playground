def printChars(ch1, ch2, numberPerLine):
    count = 0
    for i in range(ord(ch1), ord(ch2) + 1):
        if chr(i).isalnum():
            count += 1
            print(chr(i), end=" ")
        if (i - ord(ch1)) % numberPerLine == numberPerLine - 1:
            print()


printChars('1', 'z', 10)
