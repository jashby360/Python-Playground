ssn = input("Enter a SSN(ddd-dd-dddd): ").split('-')

if len(ssn) == 3:
    if len(ssn[0]) == 3 and len(ssn[1]) == 2 and len(ssn[2]) == 4:
        print("Valid SSN")
    else:
        print("Invalid SSN")
