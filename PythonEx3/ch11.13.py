def locateLargest(a):
    large = [0, 0]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > a[large[0]][large[1]]:
                large = [i, j]
    return large


def main():
    rows = eval(input("Enter the number of rows in the list: "))
    matrix = []
    for i in range(rows):
        user = input("Enter a row: ")
        matrix.append([eval(j) for j in user.split()])
    a = locateLargest(matrix)
    print("The location of the largest element is at (" +
          str(a[0]) + ", " + (str(a[1])) + ")")


main()
