 '''Word Frequency Analyzer 
Problem Statement 
A text file contains the following paragraph. 
Sample Input/Data (article.txt) 
Python is easy to learn. 
Python is powerful. 
Python supports multiple programming paradigms. 
Programming with Python is enjoyable. 
Tasks 
1. Count the total number of words.  
2. Count the frequency of each word.  
3. Find the most frequently occurring word.  
4. Display words appearing only once.  
5. Display all unique words.  
Sample Output 
Total Words: 16 
 
Most Frequent Word: 
Python (4 times) 
 
Words Appearing Once: 
easy 
to 
learn 
powerful 
supports 
multiple 
paradigms 
with 
enjoyable 
 
Unique Words Count: 12'''

# Word Frequency Analyzer

# Open the file in read mode
file = open("article.txt", "r")

# Read complete content from the file
content = file.read()

# Close the file
file.close()

# Convert text to lowercase for accurate counting
content = content.lower()

# Remove punctuation marks
content = content.replace(".", "")
content = content.replace(",", "")
content = content.replace("!", "")
content = content.replace("?", "")

# Split content into words
words = content.split()

# --------------------------------------------------
# Task 1: Count the total number of words
# --------------------------------------------------

total_words = len(words)

print("Total Words:", total_words)

# --------------------------------------------------
# Task 2: Count the frequency of each word
# --------------------------------------------------

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")

for word, count in frequency.items():
    print(word, ":", count)

# --------------------------------------------------
# Task 3: Find the most frequently occurring word
# --------------------------------------------------

most_frequent_word = ""
highest_count = 0

for word, count in frequency.items():

    if count > highest_count:
        highest_count = count
        most_frequent_word = word

print("\nMost Frequent Word:")
print(most_frequent_word, f"({highest_count} times)")

# --------------------------------------------------
# Task 4: Display words appearing only once
# --------------------------------------------------

print("\nWords Appearing Once:")

for word, count in frequency.items():

    if count == 1:
        print(word)

# --------------------------------------------------
# Task 5: Display all unique words
# --------------------------------------------------

unique_words = []

for word, count in frequency.items():
    unique_words.append(word)

print("\nUnique Words Count:", len(unique_words))
print("Unique Words:")
print(unique_words)
