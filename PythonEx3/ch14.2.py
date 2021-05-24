def main():
    numbers = [eval(x) for x in input("Enter the numbers: ").split()]

    dict = {}
    for i in numbers:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    max = max(dict.values())
    pairs = list(dict.items())
    items = [[x, y] for (x, y) in pairs]
    
    print("The numbers with the most occurrence are ", end="")
    for (x, y) in items:
        if y == max:
            print(x, end=" ")


main()
