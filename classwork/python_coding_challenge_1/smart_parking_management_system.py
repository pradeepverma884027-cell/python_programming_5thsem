''': Smart Parking Management System 
Problem Statement 
The parking status of vehicles in a mall is maintained as follows. 
Sample Data 
parking_slots = [ 
    "Occupied", "Vacant", "Occupied", "Vacant", 
    "Occupied", "Occupied", "Vacant", "Occupied", 
    "Vacant", "Occupied" 
] 
Tasks 
1. Display vacant parking slot numbers.  
2. Count occupied and vacant slots.  
3. Allocate the first vacant slot to a new vehicle.  
4. Calculate parking occupancy percentage.  
5. Store updated parking information in parking.txt.  
Sample Output 
Vacant Parking Slots: 
2 4 7 9 
Occupied Slots: 6 
Vacant Slots: 4 
Vehicle Allocated to Slot 2 
Occupancy Percentage: 70.0% 
Parking Details Saved Successfully. '''



# Smart Parking Management System

# List storing parking slot status
parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

# --------------------------------------------------
# Task 1: Display vacant parking slot numbers
# --------------------------------------------------

print("Vacant Parking Slots:")

# Traverse parking slots
for i in range(len(parking_slots)):

    # Display slot number if vacant
    if parking_slots[i] == "Vacant":
        print(i + 1, end=" ")

print()

# --------------------------------------------------
# Task 2: Count occupied and vacant slots
# --------------------------------------------------

occupied_count = 0
vacant_count = 0

# Traverse parking slots
for slot in parking_slots:

    # Count occupied slots
    if slot == "Occupied":
        occupied_count += 1

    # Count vacant slots
    else:
        vacant_count += 1

print("\nOccupied Slots:", occupied_count)
print("Vacant Slots:", vacant_count)

# --------------------------------------------------
# Task 3: Allocate first vacant slot
# --------------------------------------------------

# Traverse parking slots
for i in range(len(parking_slots)):

    # Check for first vacant slot
    if parking_slots[i] == "Vacant":

        # Allocate slot to vehicle
        parking_slots[i] = "Occupied"

        print("\nVehicle Allocated to Slot", i + 1)

        # Stop after first allocation
        break

# --------------------------------------------------
# Task 4: Calculate parking occupancy percentage
# --------------------------------------------------

occupied_count = 0

# Count occupied slots after allocation
for slot in parking_slots:

    if slot == "Occupied":
        occupied_count += 1

# Calculate occupancy percentage
occupancy_percentage = (occupied_count / len(parking_slots)) * 100

print("\nOccupancy Percentage:", occupancy_percentage, "%")

# --------------------------------------------------
# Task 5: Store updated parking information in file
# --------------------------------------------------

# Open file in write mode
file = open("parking.txt", "w")

# Write parking details to file
for i in range(len(parking_slots)):
    file.write("Slot "+ str(i + 1)+" : "+ parking_slots[i]+"\n")

# Close the file
file.close()

print("\nParking Details Saved Successfully.")
