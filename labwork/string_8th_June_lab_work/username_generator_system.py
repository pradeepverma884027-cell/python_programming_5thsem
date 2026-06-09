# ----------------------------------------------------
# Problem: Username Generator
# Rules:
# 1. Remove spaces
# 2. Convert to lowercase
# 3. Append current year (2026)
# 4. If length exceeds 12, keep first 12 characters
# 5. Count vowels
# 6. Count consonants
# 7. Display username statistics
# ----------------------------------------------------

# Take user's full name as input
name = input("Enter the name: ")

# Store original name for display
original_name = name

# Task 1: Remove spaces from the name
username = name.replace(" ", "")

# Task 2: Convert username to lowercase
username = username.lower()

# Task 3: Append current year
username = username + "2026"

# Store complete username before truncation
full_username = username

# Task 4: If username length exceeds 12, keep only first 12 characters
if len(username) > 12:
    username = username[:12]

# Task 5 & 6: Count vowels and consonants
vowel_count = 0
consonant_count = 0

for ch in username:

    # Check if character is a letter
    if ch.isalpha():

        # Count vowels
        if ch in "aeiou":
            vowel_count += 1

        # Count consonants
        else:
            consonant_count += 1

# Display Results
print("\nOriginal Name:", original_name)

print("\nGenerated Username:", full_username)

print("\nFinal Username (Max 12 Characters):", username)

print("\nUsername Length:", len(username))

print("\nVowels:", vowel_count)
print("Consonants:", consonant_count)

print("\nStatus: Username Generated Successfully")
