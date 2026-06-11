''': School Report Card Generator 
Problem Statement 
Student marks are stored in marks.txt. 
Sample Input/Data (marks.txt) 
S101,Anuj,92 
S102,Rahul,76 
S103,Priya,88 
S104,Neha,45 
S105,Amit,58 
S106,Sneha,95 
S107,Karan,81 
S108,Pooja,73 
S109,Rohit,39 
S110,Anjali,90 
Tasks 
1. Calculate grades for all students.  
Passed Students: 9 
Failed Students: 1 
2. Generate a report card file report_card.txt.  
3. Display topper details.  
4. Count pass and fail students.  
5. Display students eligible for merit certificates (marks ≥ 90).  
Sample Output 
Topper: 
Sneha (95) 
 
Merit Certificate Holders: 
Anuj 
Sneha 
Anjali 
 
Report Cards Generated Successfully'''

# School Report Card Generator

# --------------------------------------------------
# Task 1: Calculate grades for all students
# --------------------------------------------------

# Open file in read mode
file = open("marks.txt", "r")

# Variables for topper and pass/fail count
topper_name = ""
topper_marks = 0

pass_count = 0
fail_count = 0

# List to store merit certificate holders
merit_students = []

# Open report card file in write mode
report_file = open("report_card.txt", "w")

# Traverse all student records
for record in file:

    # Remove newline character
    record = record.strip()

    # Split record into fields
    sid, name, marks = record.split(",")

    marks = int(marks)

    # --------------------------------------------------
    # Calculate Grade
    # --------------------------------------------------
    if marks >= 90:
        grade = "A+"

    elif marks >= 80:
        grade = "A"

    elif marks >= 70:
        grade = "B"

    elif marks >= 60:
        grade = "C"

    elif marks >= 40:
        grade = "D"

    else:
        grade = "F"

    # --------------------------------------------------
    # Count Pass and Fail Students
    # --------------------------------------------------
    if marks >= 40:
        pass_count += 1
    else:
        fail_count += 1

    # --------------------------------------------------
    # Find Topper
    # --------------------------------------------------
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name

    # --------------------------------------------------
    # Find Merit Certificate Holders
    # --------------------------------------------------
    if marks >= 90:
        merit_students.append(name)

    # --------------------------------------------------
    # Write Report Card to File
    # --------------------------------------------------
    report_file.write(
        sid + "," + name + "," + str(marks) + "," + grade + "\n"
    )

# Close files
file.close()
report_file.close()

# --------------------------------------------------
# Task 2: Display Topper Details
# --------------------------------------------------
print("Topper:")
print(topper_name, "(", topper_marks, ")", sep="")

# --------------------------------------------------
# Task 3: Count Pass and Fail Students
# --------------------------------------------------
print("\nPassed Students:", pass_count)
print("Failed Students:", fail_count)

# --------------------------------------------------
# Task 4: Display Merit Certificate Holders
# --------------------------------------------------
print("\nMerit Certificate Holders:")

for student in merit_students:
    print(student)

# --------------------------------------------------
# Task 5: Report Generation Message
# --------------------------------------------------
print("\nReport Cards Generated Successfully")
