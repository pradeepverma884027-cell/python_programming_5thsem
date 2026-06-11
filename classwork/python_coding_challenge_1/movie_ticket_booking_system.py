'''Movie Ticket Booking System 
Problem Statement 
Seat booking status in a cinema hall is stored as follows. 
Sample Data 
tickets = { 
    "A1": "Booked", 
    "A2": "Available", 
    "A3": "Booked", 
    "A4": "Available", 
    "B1": "Booked", 
    "B2": "Available", 
    "B3": "Booked", 
    "B4": "Available", 
    "C1": "Booked", 
    "C2": "Available" 
} 
Tasks 
1. Display available seats.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Save updated booking details to tickets.txt.  
5. Calculate hall occupancy percentage.  
Sample Output 
Available Seats: 
A2 
A4 
B2 
B4 
C2 
 
Booked Seats: 5 
Available Seats: 5 
 
Seat A2 Reserved Successfully. 
 
Hall Occupancy Percentage: 60.0% 
 
Booking Details Saved Successfully. '''

# Movie Ticket Booking System

# Dictionary storing seat number and booking status
tickets = {
    "A1": "Booked",
    "A2": "Available",
    "A3": "Booked",
    "A4": "Available",
    "B1": "Booked",
    "B2": "Available",
    "B3": "Booked",
    "B4": "Available",
    "C1": "Booked",
    "C2": "Available"
}

# --------------------------------------------------
# Task 1: Display Available Seats
# --------------------------------------------------

print("Available Seats:")

# Traverse dictionary
for seat, status in tickets.items():

    # Display available seats
    if status == "Available":
        print(seat)

# --------------------------------------------------
# Task 2: Count Booked and Available Seats
# --------------------------------------------------

booked_count = 0
available_count = 0

# Traverse seat status
for status in tickets.values():

    # Count booked seats
    if status == "Booked":
        booked_count += 1

    # Count available seats
    else:
        available_count += 1

print("\nBooked Seats:", booked_count)
print("Available Seats:", available_count)

# --------------------------------------------------
# Task 3: Reserve First Available Seat
# --------------------------------------------------

# Traverse dictionary
for seat, status in tickets.items():

    # Check first available seat
    if status == "Available":

        # Reserve seat
        tickets[seat] = "Booked"

        print(f"\nSeat {seat} Reserved Successfully.")

        # Stop after first reservation
        break

# --------------------------------------------------
# Task 4: Save Updated Booking Details to File
# --------------------------------------------------

# Open file in write mode
file = open("tickets.txt", "w")

# Write updated details
for seat, status in tickets.items():
    file.write(seat + "," + status + "\n")

# Close file
file.close()

print("\nBooking Details Saved Successfully.")

# --------------------------------------------------
# Task 5: Calculate Hall Occupancy Percentage
# --------------------------------------------------

booked_count = 0

# Count booked seats after reservation
for status in tickets.values():

    if status == "Booked":
        booked_count += 1

# Calculate occupancy percentage
occupancy_percentage = (booked_count / len(tickets)) * 100

print("\nHall Occupancy Percentage:", occupancy_percentage, "%")
