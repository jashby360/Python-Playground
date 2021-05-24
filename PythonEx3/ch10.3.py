def count(lst):
    lst1 = []
    for i in lst:
        if i not in lst1:
            lst1.append(i)
            if lst.count(i) > 1:
                print("{} occurs {} times".format(i, lst.count(i)))
            else:
                print("{} occurs {} time".format(i, lst.count(i)))


def main():
    num = [int(i) for i in input("Enter integers between 1 and 100: ").split()]
    count(sorted(num))


main()

