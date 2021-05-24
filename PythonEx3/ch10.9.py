from statistics import stdev, mean


def main1():
    lst = [float(i) for i in input("Enter numbers: ").split()]
    num = mean(lst)
    num1 = stdev(lst)
    print("The mean is:", round(num, 2))
    print("The standard deviation is:", round(num1, 5))


main1()
