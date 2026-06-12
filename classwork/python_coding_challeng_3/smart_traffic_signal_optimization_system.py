 Smart Traffic Signal Optimization System 
Problem Statement 
Vehicle counts recorded at a junction every 15 minutes are stored as follows: 
traffic = [120, 95, 140, 180, 75, 60, 200, 160, 110, 85] 
Tasks 
1. Classify traffic conditions:  
o Low (< 80 vehicles)  
o Moderate (80–150 vehicles)  
o High (> 150 vehicles)  
2. Count occurrences of each traffic condition.  
3. Find the peak traffic interval.  
4. Create separate lists for each traffic category.  
5. Recommend whether manual traffic control is required (more than 3 High traffic intervals).  
Sample Output 
Traffic Conditions: 
120 → Moderate 
95 → Moderate 
140 → Moderate 
180 → High 
75 → Low 
60 → Low 
200 → High 
160 → High 
110 → Moderate 
85 → Moderate 
 
Low Traffic Intervals: 2 
Moderate Traffic Intervals: 5 
High Traffic Intervals: 3 
 
Peak Traffic Count: 
200 vehicles 
 
Low Traffic List: 
[75, 60] 
 
Moderate Traffic List: 
[120, 95, 140, 110, 85] 
 
High Traffic List: 
[180, 200, 160] 
 
Manual Traffic Control Required: 
No 
 



# Smart Traffic Signal Optimization System

# Vehicle counts recorded at a junction
traffic = [120, 95, 140, 180, 75, 60, 200, 160, 110, 85]

# Function to analyze traffic data
def traffic_analysis(traffic_data):

    try:
        # Lists for different traffic categories
        low_traffic = []
        moderate_traffic = []
        high_traffic = []

        print("Traffic Conditions:")

        # Classify traffic conditions
        for count in traffic_data:

            if count < 80:
                low_traffic.append(count)
                print(count, "→ Low")

            elif count <= 150:
                moderate_traffic.append(count)
                print(count, "→ Moderate")

            else:
                high_traffic.append(count)
                print(count, "→ High")

        # Display counts
        print("\nLow Traffic Intervals:", len(low_traffic))
        print("Moderate Traffic Intervals:", len(moderate_traffic))
        print("High Traffic Intervals:", len(high_traffic))

        # Find peak traffic count
        peak_traffic = max(traffic_data)

        print("\nPeak Traffic Count:")
        print(peak_traffic, "vehicles")

        # Display categorized lists
        print("\nLow Traffic List:")
        print(low_traffic)

        print("\nModerate Traffic List:")
        print(moderate_traffic)

        print("\nHigh Traffic List:")
        print(high_traffic)

        # Check if manual traffic control is required
        print("\nManual Traffic Control Required:")

        if len(high_traffic) > 3:
            print("Yes")
        else:
            print("No")

    except ValueError:
        print("Error: Traffic data is empty.")

    except Exception as e:
        print("Error:", e)


# Function Call
traffic_analysis(traffic)
