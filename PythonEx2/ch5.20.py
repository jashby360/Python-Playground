print("Patter A")
for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPatter B")
for i in range(6, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPatter C")
for i in range(1, 7):
    num = 1
    for j in range(6, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print(num, end=" ")
            num += 1
    print()

print("\nPatter D")
for i in range(6, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
