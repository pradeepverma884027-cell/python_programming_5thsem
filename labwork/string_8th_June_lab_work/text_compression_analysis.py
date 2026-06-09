'''----------------------------------------------------
Problem Statement: Compressed Message Analysis System

Original Text:
AAABBBCCCDDDAAA

Tasks
1. Count occurrences of each character.
2. Create a dictionary of character frequencies.
3. Display unique characters.
4. Find the most frequent character.
5. Create a compressed output.
6. Calculate compression ratio.
----------------------------------------------------'''

# storing original text
text = "AAABBBCCCDDDAAA"

#--------------------------------------------------
# Task-1 and Task-2 :
# Create dictionary of character frequencies

frequency = {}

# traverse text
for ch in text:

    if ch in frequency:
        frequency[ch] += 1

    else:
        frequency[ch] = 1

print("Character Frequencies :")

for character, count in frequency.items():
    print(character, "->", count)

#--------------------------------------------------
# Task-3 : Display unique characters

unique_characters = list(frequency.keys())

print("\nUnique Characters :")
print(unique_characters)

#--------------------------------------------------
# Task-4 : Find most frequent character

dict_items = list(frequency.items())

most_frequent_character = dict_items[0][0]
highest_frequency = dict_items[0][1]

for item in dict_items:

    if item[1] > highest_frequency:
        most_frequent_character = item[0]
        highest_frequency = item[1]

print("\nMost Frequent Character :",
      most_frequent_character)

#--------------------------------------------------
# Task-5 : Create compressed output

compressed_text = ""

count = 1

for i in range(len(text) - 1):

    if text[i] == text[i + 1]:
        count += 1

    else:
        compressed_text += text[i] + str(count)
        count = 1

# add last character group
compressed_text += text[-1] + str(count)

print("\nCompressed Output :")
print(compressed_text)

#--------------------------------------------------
# Task-6 : Calculate compression ratio

original_length = len(text)

compressed_length = len(compressed_text)

compression_ratio = (
    compressed_length / original_length
) * 100

print("\nOriginal Length :", original_length)

print("Compressed Length :", compressed_length)

print("\nCompression Ratio :",
      round(compression_ratio, 2), "%")

#--------------------------------------------------

'''
Output:

Character Frequencies :
A -> 6
B -> 3
C -> 3
D -> 3

Unique Characters :
['A', 'B', 'C', 'D']

Most Frequent Character : A

Compressed Output :
A3B3C3D3A3

Original Length : 15
Compressed Length : 10

Compression Ratio : 66.67 %
'''
