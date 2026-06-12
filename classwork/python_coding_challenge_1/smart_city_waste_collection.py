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
