def eliminateDuplicates(lst):
    list2 = []
    for num in lst:
        if num not in list2:
            list2.append(num)
    return list2


def main():
    num = [i for i in input("Enter ten numbers: ").split()]
    print("The distinct numbers are:", " ".join(eliminateDuplicates(num)))


main()