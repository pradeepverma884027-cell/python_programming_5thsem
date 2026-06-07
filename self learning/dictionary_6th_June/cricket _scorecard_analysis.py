'''Sample Data 
scores = { 
    "Virat": 78, 
    "Rohit": 112, 
    "Gill": 45, 
    "Rahul": 89, 
    "Hardik": 32, 
    "Jadeja": 61, 
    "Surya": 105, 
    "Pant": 95, 
    "Bumrah": 18, 
    "Shami": 25 
} 
Tasks 
• Display players who scored 50 or more runs.  
• Count the number of centuries.  
• Find the player with the highest score.  
• Create a list of players scoring below 30 runs.  
• Determine how many players scored between 50 and 99.'''

'''
Cricket Score Analysis
'''

# Dictionary containing player names and their scores
scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# --------------------------------------------------
# Task 1: Display players who scored 50 or more runs
# --------------------------------------------------

print("Players scoring 50 or more runs:")

# Traverse dictionary
for player, score in scores.items():

    # Check if score is 50 or more
    if score >= 50:
        print(player)

print("-----------------------------------")

# --------------------------------------------------
# Task 2: Count the number of centuries
# --------------------------------------------------

centuries = 0

# Traverse score values
for score in scores.values():

    # Check if score is 100 or more
    if score >= 100:
        centuries += 1

print("Number of Centuries:", centuries)

print("-----------------------------------")

# --------------------------------------------------
# Task 3: Find the player with the highest score
# --------------------------------------------------

# Assume first player has highest score
highest_player = list(scores.keys())[0]

# Store first player's score
highest_score = scores[highest_player]

# Traverse dictionary
for player, score in scores.items():

    # Update highest score and player
    if score > highest_score:
        highest_score = score
        highest_player = player

print("Highest Scorer:", highest_player)
print("Score:", highest_score)

print("-----------------------------------")

# --------------------------------------------------
# Task 4: Create a list of players
# scoring below 30 runs
# --------------------------------------------------

below_30 = []

# Traverse dictionary
for player, score in scores.items():

    # Check if score is below 30
    if score < 30:
        below_30.append(player)

print("Players scoring below 30 runs:")
print(below_30)

print("-----------------------------------")

# --------------------------------------------------
# Task 5: Determine how many players
# scored between 50 and 99
# --------------------------------------------------

count = 0 # counter for counting players scored between 50 and 99


# Traverse score values
for score in scores.values():

    # Check score range
    if 50 <= score <= 99:
        count += 1

print("Players scoring between 50 and 99:", count)
