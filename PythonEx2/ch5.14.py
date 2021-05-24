import math

n = int(input("Enter a integer: "))

square = int(math.pow(n, 2))  # square ex) n^2
while square < 12000:
    n += 1
print("The N^2 integer:", square)
