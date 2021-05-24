students = int(input("Enter the number of students: "))
highest = 0

for i in range(students):
    grades = float(input("Enter the student's score: "))
    if highest < grades:
        highest = grades
print("\nThe highest score is", highest)