# Lift starts at floor 0
current_floor = 0

# Store total floors travelled
total_travelled = 0

while True:
    # Input destination floor
    destination = int(input("Enter Destination (-1 to stop): "))

    # Stop when -1 is entered
    if destination == -1:
        break

    # Calculate floors travelled in this trip
    travelled = abs(destination - current_floor)

    # Display floors travelled
    print("Travelled:", travelled, "floors")

    # Add to total floors travelled
    total_travelled += travelled

    # Update current floor
    current_floor = destination

# Display total floors travelled
print("Total Travelled:", total_travelled, "floors")
