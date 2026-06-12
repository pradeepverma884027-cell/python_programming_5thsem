# University Course Enrollment Management System

# Dictionary storing course names and number of enrolled students
enrollment = {
    "Python": 45,
    "Java": 38,
    "Data Science": 52,
    "Web Development": 34,
    "Machine Learning": 41,
    "Cloud Computing": 29,
    "Cyber Security": 33,
    "DBMS": 48,
    "Networking": 26,
    "Operating Systems": 37
}

# --------------------------------------------------
# Task 1: Display courses having more than 40 enrollments
# --------------------------------------------------

print("Courses with More Than 40 Enrollments:")

# Traverse the dictionary and check enrollment count
for course, students in enrollment.items():
    if students > 40:
        print(course)

# --------------------------------------------------
# Task 2: Find the most and least popular courses
# --------------------------------------------------

# Assume the first course as both maximum and minimum initially
max_course = list(enrollment.keys())[0]
min_course = list(enrollment.keys())[0]

max_students = enrollment[max_course]
min_students = enrollment[min_course]

# Compare each course enrollment with current maximum and minimum
for course, students in enrollment.items():

    # Update most popular course
    if students > max_students:
        max_students = students
        max_course = course

    # Update least popular course
    if students < min_students:
        min_students = students
        min_course = course

# Display most and least popular courses
print("\nMost Popular Course:")
print(max_course, f"({max_students} students)")

print("\nLeast Popular Course:")
print(min_course, f"({min_students} students)")

# --------------------------------------------------
# Task 3: Calculate total enrollments
# --------------------------------------------------

total_enrollments = 0

# Add enrollment of every course
for students in enrollment.values():
    total_enrollments += students

print("\nTotal Enrollments:", total_enrollments)

# --------------------------------------------------
# Task 4: Categorize courses based on demand
# --------------------------------------------------

# Lists for storing course names according to demand level
high_demand = []
medium_demand = []
low_demand = []

# Classify each course
for course, students in enrollment.items():

    # High Demand: More than 40 students
    if students > 40:
        high_demand.append(course)

    # Medium Demand: 30 to 40 students
    elif students >= 30:
        medium_demand.append(course)

    # Low Demand: Less than 30 students
    else:
        low_demand.append(course)

# Display categorized course lists
print("\nHigh Demand:")
print(high_demand)

print("\nMedium Demand:")
print(medium_demand)

print("\nLow Demand:")
print(low_demand)

# --------------------------------------------------
# Task 5: Count courses requiring promotional activities
# (Courses having less than 35 enrollments)
# --------------------------------------------------

promotion_count = 0

# Count courses with enrollment below 35
for students in enrollment.values():
    if students < 35:
        promotion_count += 1

print("\nCourses Requiring Promotion:", promotion_count)
