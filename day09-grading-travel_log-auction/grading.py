student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# Create an empty dictionary called student_grades.
student_grades = {}

# Write your code below to add the grades to student_grades.👇
for k, v in student_scores.items():

    if v > 90:
        grade = "Outstanding"
    elif v > 80:
        grade = "Exceeds Expectations"
    elif v > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[k] = grade

# --or-- more in line with what was taught:
# for student in student_score:
# if student_scores[student] == 100:
#     ...


# 🚨 Don't change the code below 👇
print(student_grades)
