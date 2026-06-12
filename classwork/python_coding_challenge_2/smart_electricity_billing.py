
'''Problem 1: Smart Electricity Billing System 
Problem Statement 
Monthly electricity consumption (units) of different houses in a residential society is stored as follows: 
Sample Data 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 
Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate the total units consumed.  
5. Create separate lists for:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300).  
Sample Output 
Houses Consuming More Than 400 Units: 
House103 
House106 
House110 
 
Highest Consumption: 
House110 (600 units) 
 
Lowest Consumption: 
House109 (145 units) 
 
Total Units Consumed: 3220 
 
Low Consumption: 
['House102', 'House105', 'House109'] 
 
Medium Consumption: 
['House101', 'House104', 'House107', 'House108'] 
 
High Consumption: 
['House103', 'House106', 'House110'] 
 
Eligible for Energy-Saving Campaign: 5'''

#creating dictionary of units consumed
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
}

#1. Display houses consuming more than 400 units.  
print("Houses consuming more than  400 units: ")
for house,unit in units.items():
    if unit>400:
        print(house)


# house with highest units
highest_house = list(units.keys())[0]
highest_units = units[highest_house]

for house, consumption in units.items():
    if consumption > highest_units:
        highest_units = consumption
        highest_house = house

print("\nHighest Consumption:")
print(highest_house, highest_units, "units")


#house with lowest unit
lowest_house = list(units.keys())[0]
lowest_unit = units[lowest_house]

for house, unit in units.items():
    if unit < lowest_unit:
        lowest_unit = unit
        lowest_house = house

print("\nLowest Consumption:")
print(lowest_house, lowest_unit, "units")


#Calculate the total units consumed.
total_bill=sum(units.values())

print("Total Units Consumed: ",total_bill)


'''Create separate lists for:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  '''


low_consumption=[]
medium_consumption=[]

high_consumption=[]

for house,unit in units.items():
    if unit<200:
        low_consumption.append(house)

    if unit>200 and unit<400:
        medium_consumption.append(house)

    if unit>400:
        high_consumption.append(house)



print("Low Consumption:") 
print(low_consumption)
 
print("Medium Consumption: ")
print(medium_consumption)
 
print("High Consumption:") 
print(high_consumption)

#6. Count houses eligible for an energy-saving campaign (consumption > 300).  
count=0#for counting houses eligible for an energy-saving campaign (consumption > 300).  
for house, unit in units.items():
    if unit>300:
        count+=1

print("Eligible for Energy-Saving Campaign: ",count)
