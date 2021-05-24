class Location:
    def __init__(self, row=0, column=0, maxValue=0.0):
        self.__row = row
        self.__column = column
        self.__maxValue = maxValue

    def getRow(self):
        return self.__row

    def getColumn(self):
        return self.__column

    def getMaxValue(self):
        return self.__maxValue


def locateLargest(a):
    maxValue = a[0][0]
    row = 0
    column = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if maxValue < a[i][j]:
                maxValue = a[i][j]
                row = i
                column = j
    return Location(row, column, maxValue)


def main():
    rows, columns = eval(input("Enter the number of rows and columns in the list: "))
    matrix = []
    for i in range(rows):
        user = input("Enter a row " + str(i) + ": ")
        for k in range(columns):
            matrix.append([eval(j) for j in user.split()])

    location = locateLargest(matrix)
    l1 = str(location.getMaxValue())
    l2 = str(location.getRow())
    l3 = str(location.getColumn())
    print("The location of the largest element is {} at ({},{})".format(l1, l2, l3))


main()
