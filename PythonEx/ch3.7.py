amount = float(input("Enter an amount, ex) 15.56: "))

change = int(amount * 100)
# penny=1 cent, nickel=5 cents, dime=10 cents and quarter=25 cents.

dollar = change // 100
remain = change % 100

quarter = remain // 25
remain = change % 25

dime = remain // 10
remain = change % 10

nickel = remain // 5
remain = change % 5

penny = remain

print("Your amount", amount, "consists of")
print(dollar, "dollars")
print(quarter, "quarters")
print(dime, "dimes")
print(nickel, "nickels")
print(penny, "pennies")
