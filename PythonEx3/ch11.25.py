def isMarkovMatrix(m):
    for i in range(len(m)):
        sum = 0
        for j in range(len(m)):
            if m[j][i] < 0:
                return False
            sum += m[j][i]
        if sum != 1.0:
            return False
    return True


def main():
    print("Enter a 3-by-3 matrix row by row: ")
    matrix = []
    for i in range(3):
        user = input("Enter a row: ")
        matrix.append([eval(j) for j in user.split()])
    print(matrix)

    if isMarkovMatrix(matrix):
        print("It is a Markov matrix")
    else:
        print("It is not a Markov matrix")


main()
