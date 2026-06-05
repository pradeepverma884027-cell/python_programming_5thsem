# List representing bus seats
# 1 = Booked Seat
# 0 = Available Seat
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Counter for booked seats
booked_seats = 0

# Counter for available seats
available_seats = 0

# List to store available seat numbers
available_seat_numbers = []

# Traverse through the seats list using index
for i in range(len(seats)):

    # Check if seat is booked
    if seats[i] == 1:
        booked_seats += 1

    # Check if seat is available
    else:
        available_seats += 1

        # Store seat number (index + 1)
        available_seat_numbers.append(i + 1)

# Find first available seat
for i in range(len(seats)):
    if seats[i] == 0:
        s = i + 1
        break

# Calculate occupancy percentage
occupancy = ((booked_seats / (booked_seats + available_seats)) * 100)

# Display results
print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)
print("First Available Seat:", s)
print("Available Seat Numbers:", available_seat_numbers)
print("Bus Occupancy:", occupancy, "%")

# Check occupancy status
if occupancy < 70:
    print("Status: Not More Than 70% Occupied")
