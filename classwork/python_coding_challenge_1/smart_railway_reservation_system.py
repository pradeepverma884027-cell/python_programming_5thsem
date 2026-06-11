# Smart Railway Reservation System

# Dictionary storing seat numbers and their booking status
seats = {
    1: "Booked",
    2: "Available",
    3: "Booked",
    4: "Available",
    5: "Booked",
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}

# --------------------------------------------------
# Task 1: Display all available seat numbers
# --------------------------------------------------
print("Available Seats:")

# Traverse the dictionary
for seat, status in seats.items():

    # Display seat number if seat is available
    if status == "Available":
        print(seat, end=" ")

print()

# --------------------------------------------------
# Task 2: Count booked and available seats
# --------------------------------------------------
booked_count = 0
available_count = 0

# Traverse all seat statuses
for status in seats.values():

    # Count booked seats
    if status == "Booked":
        booked_count += 1

    # Count available seats
    else:
        available_count += 1

# Display counts
print("\nBooked Seats:", booked_count)
print("Available Seats:", available_count)

# --------------------------------------------------
# Task 3: Reserve the first available seat
# --------------------------------------------------

# Traverse dictionary
for seat, status in seats.items():

    # Check for first available seat
    if status == "Available":

        # Reserve the seat
        seats[seat] = "Booked"

        print(f"\nSeat {seat} Reserved Successfully.")

        # Stop after reserving first available seat
        break

# --------------------------------------------------
# Task 4: Cancel booking for a given seat number
# --------------------------------------------------

# Take seat number input from user
seat_no = int(input("\nEnter Seat Number to Cancel Booking: "))

# Check whether seat number exists
if seat_no in seats:

    # Check if seat is booked
    if seats[seat_no] == "Booked":

        # Cancel booking
        seats[seat_no] = "Available"

        print("Booking Cancelled Successfully.")

    else:
        print("Seat is Already Available.")

else:
    print("Invalid Seat Number.")

# --------------------------------------------------
# Task 5: Store updated reservation status in file
# --------------------------------------------------

# Open file in write mode
file = open("reservations.txt", "w")

# Write seat details into file
for seat, status in seats.items():
    file.write(f"Seat {seat} : {status}\n")

# Close the file
file.close()

print("\nReservation Details Saved Successfully.")

# --------------------------------------------------
# Task 6: Display occupancy percentage
# --------------------------------------------------

# Recalculate booked seats after updates
booked_count = 0

# Traverse seat statuses
for status in seats.values():

    # Count booked seats
    if status == "Booked":
        booked_count += 1

# Calculate occupancy percentage
occupancy_percentage = (booked_count / len(seats)) * 100

# Display occupancy percentage
print("\nOccupancy Percentage:", occupancy_percentage, "%")

