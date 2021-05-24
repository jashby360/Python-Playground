import random

print("Enter 0 for head and 1 for tail")
prob = int(input("Guess head or tail? "))

flip = random.randint(0, 1)

if prob == flip:
    print("Correct guess")
elif prob == 0:
    print("Sorry, it is a tail")
    print("Flip value: " + str(flip))
else:
    print("Sorry, it is head")
    print("Flip value: " + str(flip))
