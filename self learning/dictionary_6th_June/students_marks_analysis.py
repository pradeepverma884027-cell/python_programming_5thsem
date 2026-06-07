'''
Student Marks Analysis
'''

# Dictionary storing student names and their marks
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# ---------------------------------------------------
# Task 1: Display students scoring 80 or above
# ---------------------------------------------------

print("Students having score 80 or above:")

# Traverse dictionary and check marks
for student, mark in marks.items():

    # Display student name if marks are 80 or above
    if mark >= 80:
        print(student)

print("-------------------------------------")

# ---------------------------------------------------
# Task 2: Count students who failed (marks < 40)
# ---------------------------------------------------

print("Number of students who failed:")

# Counter variable for failed students
count = 0

# Traverse only the marks
for mark in marks.values():

    # Check if marks are below 40
    if mark < 40:
        count += 1

# Display count of failed students
print(count)

print("--------------------------------------")

# ---------------------------------------------------
# Task 3: Find the highest scorer
# ---------------------------------------------------

print("The highest scorer is:")

# Assume highest marks are 0 initially
highest_marks = 0

# Traverse dictionary
for student, score in marks.items():

    # Update highest marks and student name
    if score > highest_marks:
        highest_marks = score
        highest_student = student

# Display highest scorer and marks
print(highest_student, ":", highest_marks)

print("-------------------------------------")

# ---------------------------------------------------
# Task 4: Create a list of students
# scoring between 60 and 75
# ---------------------------------------------------

# Empty list to store student names
students = []

print("Students scoring between 60 and 75:")

# Traverse dictionary
for student, mark in marks.items():

    # Check if marks are between 60 and 75 (inclusive)
    if 60 <= mark <= 75:
        students.append(student)

# Display the list
print(students)

print("-------------------------------------")

# ---------------------------------------------------
# Task 5: Assign grades
# ---------------------------------------------------

'''
Grade Criteria:
A : >= 90
B : 75 - 89
C : 50 - 74
F : < 50
'''

print("Grades:")

# Traverse dictionary
for student, mark in marks.items():

    # Grade A
    if mark >= 90:
        print(student, "-> Grade A")

    # Grade B
    elif mark >= 75:
        print(student, "-> Grade B")

    # Grade C
    elif mark >= 50:
        print(student, "-> Grade C")

    # Grade F
    else:
        print(student, "-> Grade F")
