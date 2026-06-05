# List containing marks of students
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# Empty list to store passed students
pass_students = []

# Empty list to store marks above 75
above_75 = []

# Variable to count failed students
failed = 0

# Traverse through the marks list
for i in marks:

    # Check for passed students
    if i >= 40:
        pass_students.append(i)

    # Count failed students
    if i < 40:
        failed += 1

    # Store marks greater than 75
    if i > 75:
        above_75.append(i)

# Assume first element is both maximum and minimum
max = marks[0]
min = marks[0]

# Find highest and lowest marks without using max() or min()
for i in range(len(marks)):

    # Update maximum mark
    if marks[i] > max:
        max = marks[i]

    # Update minimum mark
    if marks[i] < min:
        min = marks[i]

# Display results
print("Passed Students:", pass_students)
print("Highest Marks:", max)
print("Lowest Marks:", min)
print("Marks Above 75:", above_75)
print("Failed Students Count:", failed)
