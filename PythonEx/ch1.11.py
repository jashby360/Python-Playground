population = 312032486
years = 365 * 60 * 60 * 24
birth = years / 7
death = years / 13
immigrant = years / 45

census1 = int(population + 1 * (birth - death + immigrant))
census2 = int(population + 2 * (birth - death + immigrant))
census3 = int(population + 3 * (birth - death + immigrant))
census4 = int(population + 4 * (birth - death + immigrant))
census5 = int(population + 5 * (birth - death + immigrant))

print("Year 1:", census1)
print("Year 2:", census2)
print("Year 3:", census3)
print("Year 4:", census4)
print("Year 5:", census5)
