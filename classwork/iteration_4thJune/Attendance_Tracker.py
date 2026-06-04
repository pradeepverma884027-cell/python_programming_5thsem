student_in_class = 0
present_count = 0
absent_count = 0

for i in range(1,31):
    p = str(input("Enter P for Present, A for Absent: "))

    if p == "P":
        print("Student ",i)
        print("Attendance : Present")
        present_count += 1
    else:
        print("Student", i)
        print("Attendance : Absent")
        absent_count += 1

    student_in_class += 1

print("No. of Students Present:", present_count)
print("No. of Students Absent:", absent_count)
