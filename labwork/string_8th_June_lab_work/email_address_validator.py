''' Problem Statement: Email Address Verification System 
Email: rahul.sharma2026@gmail.com 
Tasks 1. Extract username. 
2. Extract domain name. 
3. Extract extension. 
4. Count digits present in username. 
5. Count special characters. 
6. Check whether: • Exactly one '@' exists. • At least one '.' exists after '@'. 
7. Display Valid Email or Invalid Email. 
----------------------------------------------------'''
# storing email address
email = "rahul.sharma2026@gmail.com"

#--------------------------------------------------
# Task-1 : Extract username

parts = email.split("@")

username = parts[0]

#--------------------------------------------------
# Task-2 and Task-3 :
# Extract domain and extension

domain_parts = parts[1].split(".")

domain = domain_parts[0]
extension = domain_parts[1]

print("Username :", username)
print("Domain :", domain)
print("Extension :", extension)

#--------------------------------------------------
# Task-4 and Task-5 :
# Count digits and special characters in username

digit_count = 0
special_count = 0

for ch in username:

    # count digits
    if ch.isdigit():
        digit_count += 1

    # count special characters
    if not ch.isalnum():
        special_count += 1

print("Digits Found :", digit_count)
print("Special Characters Found :", special_count)

#--------------------------------------------------
# Task-6 : Validate email


validity = (
    email.count("@") == 1
    and "." in email[email.index("@"):]
)
#--------------------------------------------------
# Task-7 : Display email status

if validity:
    print("Email Status : Valid")

else:
    print("Email Status : Invalid")


'''Sample Output 
Email: rahul.sharma2026@gmail.com 
 
Username: rahul.sharma2026 
Domain: gmail 
Extension: com 
 
Digits Found: 4 
Special Characters Found: 2 
 
Email Status: Valid '''
