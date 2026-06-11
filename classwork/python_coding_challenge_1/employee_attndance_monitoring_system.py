''' Employee Attendance Monitoring System 
Problem Statement 
Employee attendance records are stored in attendance.txt. 
Sample Input/Data (attendance.txt) 
EMP101,P 
EMP102,A 
EMP103,P 
EMP104,P 
EMP105,A 
EMP106,P 
EMP107,P 
EMP108,A 
EMP109,P 
EMP110,P 
Tasks 
1. Count present and absent employees.  
2. Display absent employee IDs.  
3. Calculate attendance percentage.  
4. Generate an absentee report in absent_report.txt.  
5. Display employees eligible for attendance awards (100% attendance).  
Sample Output 
Present Employees: 7 
 
Absent Employees: 3 
 
Absent Employee IDs: 
EMP102 
EMP105 
EMP108 
 
Attendance Percentage: 70.0% 
 
Absentee Report Generated Successfully. 
 
Attendance Award Eligibility: 
Not Applicable '''

# Employee Attendance Monitoring System

# --------------------------------------------------
# Task 1: Count Present and Absent Employees
# --------------------------------------------------

# Open file in read mode
file = open("attendance.txt", "r")

present_count = 0
absent_count = 0

# List to store absent employee IDs
absent_employees = []

# Traverse attendance records
for record in file:

    # Remove newline character
    record = record.strip()

    # Split employee ID and status
    emp_id, status = record.split(",")

    # Count present employees
    if status == "P":
        present_count += 1

    # Count absent employees
    else:
        absent_count += 1
        absent_employees.append(emp_id)

# Close file
file.close()

print("Present Employees:", present_count)
print("\nAbsent Employees:", absent_count)

# --------------------------------------------------
# Task 2: Display Absent Employee IDs
# --------------------------------------------------

print("\nAbsent Employee IDs:")

for emp_id in absent_employees:
    print(emp_id)

# --------------------------------------------------
# Task 3: Calculate Attendance Percentage
# --------------------------------------------------

total_employees = present_count + absent_count

attendance_percentage = (present_count / total_employees) * 100

print("\nAttendance Percentage:", attendance_percentage, "%")

# --------------------------------------------------
# Task 4: Generate Absentee Report
# --------------------------------------------------

# Open report file in write mode
report_file = open("absent_report.txt", "w")

# Write absent employee IDs
for emp_id in absent_employees:
    report_file.write(emp_id + "\n")

# Close report file
report_file.close()

print("\nAbsentee Report Generated Successfully.")

# --------------------------------------------------
# Task 5: Display Employees Eligible for Attendance Awards
# --------------------------------------------------

print("\nAttendance Award Eligibility:")

# Since attendance file contains only one day's record,
# no employee can be confirmed for 100% attendance.
print("Not Applicable")
