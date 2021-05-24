def sumMajorDiagonal(m):
    sum = 0
    for i in range(len(m)):
        # initiating a 2D array
        sum += m[i][i]
    return sum


def main():
    matrix = []
    for j in range(4):
        num = [float(i) for i in input("Enter a 4-by-4 matrix row for row " + str(j+1) + ": ").split()]
        matrix.append(num)
    print("Sum of the elements in the major diagonal is", sumMajorDiagonal(matrix))


main()
