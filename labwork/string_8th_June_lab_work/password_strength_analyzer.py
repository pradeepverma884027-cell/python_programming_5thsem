
'''----------------------------------------------------
Problem Statement:
A user enters a password.

Password:
Python@2026!

Tasks
1. Determine whether the password is Strong, Medium, or Weak.
2. Count uppercase letters.
3. Count lowercase letters.
4. Count digits.
5. Count special characters.
6. Display all digits separately.
7. Display all special characters separately.

Rules:
• Minimum length 8
• At least 1 uppercase letter
• At least 1 lowercase letter
• At least 1 digit
• At least 1 special character
----------------------------------------------------'''

# storing password
password = "Python@2026!"
if password.isspace():
    exit("password cannot be blank")
#--------------------------------------------------
# initialize counters and lists

uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_count = 0

#--------------------------------------------------
# traverse password and count different types
# of characters

for ch in password:

    # count uppercase letters
    if ch.isupper():
        uppercase_count += 1

    # count lowercase letters
    elif ch.islower():
        lowercase_count += 1

    # count digits and store them in list
    elif ch.isdigit():
        digit_count += 1
        

    # count special characters and store them
    else:
        special_count += 1
#--------------------------------------------------
# Task-1 : Determine password strength

if (
    len(password) >= 8
    and uppercase_count >= 1
    and lowercase_count >= 1
    and digit_count >= 1
    and special_count >= 1
):
    strength = "Strong"

elif (
    len(password) >= 8
    and (
        uppercase_count >= 1
        or lowercase_count >= 1
        or digit_count >= 1
        or special_count >= 1
    )
):
    strength = "Medium"

else:
    strength = "Weak"

#--------------------------------------------------
# Task-2 : Display uppercase letter count

print("Uppercase Letters :", uppercase_count)

#--------------------------------------------------
# Task-3 : Display lowercase letter count

print("Lowercase Letters :", lowercase_count)

#--------------------------------------------------
# Task-4 : Display digit count

print("Digits :", digit_count)

#--------------------------------------------------
# Task-5 : Display special character count

print("Special Characters :", special_count)

#--------------------------------------------------
# Task-6 : Display all digits separately
# first check digit or special character then allocate memory
digits_found = []
special_characters_found = []
for ch in password:
    if ch.isdigit():
        digits_found.append(ch)
    if ch.isalpha():
        continue
    if ch.isalnum():
        continue
    else:
        special_characters_found.append(ch)
print("\nDigits Found :", digits_found)

#--------------------------------------------------
# Task-7 : Display all special characters separately

print("Special Characters Found :", special_characters_found)

#--------------------------------------------------
# Display password strength

print("\nPassword Strength :", strength)

#--------------------------------------------------

'''
Output:

Uppercase Letters : 1
Lowercase Letters : 5
Digits : 4
Special Characters : 2

Digits Found : ['2', '0', '2', '6']
Special Characters Found : ['@', '!']

Password Strength : Strong
'''
