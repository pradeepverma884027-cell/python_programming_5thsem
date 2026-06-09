'''----------------------------------------------------
Problem Statement: Email Address Verification System

Email:
rahul.sharma2026@gmail.com

Tasks
1. Extract username.
2. Extract domain name.
3. Extract extension.
4. Count digits present in username.
5. Count special characters.
6. Check whether:
   • Exactly one '@' exists.
   • At least one '.' exists after '@'.
7. Display Valid Email or Invalid Email.
----------------------------------------------------'''

# storing email address
email = "rahul.sharma2026@gmail.com"

#--------------------------------------------------
# Task-1 : Extract username

username = email[:email.index("@")]

print("Username :", username)

#--------------------------------------------------
# Task-2 : Extract domain name

domain = email[email.index("@") + 1 : email.rindex(".")]

print("Domain :", domain)

#--------------------------------------------------
# Task-3 : Extract extension

extension = email[email.rindex(".") + 1:]

print("Extension :", extension)

#--------------------------------------------------
# Task-4 : Count digits present in username

digit_count = 0

# traverse username
for ch in username:

    if ch.isdigit():
        digit_count += 1

print("\nDigits Found :", digit_count)

#--------------------------------------------------
# Task-5 : Count special characters

special_count = 0

# traverse complete email
for ch in email:

    if not(ch.isalpha() or ch.isdigit()):
        special_count += 1

print("Special Characters Found :", special_count)

#--------------------------------------------------
# Task-6 : Verify email format

is_valid = (
    email.count("@") == 1 and
    "." in email[email.index("@"):]
)

#--------------------------------------------------
# Task-7 : Display email status

if is_valid:
    print("\nEmail Status : Valid")
else:
    print("\nEmail Status : Invalid")

#--------------------------------------------------

'''
Output:

Username : rahul.sharma2026
Domain : gmail
Extension : com

Digits Found : 4
Special Characters Found : 2

Email Status : Valid
'''
