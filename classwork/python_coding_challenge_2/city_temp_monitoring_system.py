# City Temperature Monitoring System

temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Display cities with temperature above 40°C
print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)

# 2. Find the hottest city
hottest_city = max(temperature, key=temperature.get)
print("\nHottest City:")
print(f"{hottest_city} ({temperature[hottest_city]}°C)")

# 3. Find the coolest city
coolest_city = min(temperature, key=temperature.get)
print("\nCoolest City:")
print(f"{coolest_city} ({temperature[coolest_city]}°C)")

# 4. Calculate average temperature
total_temp = sum(temperature.values())
average_temp = total_temp / len(temperature)

print("\nAverage Temperature:")
print(f"{average_temp:.1f}°C")

# 5. Create a list of pleasant cities (<35°C)
pleasant_cities = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)

print("\nPleasant Cities:")
print(pleasant_cities)
