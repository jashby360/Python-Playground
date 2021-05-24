months = [None, "January", "February", "March", "April", "May",
          "June", "July", "August", "September", "October",
          "November", "December"]

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = int(input("Enter a month in the year: "))
year = int(input("Enter a year: "))

leap = (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

if month == 2 and leap:
    print(months[month], year, "has 29 days")
else:
    print(months[month], year, "has", days[month], "days")
