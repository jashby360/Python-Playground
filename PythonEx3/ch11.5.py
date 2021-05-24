def addMatrix(a, b):
    matrix = []
    for i in range(len(a)):
        c = []
        for j in range(len(b)):
            c.append(a[i][j] + b[i][j])
        matrix.append(c)
    return matrix


def getMatrix(m):
    user = input(m).split()
    m1 = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(eval(user[i * 3 + j]))
        m1.append(row)
    return m1


def printMatrix(m2, sign):
    print("The matrices are added as follows:")
    for row in range(3):
        line = " "
        for mat in range(3):
            m3 = ""
            for column in range(3):
                m3 += format(m2[mat][row][column], ".1f") + " "
                if row == 1 and column == 2:
                    if mat == 0:
                        m3 += " " + sign
                    elif mat == 1:
                        m3 += " ="
            line += format(m3, "<16")
        print(line)


matrix1 = getMatrix("Enter matrix1: ")
matrix2 = getMatrix("Enter matrix2: ")
matrix3 = addMatrix(matrix1, matrix2)
m4 = [matrix1, matrix2, matrix3]
printMatrix(m4, "+")
