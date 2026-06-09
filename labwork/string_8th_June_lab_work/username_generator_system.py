'''----------------------------------------------------
Problem Statement: Username Generator System

Student Name:
Rahul Sharma

Tasks
1. Remove spaces.
2. Convert to lowercase.
3. Append current year (2026).
4. If username length exceeds 12, keep only first 12 characters.
5. Count vowels in the generated username.
6. Count consonants.
7. Display username statistics.
----------------------------------------------------'''

# storing student name
name = "Rahul Sharma"

#--------------------------------------------------
# Task-1 : Remove spaces

username = name.replace(" ", "")

#--------------------------------------------------
# Task-2 : Convert to lowercase

username = username.lower()

#--------------------------------------------------
# Task-3 : Append current year

username = username + "2026"

# display generated username
print("Generated Username :", username)

#--------------------------------------------------
# Task-4 : If username length exceeds 12,
# keep only first 12 characters

if len(username) > 12:
    short_username = username[:12]
else:
    short_username = username

print("Username After Applying Length Rule :", short_username)

#--------------------------------------------------
# Task-5 and Task-6 :
# Count vowels and consonants

vowel_count = 0
consonant_count = 0

# traverse generated username
for ch in username:

    # count only alphabets
    if ch.isalpha():

        if ch in "aeiou":
            vowel_count += 1

        else:
            consonant_count += 1

#--------------------------------------------------
# Task-7 : Display username statistics

print("\nOriginal Name :", name)

print("Generated Username :", username)

print("Username Length :", len(username))

print("\nVowels :", vowel_count)
print("Consonants :", consonant_count)

print("\nStatus : Username Generated Successfully")

#--------------------------------------------------

'''
Output:

Original Name : Rahul Sharma

Generated Username : rahulsharma2026

Username Length : 15

Vowels : 4
Consonants : 7

Status : Username Generated Successfully
'''
