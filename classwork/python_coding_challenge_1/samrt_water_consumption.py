'''Smart Water Consumption Monitoring System 
Problem Statement 
Monthly water consumption (in litres) of households is recorded below. 
Sample Data 
water_usage = { 
    "House101": 1800, 
    "House102": 2200, 
    "House103": 3500, 
    "House104": 2800, 
    "House105": 1600, 
    "House106": 4100, 
    "House107": 2400, 
    "House108": 3900, 
    "House109": 1500, 
    "House110": 4500 
} 
Tasks 
1. Display houses consuming more than 3000 litres.  
2. Find the highest and lowest consumers.  
3. Calculate total water consumption.  
4. Categorize houses:  
o Low (<2000 litres)  
o Medium (2000–3500 litres)  
o High (>3500 litres)  
5. Count households eligible for conservation awareness programs (>2500 litres).  
Sample Output 
Houses Consuming More Than 3000 Litres: 
House103 
House106 
House108 
House110 
 
Highest Consumption: 
House110 (4500 litres) 
 
Lowest Consumption: 
House109 (1500 litres) 
 
Total Consumption: 28,300 litres 
 
Low Consumption: 
['House101', 'House105', 'House109'] 
 
Medium Consumption: 
['House102', 'House103', 'House104', 'House107'] 
 
High Consumption: 
['House106', 'House108', 'House110'] 
 
Eligible Households: 5'''
# Smart Water Consumption Monitoring System

water_usage = {
    "House101": 1800,
    "House102": 2200,
    "House103": 3500,
    "House104": 2800,
    "House105": 1600,
    "House106": 4100,
    "House107": 2400,
    "House108": 3900,
    "House109": 1500,
    "House110": 4500
}

# 1. Display houses consuming more than 3000 litres
print("Houses Consuming More Than 3000 Litres:")

for house in water_usage:
    if water_usage[house] > 3000:
        print(house)

# 2. Find highest and lowest consumers
houses = list(water_usage.keys())

highest = houses[0]
lowest = houses[0]

for house in water_usage:

    if water_usage[house] > water_usage[highest]:
        highest = house

    if water_usage[house] < water_usage[lowest]:
        lowest = house

print("\nHighest Consumption:")
print(highest, "(", water_usage[highest], "litres )")

print("\nLowest Consumption:")
print(lowest, "(", water_usage[lowest], "litres )")

# 3. Calculate total water consumption
total_consumption = 0

for house in water_usage:
    total_consumption += water_usage[house]

print("\nTotal Consumption:", total_consumption, "litres")

# 4. Categorize houses
low = []
medium = []
high = []

for house in water_usage:

    if water_usage[house] < 2000:
        low.append(house)

    elif water_usage[house] <= 3500:
        medium.append(house)

    else:
        high.append(house)

print("\nLow Consumption:")
print(low)

print("\nMedium Consumption:")
print(medium)

print("\nHigh Consumption:")
print(high)

# 5. Count households eligible for conservation awareness programs
eligible_count = 0

for house in water_usage:

    if water_usage[house] > 2500:
        eligible_count += 1

print("\nEligible Households:", eligible_count)
