investmentAmount = float(input("Enter investment amount: "))
monthlyInterestRate = float(input("Enter annual interest rate: "))
numberOfMonths = float(input("Enter number of years: "))

futureInvestmentAmount = investmentAmount * (1 + monthlyInterestRate / 1200) ** (numberOfMonths * 12)

print("Accumulated value is", futureInvestmentAmount)
