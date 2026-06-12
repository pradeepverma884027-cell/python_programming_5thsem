'''Smart City Waste Collection Management System 
Problem Statement 
The amount of waste collected (in kilograms) from different sectors of a city is stored below. 
Sample Data 
    "Sector2": 180, 
    "Sector3": 510, 
    "Sector4": 275, 
    "Sector5": 150, 
    "Sector6": 430, 
    "Sector7": 220, 
    "Sector8": 390, 
    "Sector9": 145, 
    "Sector10": 600 
} 
Tasks 
1. Display sectors generating more than 400 kg of waste.  
2. Find the sector generating maximum waste.  
3. Find the sector generating minimum waste.  
4. Calculate the total waste collected.  
5. Categorize sectors:  
o Low Waste (<200 kg)  
o Medium Waste (200–400 kg)  
o High Waste (>400 kg)  
6. Count sectors requiring awareness campaigns (waste generation >300 kg).  
7. Save the awareness campaign list to campaign_sectors.txt.  
Sample Output 
Sectors Generating More Than 400 kg Waste: 
Sector3 
Sector6 
Sector10 
 
Maximum Waste Generation: 
Sector10 (600 kg) 
 
Minimum Waste Generation: 
Sector9 (145 kg) 
 
Total Waste Collected: 3220 kg 
 
Low Waste: 
['Sector2', 'Sector5', 'Sector9'] 
 
Medium Waste: 
['Sector1', 'Sector4', 'Sector7', 'Sector8'] 
 
High Waste: 
['Sector3', 'Sector6', 'Sector10'] 
 
Sectors Requiring Awareness Campaign: 
Sector1 
Sector3 
Sector6 
Sector8 
Sector10 
 
Campaign Report Generated Successfully.'''
# Smart City Waste Collection Management System

waste_data = {
    "Sector1": 320,
    "Sector2": 180,
    "Sector3": 510,
    "Sector4": 275,
    "Sector5": 150,
    "Sector6": 430,
    "Sector7": 220,
    "Sector8": 390,
    "Sector9": 145,
    "Sector10": 600
}

# 1. Display sectors generating more than 400 kg waste
print("Sectors Generating More Than 400 kg Waste:")

for sector in waste_data:
    if waste_data[sector] > 400:
        print(sector)

# 2. Find maximum and minimum waste generating sectors
sectors = list(waste_data.keys())

max_sector = sectors[0]
min_sector = sectors[0]

for sector in waste_data:

    if waste_data[sector] > waste_data[max_sector]:
        max_sector = sector

    if waste_data[sector] < waste_data[min_sector]:
        min_sector = sector

print("\nMaximum Waste Generation:")
print(max_sector, "(", waste_data[max_sector], "kg )")

print("\nMinimum Waste Generation:")
print(min_sector, "(", waste_data[min_sector], "kg )")

# 3. Calculate total waste collected
total_waste = 0

for sector in waste_data:
    total_waste = total_waste + waste_data[sector]

print("\nTotal Waste Collected:", total_waste, "kg")

# 4. Categorize sectors
low_waste = []
medium_waste = []
high_waste = []

for sector in waste_data:

    if waste_data[sector] < 200:
        low_waste.append(sector)

    elif waste_data[sector] <= 400:
        medium_waste.append(sector)

    else:
        high_waste.append(sector)

print("\nLow Waste:")
print(low_waste)

print("\nMedium Waste:")
print(medium_waste)

print("\nHigh Waste:")
print(high_waste)

# 5. Count sectors requiring awareness campaigns
campaign_count = 0
campaign_sectors = []

for sector in waste_data:

    if waste_data[sector] > 300:
        campaign_count += 1
        campaign_sectors.append(sector)

print("\nSectors Requiring Awareness Campaign:")

for sector in campaign_sectors:
    print(sector)

print("\nTotal Sectors Requiring Campaign:", campaign_count)

# 6. Save campaign sectors to file
file = open("campaign_sectors.txt", "w")

for sector in campaign_sectors:
    file.write(sector + "\n")

file.close()

print("\nCampaign Report Generated Successfully.")
