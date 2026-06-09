'''Problem Statement 
Store statistics of at least 30 cricket players. 
Example Structure 
players = { 
    "Virat": { 
        "runs": 645, 
        "matches": 12, 
        "wickets": 0 
    } 
} 
Requirements 
1. Display all player statistics.  
2. Find highest run scorer.  
3. Find lowest run scorer.  
4. Calculate average runs.  
5. Find player with maximum wickets.  
6. Find all-rounders (runs > 300 and wickets > 5).  
7. Display players scoring above average.  
8. Create categories:  
o Star Performer  
o Good Performer  
o Average Performer  
o Poor Performer  
9. Generate team statistics.  
10. Display top 5 batsmen.  
11. Display top 5 bowlers.  
12. Create a separate dictionary for award winners. '''



# ==================================================
# CRICKET PLAYER STATISTICS MANAGEMENT SYSTEM
# ==================================================

# Dictionary to store player statistics
players = {}

# --------------------------------------------------
# Enter details of 30 players
# --------------------------------------------------

for i in range(30):

    print(f"\nEnter Details of Player {i}")

    name = input("Enter Player Name: ")
    runs = int(input("Enter Total Runs: "))
    matches = int(input("Enter Matches Played: "))
    wickets = int(input("Enter Total Wickets: "))

    players[name] = {
        "runs": runs,
        "matches": matches,
        "wickets": wickets
    }

# ==================================================
# 1. DISPLAY ALL PLAYER STATISTICS
# ==================================================

print("\n========== PLAYER STATISTICS ==========")

for player, details in players.items():

    print("\nPlayer Name :", player)
    print("Runs        :", details["runs"])
    print("Matches     :", details["matches"])
    print("Wickets     :", details["wickets"])

# ==================================================
# 2. FIND HIGHEST RUN SCORER
# ==================================================

runs_list = []

for details in players.values():
    runs_list.append(details["runs"])

highest_runs = max(runs_list)

for player, details in players.items():

    if details["runs"] == highest_runs:

        print("\nHighest Run Scorer")
        print("Player :", player)
        print("Runs   :", details["runs"])

# ==================================================
# 3. FIND LOWEST RUN SCORER
# ==================================================

lowest_runs = min(runs_list)

for player, details in players.items():

    if details["runs"] == lowest_runs:

        print("\nLowest Run Scorer")
        print("Player :", player)
        print("Runs   :", details["runs"])

# ==================================================
# 4. CALCULATE AVERAGE RUNS
# ==================================================

total_runs = 0

for details in players.values():

    total_runs += details["runs"]

average_runs = total_runs / len(players)

print("\nAverage Runs :", round(average_runs, 2))

# ==================================================
# 5. FIND PLAYER WITH MAXIMUM WICKETS
# ==================================================

wicket_list = []

for details in players.values():

    wicket_list.append(details["wickets"])

max_wickets = max(wicket_list)

for player, details in players.items():

    if details["wickets"] == max_wickets:

        print("\nMaximum Wicket Taker")
        print("Player  :", player)
        print("Wickets :", details["wickets"])

# ==================================================
# 6. FIND ALL-ROUNDERS
# Runs > 300 and Wickets > 5
# ==================================================

print("\n========== ALL-ROUNDERS ==========")

for player, details in players.items():

    if details["runs"] > 300 and details["wickets"] > 5:

        print(player,"Runs:", details["runs"],"Wickets:", details["wickets"])

# ==================================================
# 7. DISPLAY PLAYERS SCORING ABOVE AVERAGE
# ==================================================

print("\n========== PLAYERS ABOVE AVERAGE ==========")

for player, details in players.items():

    if details["runs"] > average_runs:

        print(player,"Runs:", details["runs"])

# ==================================================
# 8. PLAYER CATEGORIES
# ==================================================

print("\n========== PLAYER CATEGORIES ==========")

for player, details in players.items():

    runs = details["runs"]

    if runs >= 600:

        print(player, "- Star Performer")

    elif runs >= 400:

        print(player, "- Good Performer")

    elif runs >= 200:

        print(player, "- Average Performer")

    else:

        print(player, "- Poor Performer")

# ==================================================
# 9. GENERATE TEAM STATISTICS
# ==================================================

total_wickets = 0

for details in players.values():

    total_wickets += details["wickets"]

print("\n========== TEAM STATISTICS ==========")

print("Total Players :", len(players))
print("Total Runs    :", total_runs)
print("Total Wickets :", total_wickets)
print("Average Runs  :", round(average_runs, 2))

# ==================================================
# 10. DISPLAY TOP 5 BATSMEN
# ==================================================

batsmen = []

for player, details in players.items():

    batsmen.append([details["runs"], player])

# Sort list in ascending order
batsmen.sort()

print("\n========== TOP 5 BATSMEN ==========")

for i in range(len(batsmen)-1,len(batsmen)-6,-1):

    print("Player :", batsmen[i][1])
    print("Runs   :", batsmen[i][0])
    print()

# ==================================================
# 11. DISPLAY TOP 5 BOWLERS
# ==================================================

bowlers = []

for player, details in players.items():

    bowlers.append([details["wickets"], player])

# Sort list in ascending order
bowlers.sort()

print("\n========== TOP 5 BOWLERS ==========")

for i in range(len(bowlers)-1,len(bowlers)-6,-1):

    print("Player  :", bowlers[i][1])
    print("Wickets :", bowlers[i][0])
    print()

# ==================================================
# 12. CREATE DICTIONARY OF AWARD WINNERS
# Condition:
# Runs > 500 OR Wickets > 15
# ==================================================

award_winners = {}

for player, details in players.items():

    if details["runs"] > 500 or details["wickets"] > 15:

        award_winners[player] = details

print("\n========== AWARD WINNERS ==========")

for player, details in award_winners.items():

    print(player)
    print("Runs    :", details["runs"])
    print("Matches :", details["matches"])
    print("Wickets :", details["wickets"])
    print()

# ==================================================
# DISPLAY COMPLETE PLAYERS DICTIONARY
# ==================================================

print("\n========== COMPLETE PLAYER RECORD ==========")

for player, details in players.items():

    print(player, details)
