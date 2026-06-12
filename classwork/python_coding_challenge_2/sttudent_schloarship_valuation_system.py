# Student Scholarship Evaluation System

# Dictionary storing student names and their marks
marks = {
    "Anuj": 92,
    "Rahul": 76,
    "Priya": 88,
    "Neha": 64,
    "Amit": 58,
    "Sneha": 95,
    "Karan": 81,
    "Pooja": 73,
    "Rohit": 47,
    "Anjali": 90
}

# --------------------------------------------------
# Task 1: Display students scoring above 85 marks
# --------------------------------------------------

print("Students Scoring Above 85:")

# Traverse the dictionary and check marks
for student, score in marks.items():
    if score > 85:
        print(student)

# --------------------------------------------------
# Task 2: Find the topper
# --------------------------------------------------

# Assume the first student is the topper initially
topper = list(marks.keys())[0]
highest_marks = marks[topper]

# Compare marks of all students
for student, score in marks.items():
    if score > highest_marks:
        highest_marks = score
        topper = student

print("\nTopper:")
print(topper, f"({highest_marks})")

# --------------------------------------------------
# Task 3: Find the student with the lowest marks
# --------------------------------------------------

# Assume the first student has the lowest marks initially
lowest_student = list(marks.keys())[0]
lowest_marks = marks[lowest_student]

# Compare marks of all students
for student, score in marks.items():
    if score < lowest_marks:
        lowest_marks = score
        lowest_student = student

print("\nLowest Scorer:")
print(lowest_student, f"({lowest_marks})")

# --------------------------------------------------
# Task 4: Calculate class average marks
# --------------------------------------------------

total_marks = 0

# Add marks of all students
for score in marks.values():
    total_marks += score

# Calculate average
average_marks = total_marks / len(marks)

print("\nAverage Marks:", average_marks)

# --------------------------------------------------
# Task 5: Generate grades
# A (90+)
# B (75–89)
# C (50–74)
# F (<50)
# --------------------------------------------------

print("\nStudent Grades:")

for student, score in marks.items():

    if score >= 90:
        grade = "A"

    elif score >= 75:
        grade = "B"

    elif score >= 50:
        grade = "C"

    else:
        grade = "F"

    print(student, ":", grade)

# --------------------------------------------------
# Task 6: Create a list of scholarship students
# (Marks greater than or equal to 90)
# --------------------------------------------------

scholarship_students = []

# Check eligibility for scholarship
for student, score in marks.items():
    if score >= 90:
        scholarship_students.append(student)

print("\nScholarship Students:")
print(scholarship_students)
