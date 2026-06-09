'''Problem Statement 
A customer submits a review: 
This product is excellent excellent excellent and very useful 
Tasks 
Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
4. Find all words appearing only once.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words.  
 
Sample Output 
Total Words: 8 
 
Word Frequencies: 
This -> 1 
product -> 1 
is -> 1 
excellent -> 3 
and -> 1 
very -> 1 
useful -> 1 
 
Most Frequent Word: excellent 
 
Words Appearing Once: 
['This', 'product', 'is', 'and', 'very', 'useful'] 
 
Unique Words: 
['This', 'product', 'is', 'excellent', 'and', 'very', 'useful'] '''

# storing customer review
review = "This product is excellent excellent excellent and very useful"

#--------------------------------------------------
# convert review into list of words

words = review.split()

#--------------------------------------------------
# Task-1 : Count total words

total_words = len(words)

print("Total Words :", total_words)

#--------------------------------------------------
# Task-2 : Create dictionary containing word frequencies

word_frequency = {}

# traverse each word
for word in words:

    # if word already exists, increase count
    if word in word_frequency:
        word_frequency[word] += 1

    # otherwise add word with frequency 1
    else:
        word_frequency[word] = 1

print("\nWord Frequencies :")

for word, frequency in word_frequency.items():
    print(word, "->", frequency)

#--------------------------------------------------
# Task-3 : Find the most frequently used word

dict_items = list(word_frequency.items())

most_frequent_word = dict_items[0][0]
highest_frequency = dict_items[0][1]

for item in dict_items:

    if item[1] > highest_frequency:
        most_frequent_word = item[0]
        highest_frequency = item[1]

print("\nMost Frequent Word :", most_frequent_word)

#--------------------------------------------------
# Task-4 : Find all words appearing only once

single_occurrence_words = []

for word, frequency in word_frequency.items():

    if frequency == 1:
        single_occurrence_words.append(word)

print("\nWords Appearing Once :")
print(single_occurrence_words)

#--------------------------------------------------
# Task-5 : Count words having more than 5 characters

count = 0

for word in words:

    if len(word) > 5:
        count += 1

print("\nWords Having More Than 5 Characters :", count)

#--------------------------------------------------
# Task-6 : Display words in reverse order

print("\nWords In Reverse Order :")

for word in words[::-1]:
    print(word)

#--------------------------------------------------
# Task-7 : Create a list of unique words

unique_words = []

for word in words:

    if word not in unique_words:
        unique_words.append(word)

print("\nUnique Words :")
print(unique_words)

#--------------------------------------------------

'''
Output:

Total Words : 8

Word Frequencies :
This -> 1
product -> 1
is -> 1
excellent -> 3
and -> 1
very -> 1
useful -> 1

Most Frequent Word : excellent

Words Appearing Once :
['This', 'product', 'is', 'and', 'very', 'useful']

Words Having More Than 5 Characters : 5

Words In Reverse Order :
useful
very
and
excellent
excellent
excellent
is
product
This

Unique Words :
['This', 'product', 'is', 'excellent', 'and', 'very', 'useful']
'''
