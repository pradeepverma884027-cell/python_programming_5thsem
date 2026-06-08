'''----------------------------------------------------
Employee ID Validation and Analysis System

Problem Statement
A company generates employee IDs in the following format:

EMP2026ANUJ458

Tasks
1. Count the number of uppercase letters.
2. Count the number of digits.
3. Extract the joining year.
4. Extract the employee name.
5. Check whether the ID follows these rules:
   • Starts with "EMP"
   • Contains exactly 4 digits for the year
   • Ends with exactly 3 digits
6. Create a list containing all digits present in the ID.
7. Find the sum of all digits present in the ID.
8. Display whether the ID is valid or invalid.
----------------------------------------------------'''

# creating employee id
employee_id = "EMP2026ANUJ458"

#--------------------------------------------------
# Task-1 : Count the number of uppercase letters

# initialize counter
uppercase_count = 0

# traverse each character of employee id
for ch in employee_id:

    # check whether character is uppercase
    if ch.isupper():
        uppercase_count += 1

print("Uppercase Letters :", uppercase_count)

#--------------------------------------------------
# Task-2 : Count the number of digits

# initialize counter
digit_count = 0

# traverse each character of employee id
for ch in employee_id:

    # check whether character is a digit
    if ch.isdigit():
        digit_count += 1

print("Digits :", digit_count)

#--------------------------------------------------
# Task-3 : Extract the joining year

# year starts after EMP and occupies 4 positions
joining_year = employee_id[3:7]

print("Joining Year :", joining_year)

#--------------------------------------------------
# Task-4 : Extract the employee name

# name lies between year and last 3 digits
employee_name = employee_id[7:-3]

print("Employee Name :", employee_name)

#--------------------------------------------------
# Task-5 : Validate the employee id

# check all required conditions
is_valid = (
    employee_id.startswith("EMP")      # starts with EMP
    and employee_id[3:7].isdigit()     # year contains digits only
    and len(employee_id[3:7]) == 4     # year has exactly 4 digits
    and employee_id[-3:].isdigit()     # last 3 characters are digits
)

# display validation result
if is_valid:
    print("Validation Result : Valid")
else:
    print("Validation Result : Invalid")

#--------------------------------------------------
# Task-6 : Create a list containing all digits

# create empty list
digits = []

# traverse employee id
for ch in employee_id:

    # store digit in list
    if ch.isdigit():
        digits.append(int(ch))

print("Digit List :", digits)

#--------------------------------------------------
# Task-7 : Find the sum of all digits

# initialize sum variable
sum_digits = 0

# traverse digit list
for digit in digits:
    sum_digits += digit

print("Sum of Digits :", sum_digits)

#--------------------------------------------------
# Task-8 : Display whether the ID is valid or invalid

if is_valid:
    print("ID Status : Valid")
else:
    print("ID Status : Invalid")

#--------------------------------------------------

'''
Output:

Uppercase Letters : 7
Digits : 7

Joining Year : 2026
Employee Name : ANUJ

Validation Result : Valid

Digit List : [2, 0, 2, 6, 4, 5, 8]

Sum of Digits : 27

ID Status : Valid
'''
