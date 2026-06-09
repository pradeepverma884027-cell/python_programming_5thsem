'''----------------------------------------------------
Problem Statement: Software License Key Verification

License Key:
ABCD-EFGH-IJKL-MNOP

Tasks
1. Verify there are exactly 4 groups.
2. Verify each group contains exactly 4 characters.
3. Count total letters.
4. Count vowels.
5. Remove hyphens and display the merged key.
6. Create a list containing all groups.
7. Display whether the key format is valid.
----------------------------------------------------'''

# storing license key
license_key = "ABCD-EFGH-IJKL-MNOP"

#--------------------------------------------------
# Task-1 and Task-6 :
# Create list of all groups

groups = license_key.split("-")

print("Groups :")
print(groups)

#--------------------------------------------------
# Task-1 : Verify there are exactly 4 groups

group_count = len(groups)

print("\nNumber of Groups :", group_count)

#--------------------------------------------------
# Task-2 : Verify each group contains exactly
# 4 characters

all_groups_valid = True

for group in groups:

    if len(group) != 4:
        all_groups_valid = False
        break

#--------------------------------------------------
# Task-3 : Count total letters

letter_count = 0

for ch in license_key:

    if ch.isalpha():
        letter_count += 1

print("\nTotal Letters :", letter_count)

#--------------------------------------------------
# Task-4 : Count vowels

vowel_count = 0

for ch in license_key:

    if ch.upper() in "AEIOU":
        vowel_count += 1

print("Total Vowels :", vowel_count)

#--------------------------------------------------
# Task-5 : Remove hyphens and display merged key

merged_key = license_key.replace("-", "")

print("\nMerged Key :")
print(merged_key)

#--------------------------------------------------
# Task-7 : Display whether key format is valid

is_valid = (
    len(groups) == 4
    and all_groups_valid
)

if is_valid:
    print("\nLicense Key Status : Valid")

else:
    print("\nLicense Key Status : Invalid")

#--------------------------------------------------

'''
Output:

Groups :
['ABCD', 'EFGH', 'IJKL', 'MNOP']

Number of Groups : 4

Total Letters : 16
Total Vowels : 4

Merged Key :
ABCDEFGHIJKLMNOP

License Key Status : Valid
'''
