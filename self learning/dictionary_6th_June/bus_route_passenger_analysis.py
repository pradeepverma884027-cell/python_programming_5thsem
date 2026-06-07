'''Sample Data 
passengers = { 
    "Stop1": 12, 
    "Stop2": 25, 
    "Stop3": 18, 
    "Stop4": 32, 
    "Stop5": 9, 
    "Stop6": 28, 
    "Stop7": 14, 
    "Stop8": 7, 
    "Stop9": 21, 
    "Stop10": 16 
} 
Tasks 
• Display stops having more than 20 passengers.  
• Count stops with fewer than 10 passengers.  
• Find the busiest stop.  
• Create a list of stops requiring an extra bus (passengers > 25).  
• Calculate the average number of passengers.'''

'''
Bus Passenger Analysis
'''

# Dictionary containing bus stops and passenger count
passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# --------------------------------------------------
# Task 1: Display stops having more than 20 passengers
# --------------------------------------------------

print("Stops having more than 20 passengers:")

# Traverse dictionary
for stop, count in passengers.items():

    # Check passenger count
    if count > 20:
        print(stop)

print("-----------------------------------")

# --------------------------------------------------
# Task 2: Count stops with fewer than 10 passengers
# --------------------------------------------------

stops = 0 # counter to count  stops with passenger less than 10

# Traverse passenger counts
for count in passengers.values():

    # Check if passenger count is below 10
    if count < 10:
        stops+= 1

print("Stops with fewer than 10 passengers:")
print(stops)

print("-----------------------------------")

# --------------------------------------------------
# Task 3: Find the busiest stop
# --------------------------------------------------

# Assume first stop is busiest initially
busiest_stop = list(passengers.keys())[0]

# Store passenger count of first stop
max_passengers = passengers[busiest_stop]

# Traverse dictionary
for stop, count in passengers.items():

    # Update busiest stop if larger count found
    if count > max_passengers:
        max_passengers = count
        busiest_stop = stop

print("Busiest Stop:", busiest_stop)
print("Passengers:", max_passengers)

print("-----------------------------------")

# --------------------------------------------------
# Task 4: Create a list of stops requiring
# an extra bus (passengers > 25)
# --------------------------------------------------

extra_bus_stops = []

# Traverse dictionary
for stop, count in passengers.items():

    # Check if passenger count exceeds 25
    if count > 25:
        extra_bus_stops.append(stop)

print("Stops Requiring Extra Bus:")
print(extra_bus_stops)

print("-----------------------------------")

# --------------------------------------------------
# Task 5: Calculate average number of passengers
# --------------------------------------------------

total_passengers = 0

# Calculate total passengers
for count in passengers.values():
    total_passengers += count

# Calculate average
average_passengers = total_passengers / len(passengers)

print("Average Number of Passengers:")
print(average_passengers)
