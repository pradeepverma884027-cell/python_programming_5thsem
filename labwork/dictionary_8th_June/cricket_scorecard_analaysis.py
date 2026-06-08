'''----------------------------------------------------
Problem Statement: Cricket Tournament Statistics

Scenario
Runs scored by players in a tournament:

runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

Tasks
1. Display players scoring more than 500 runs.
2. Find the Orange Cap winner.
3. Find the lowest scorer.
4. Calculate total runs scored.
5. Create a list of players scoring below 400.
6. Count players scoring between 400 and 600 runs.
----------------------------------------------------'''

# creating a dictionary to store players and their runs
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

#--------------------------------------------------
# to display players scoring more than 500 runs

print("\nPlayers Scoring More Than 500 Runs :")

for player, score in runs.items():
    if score > 500:
        print(player)

#--------------------------------------------------
# to find the Orange Cap winner

dict_items = list(runs.items())

orange_cap_winner = dict_items[0][0]
highest_runs = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_runs:
        orange_cap_winner = item[0]
        highest_runs = item[1]

print("\nOrange Cap Winner :", orange_cap_winner, "(", highest_runs, ")")

#--------------------------------------------------
# to find the lowest scorer

lowest_scorer = dict_items[0][0]
lowest_runs = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_runs:
        lowest_scorer = item[0]
        lowest_runs = item[1]

print("\nLowest Scorer :", lowest_scorer, "(", lowest_runs, ")")

#--------------------------------------------------
# to calculate total runs scored

total_runs = 0

for score in runs.values():
    total_runs += score

print("\nTotal Tournament Runs :", total_runs)

#--------------------------------------------------
# to create a list of players scoring below 400

below_400 = []# list for storing players who scored below 400

for player, score in runs.items():
    if score < 400:
        below_400.append(player)

print("\nPlayers Scoring Below 400 :")
print(below_400)

#--------------------------------------------------
# to count players scoring between 400 and 600 runs

count = 0 # counter to count players scoring between 400 and 600 runs

for score in runs.values():
    if (score >= 400) and (score <= 600):
        count += 1

print("\nPlayers Between 400 and 600 Runs :", count)

#--------------------------------------------------

'''
Output:

Players Scoring More Than 500 Runs :
Virat
Rohit
Gill
Pant

Orange Cap Winner : Gill ( 698 )

Lowest Scorer : Hardik ( 278 )

Total Tournament Runs : 4657

Players Scoring Below 400 :
['Hardik', 'Surya', 'Jadeja']

Players Between 400 and 600 Runs : 5
'''
