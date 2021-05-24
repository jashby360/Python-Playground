def getPentagonalNumber(n):
    return int(n * (3 * n - 1) / 2)


def main():
    for i in range(1, 100, 10):
        for j in range(i, i + 10):
            print(format(getPentagonalNumber(j), "5d"), end=" ")
        print()


main()
