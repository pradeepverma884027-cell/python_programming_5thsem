# University Course Enrollment Management System

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

# 1. Display courses having more than 40 enrollments
print("Courses with More Than 40 Enrollments:")
for course, students in enrollment.items():
    if students > 40:
        print(course)

# 2. Find the most and least popular courses
most_popular = max(enrollment, key=enrollment.get)
least_popular = min(enrollment, key=enrollment.get)

print("\nMost Popular Course:")
print(f"{most_popular} ({enrollment[most_popular]} students)")

print("\nLeast Popular Course:")
print(f"{least_popular} ({enrollment[least_popular]} students)")

# 3. Calculate total enrollments
total_enrollments = sum(enrollment.values())

print("\nTotal Enrollments:", total_enrollments)

# 4. Create demand categories
high_demand = []
medium_demand = []
low_demand = []

for course, students in enrollment.items():

    if students > 40:
        high_demand.append(course)

    elif students >= 30:
        medium_demand.append(course)

    else:
        low_demand.append(course)

print("\nHigh Demand:")
print(high_demand)

print("\nMedium Demand:")
print(medium_demand)

print("\nLow Demand:")
print(low_demand)

# 5. Count courses requiring promotional activities
promotion_count = 0

for students in enrollment.values():
    if students < 35:
        promotion_count += 1

print("\nCourses Requiring Promotion:", promotion_count)
