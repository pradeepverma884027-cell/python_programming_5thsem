# Input number of racers
n = int(input("Enter number of racers: "))

# Input first racer's lap time
time = float(input("Enter lap time of racer 1: "))

# Assume first racer is both fastest and slowest initially
fastest_time = time
slowest_time = time
fastest_position = 1
slowest_position = 1

# Input remaining racers
for i in range(2, n + 1):
    time = float(input(f"Enter lap time of racer {i}: "))

    # Check for fastest racer
    if time < fastest_time:
        fastest_time = time
        fastest_position = i

    # Check for slowest racer
    if time > slowest_time:
        slowest_time = time
        slowest_position = i

# Calculate difference
difference = slowest_time - fastest_time

# Display results
print("Fastest racer position:", fastest_position)
print("Slowest racer position:", slowest_position)
print("Difference:", difference)
