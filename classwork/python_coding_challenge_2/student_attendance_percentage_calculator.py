'''Student Attendance Percentage Calculator 
Problem Statement 
The attendance status of a student for 15 days is represented as follows: 
Sample Data 
attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P') 
Tasks 
1. Count present days.  
2. Count absent days.  
3. Calculate attendance percentage.  
4. Determine whether attendance is below 75%.  
5. Display the attendance status.  
Sample Output 
Present Days: 11 
 
Absent Days: 4 
 
Attendance Percentage: 73.33% 
 
Attendance Status: 
Below 75'''


# Student Attendance Percentage Calculator

# Tuple storing attendance status for 15 days
attendance = (
    'P', 'P', 'A', 'P', 'P',
    'P', 'A', 'A', 'P', 'P',
    'P', 'P', 'A', 'P', 'P'
)

# --------------------------------------------------
# Task 1: Count present days
# --------------------------------------------------

present_days = 0

for day in attendance:
    if day == 'P':
        present_days += 1

print("Present Days:", present_days)

# --------------------------------------------------
# Task 2: Count absent days
# --------------------------------------------------

absent_days = 0

for day in attendance:
    if day == 'A':
        absent_days += 1

print("\nAbsent Days:", absent_days)

# --------------------------------------------------
# Task 3: Calculate attendance percentage
# --------------------------------------------------

total_days = len(attendance)

attendance_percentage = (present_days / total_days) * 100

print("\nAttendance Percentage:", round(attendance_percentage, 2), "%")

# --------------------------------------------------
# Task 4: Determine whether attendance
# is below 75%
# --------------------------------------------------

# --------------------------------------------------
# Task 5: Display attendance status
# --------------------------------------------------

print("\nAttendance Status:")
if attendance_percentage < 75:
    print("Below 75%")
else:
    print("75% or Above")

# --------------------------------------------------
# Task 5: Display attendance status
# --------------------------------------------------
