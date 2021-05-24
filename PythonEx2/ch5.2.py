import time
import random

start = time.time()
correctAns = 0
count = 0

# number of questions to be 10 times
while count < 10:
    # returns a number between 1 and 15 (both included)
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)

    print("What is", num1, "+", num2, " ?")
    answer = int(input())

    if num1 + num2 == answer:
        print("You're correct")
        correctAns += 1
    else:
        print("Your answer is wrong")
    count += 1
end = time.time()
overall = end - start
print("\nThe correct count is:", correctAns)
print("Test time is:", float(overall/1000))
