'''Sample Data 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 450, 
    "House104": 290, 
    "House105": 150, 
    "House106": 510, 
    "House107": 220, 
    "House108": 390, 
    "House109": 170, 
    "House110": 260 
} 
Tasks 
• Display houses consuming more than 300 units.  
• Count houses consuming less than 200 units.  
• Find the house with the highest consumption.  
• Create a list of houses eligible for an energy-saving awareness campaign (consumption > 400 units).  
• Categorize houses as:  
o Low: < 200 units  
o Medium: 200–350 units  
o High: > 350 units '''

'''
Electricity Consumption Analysis
'''

# Dictionary containing house numbers and electricity units consumed
units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# --------------------------------------------------
# Task 1: Display houses consuming more than 300 units
# --------------------------------------------------

print("Houses consuming more than 300 units:")

# Traverse dictionary
for house, unit in units.items():

    # Check if consumption is greater than 300
    if unit > 300:
        print(house)

print("-----------------------------------")

# --------------------------------------------------
# Task 2: Count houses consuming less than 200 units
# --------------------------------------------------

count = 0

# Traverse unit values
for unit in units.values():

    # Check if consumption is less than 200
    if unit < 200:
        count += 1

print("Houses consuming less than 200 units:", count)

print("-----------------------------------")

# --------------------------------------------------
# Task 3: Find the house with highest consumption
# --------------------------------------------------

# Assume first house has highest consumption
highest_house = list(units.keys())[0]

# Store consumption of first house
highest_units = units[highest_house]

# Traverse dictionary
for house, unit in units.items():

    # Update highest consumption and house
    if unit > highest_units:
        highest_units = unit
        highest_house = house

print("House with Highest Consumption:", highest_house)
print("Units Consumed:", highest_units)

print("-----------------------------------")

# --------------------------------------------------
# Task 4: Create list of houses eligible for energy-saving awareness campaign (consumption > 400 units)
# --------------------------------------------------

campaign_houses = []

# Traverse dictionary
for house, unit in units.items():

    # Check campaign eligibility
    if unit > 400:
        campaign_houses.append(house)

print("Houses Eligible for Awareness Campaign:")
print(campaign_houses)

print("-----------------------------------")

# --------------------------------------------------
# Task 5: Categorize houses
# --------------------------------------------------

print("House Categories:")

# Traverse dictionary
for house, unit in units.items():

    # Low consumption category
    if unit < 200:
        category = "Low"

    # Medium consumption category
    elif 200 <= unit <= 350:
        category = "Medium"

    # High consumption category
    else:
        category = "High"

    print(house, "->", category)
