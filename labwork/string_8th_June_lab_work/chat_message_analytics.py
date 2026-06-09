'''Problem Statement 
A chat application stores a message: 
Python is awesome and Python is easy to learn 
Tasks 
Write a program to: 
1. Count total characters.  
2. Count total words.  
3. Find the longest word.  
4. Find the shortest word.  
5. Count how many times the word "Python" appears.  
6. Create a list of words having more than 4 characters.  
7. Display all words starting with a vowel.  
8. Count the number of vowels and consonants.  
'''
# storing the message
message = "Python is awesome and Python is easy to learn"

#--------------------------------------------------
# convert message into list of words

words = message.split()

#--------------------------------------------------
# Task-1 : Count total characters

character_count = len(message)

print("Total Characters :", character_count)

#--------------------------------------------------
# Task-2 : Count total words

word_count = len(words)

print("Total Words :", word_count)

#--------------------------------------------------
# Task-3 : Find the longest word

longest_word = words[0]

for word in words:

    if len(word) > len(longest_word):
        longest_word = word

print("Longest Word :", longest_word)

#--------------------------------------------------
# Task-4 : Find the shortest word

shortest_word = words[0]

for word in words:

    if len(word) < len(shortest_word):
        shortest_word = word

print("Shortest Word :", shortest_word)

#--------------------------------------------------
# Task-5 : Count occurrences of Python

python_count = 0

for word in words:

    if word == "Python":
        python_count += 1

print("Occurrences of Python :", python_count)

#--------------------------------------------------
# Task-6 : Create a list of words having more than
# 4 characters

long_words = []

for word in words:

    if len(word) > 4:
        long_words.append(word)

print("\nWords Longer Than 4 Characters :")
print(long_words)

#--------------------------------------------------
# Task-7 : Display all words starting with a vowel

vowel_words = []

for word in words:

    if word[0].lower() in "aeiou":
        vowel_words.append(word)

print("\nWords Starting With Vowel :")
print(vowel_words)

#--------------------------------------------------
# Task-8 : Count vowels and consonants

vowel_count = 0
consonant_count = 0

for ch in message.lower():

    if ch.isalpha():

        if ch in "aeiou":
            vowel_count += 1

        else:
            consonant_count += 1

print("\nVowels :", vowel_count)
print("Consonants :", consonant_count)

#--------------------------------------------------

'''
Output:

Total Characters : 45
Total Words : 8

Longest Word : awesome
Shortest Word : is

Occurrences of Python : 2

Words Longer Than 4 Characters :
['Python', 'awesome', 'Python', 'learn']

Words Starting With Vowel :
['is', 'awesome', 'and', 'is', 'easy']

Vowels : 16
Consonants : 22
'''
