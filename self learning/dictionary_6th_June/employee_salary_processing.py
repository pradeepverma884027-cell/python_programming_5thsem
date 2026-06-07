'''
Employee Salary Analysis
'''

# Creating dictionary of employee IDs and their salaries
# Key   -> Employee ID
# Value -> Salary
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# --------------------------------------------------
# Task 1: Display employees earning above ₹60,000
# --------------------------------------------------

print("Employees having salary above ₹60,000:")

# Traverse dictionary
for employee, sal in salary.items():

    # Check if salary is greater than 60000
    if sal > 60000:
        print(employee)

print("------------------------------------")

# --------------------------------------------------
# Task 2: Count employees earning below ₹40,000
# --------------------------------------------------

# Counter variable
count = 0

print("No. of Employees having salary below ₹40,000:")

# Traverse salary values only
for sal in salary.values():

    # Check if salary is less than 40000
    if sal < 40000:
        count += 1

# Display count
print(count)

print("---------------------------------------")

# --------------------------------------------------
# Task 3: Find the highest-paid employee
# --------------------------------------------------

# Assume first employee has highest salary initially
highest_employee = list(salary.keys())[0]

# Store salary of first employee
highest_salary = salary[highest_employee]

# Traverse dictionary
for emp_id, sal in salary.items():

    # Update highest salary and employee ID
    # if a larger salary is found
    if sal > highest_salary:
        highest_salary = sal
        highest_employee = emp_id

# Display highest-paid employee
print("Highest Paid Employee:", highest_employee)
print("Salary:", highest_salary)

print("-----------------------------------")

# --------------------------------------------------
# Task 4: Create list of employees eligible
# for bonus (salary > ₹50,000)
# --------------------------------------------------

# Empty list to store bonus-eligible employees
bonus_employees = []

# Traverse dictionary
for emp_id, sal in salary.items():

    # Check bonus eligibility
    if sal > 50000:
        bonus_employees.append(emp_id)

# Display list
print("Employees Eligible for Bonus:")
print(bonus_employees)

print("-----------------------------------")

# --------------------------------------------------
# Task 5: Calculate average salary
# --------------------------------------------------

# Variable to store total salary
total_salary = 0

# Add all salaries
for sal in salary.values():
    total_salary += sal

# Calculate average salary
average_salary = total_salary / len(salary)

# Display average salary
print("Average Salary:", average_salary)
