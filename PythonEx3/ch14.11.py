import os
import sys


def main():
    filename = input("Enter a text filename: ").strip()

    if not os.path.isfile(filename):
        print("File", filename, "does not exist")
        sys.exit()

    file = open(filename, "r")
    processLine(file)


# Count each word in the line
def processLine(file):
    vowels = set("AEIOUaeiou")
    consonant = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

    vow = 0
    con = 0
    for ch in file.read():
        if ch in vowels:
            vow += 1
        elif ch in consonant:
            con += 1
    print("The number of Vowels is:", vow)
    print("The number of consonants is:", con)


main()  # Call the main function
