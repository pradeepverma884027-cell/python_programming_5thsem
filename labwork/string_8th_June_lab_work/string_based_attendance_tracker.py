'''----------------------------------------------------
Problem Statement: Student Attendance Analysis System

Attendance Record:
PPAPPPAAPPPPAPP

Where:
P = Present
A = Absent

Tasks
1. Count Present and Absent days.
2. Calculate attendance percentage.
3. Find the longest consecutive streak of Presence.
4. Find the longest consecutive streak of Absence.
5. Determine whether attendance is below 75%.
----------------------------------------------------'''

# storing attendance record
attendance = "PPAPPPAAPPPPAPP"

#--------------------------------------------------
# Task-1 : Count Present and Absent days

present_count = 0
absent_count = 0

# traverse attendance record
for ch in attendance:

    if ch == "P":
        present_count += 1

    elif ch == "A":
        absent_count += 1

print("Present Days :", present_count)
print("Absent Days :", absent_count)

#--------------------------------------------------
# Task-2 : Calculate attendance percentage

total_days = len(attendance)

attendance_percentage = (present_count / total_days) * 100

print("\nAttendance Percentage :",
      round(attendance_percentage, 2), "%")

#--------------------------------------------------
# Task-3 : Find longest consecutive streak
# of Presence

current_present_streak = 0
longest_present_streak = 0

for ch in attendance:

    if ch == "P":

        current_present_streak += 1

        if current_present_streak > longest_present_streak:
            longest_present_streak = current_present_streak

    else:
        current_present_streak = 0

print("\nLongest Present Streak :",
      longest_present_streak)

#--------------------------------------------------
# Task-4 : Find longest consecutive streak
# of Absence

current_absent_streak = 0
longest_absent_streak = 0

for ch in attendance:

    if ch == "A":

        current_absent_streak += 1

        if current_absent_streak > longest_absent_streak:
            longest_absent_streak = current_absent_streak

    else:
        current_absent_streak = 0

print("Longest Absent Streak :",
      longest_absent_streak)

#--------------------------------------------------
# Task-5 : Check attendance status

if attendance_percentage < 75:
    print("\nAttendance Status : Below 75%")

else:
    print("\nAttendance Status : Above 75%")

#--------------------------------------------------

'''
Output:

Present Days : 11
Absent Days : 4

Attendance Percentage : 73.33 %

Longest Present Streak : 4
Longest Absent Streak : 2

Attendance Status : Below 75%
'''
