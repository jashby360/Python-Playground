def gcd(numbers):
    result = numbers[0]
    for x in numbers[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result


def main():
    lst = [float(i) for i in input("Enter five numbers: ").split()]
    print(gcd(lst))


main()
