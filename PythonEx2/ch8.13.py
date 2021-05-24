def prefix(s1, s2):
    index = 0
    pre = ""

    while s1[index] == s2[index]:
        pre += s1[index]
        index += 1

    if len(pre) > 0:
        print("The common prefix is " + pre)
    else:
        print(s1 + " and " + s2 + " have no common prefix")


def main():
    s1, s2 = input("Enter two string: ").split()
    prefix(s1, s2)


main()
