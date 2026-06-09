# CITY DATA ANALYSIS SYSTEM

# ==========================================

# CREATE DICTIONARY FOR 30 CITIES

# ==========================================

cities = {}

for i in range(1, 31):

    print(f"\nEnter Details of City {i}")

    city = input("Enter City Name: ")
    population = int(input("Enter Population: "))
    area = float(input("Enter Area (sq km): "))
    literacy = float(input("Enter Literacy Rate (%): "))

cities[city] = {
    "population": population,
    "area": area,
    "literacy": literacy
}


# ==========================================

# MENU DRIVEN PROGRAM

# ==========================================

while True:


    print("\n===================================")
    print("      CITY DATA ANALYSIS SYSTEM")
    print("===================================")

    print("1. Display All City Details")
    print("2. Most Populated City")
    print("3. Least Populated City")
    print("4. Average Population")
    print("5. Cities With Literacy Above 90%")
    print("6. Cities With Literacy Below Average")
    print("7. Population Density Report")
    print("8. Highest Density City")
    print("9. Categorize Cities")
    print("10. Development Priority List")
    print("11. High and Low Literacy Dictionaries")
    print("12. National Summary Report")
    print("13. Rank Cities By Population Density")
    print("14. Exit")

    choice = int(input("\nEnter Your Choice: "))

    # ======================================
    # 1. DISPLAY ALL CITY DETAILS
    # ======================================

    if choice == 1:

        print("\nCITY DETAILS")

        for city, details in cities.items():

            print("\nCity :", city)
            print("Population :", details["population"])
            print("Area :", details["area"])
            print("Literacy :", details["literacy"])

    # ======================================
    # 2. MOST POPULATED CITY
    # ======================================

    elif choice == 2:

        first_city = list(cities.keys())[0]

        max_city = first_city
        max_population = cities[first_city]["population"]

        for city, details in cities.items():

            if details["population"] > max_population:

                max_population = details["population"]
                max_city = city

        print("\nMost Populated City")
        print("City :", max_city)
        print("Population :", max_population)

    # ======================================
    # 3. LEAST POPULATED CITY
    # ======================================

    elif   choice == 3:

        first_city = list(cities.keys())[0]

        min_city = first_city
        min_population = cities[first_city]["population"]

        for city, details in cities.items():

            if details["population"] < min_population:

                min_population = details["population"]
                min_city = city

        print("\nLeast Populated City")
        print("City :", min_city)
        print("Population :", min_population)

    # ======================================
    # 4. AVERAGE POPULATION
    # ======================================

    elif choice == 4:

        total_population = 0

        for details in cities.values():

            total_population += details["population"]

        average_population = total_population / len(cities)

        print("\nAverage Population :", round(average_population, 2))

    # ======================================
    # 5. LITERACY ABOVE 90%
    # ======================================

    elif choice == 5:

        print("\nCities With Literacy Above 90%")

        for city, details in cities.items():

            if details["literacy"] > 90:

                print(city,
                    details["literacy"])

    # ======================================
    # 6. LITERACY BELOW AVERAGE
    # ======================================

    elif choice == 6:

        total_literacy = 0

        for details in cities.values():

            total_literacy += details["literacy"]

        average_literacy = total_literacy / len(cities)

        print("\nCities Below Average Literacy")

        for city, details in cities.items():

            if details["literacy"] < average_literacy:

                print(city,
                    details["literacy"])

    # ======================================
    # 7. POPULATION DENSITY REPORT
    # ======================================

    elif choice == 7:

        print("\nPopulation Density Report")

        for city, details in cities.items():

            density = (details["population"]/details["area"])

            print(city,"Density:",round(density, 2))

    # ======================================
    # 8. HIGHEST DENSITY CITY
    # ======================================

    elif choice == 8:

        first_city = list(cities.keys())[0]

        max_city = first_city

        max_density = (
        cities[first_city]["population"]/cities[first_city]["area"])

        for city, details in cities.items():

            density = (details["population"]/details["area"])

            if density > max_density:

                max_density = density
                max_city = city

        print("\nHighest Density City")
        print("City :", max_city)
        print("Density :", round(max_density, 2))

    # ======================================
    # 9. CITY CATEGORIES
    # ======================================

    elif choice == 9:

        print("\nCity Categories")

        for city, details in cities.items():

            population = details["population"]

            if population < 1000000:

                print(city, "- Small")

            elif population < 5000000:

                print(city, "- Medium")

            else:

                print(city, "- Large")

    # ======================================
    # 10. DEVELOPMENT PRIORITY LIST
    # ======================================

    elif choice == 10:

        print("\nDevelopment Priority Cities")

        for city, details in cities.items():

            if (
            details["literacy"] < 80 and details["population"] > 5000000):

                print(city)

    # ======================================
    # 11. HIGH & LOW LITERACY DICTIONARIES
    # ======================================

    elif choice == 11:

        high_literacy = {}
        low_literacy = {}

        for city, details in cities.items():

            if details["literacy"] >= 90:

                high_literacy[city] = details

            else:

                low_literacy[city] = details

        print("\nHIGH LITERACY CITIES")
        print(high_literacy)

        print("\nLOW LITERACY CITIES")
        print(low_literacy)

    # ======================================
    # 12. NATIONAL SUMMARY REPORT
    # ======================================

    elif choice == 12:

        total_population = 0
        total_area = 0
        total_literacy = 0

        for details in cities.values():

            total_population += details["population"]
            total_area += details["area"]
            total_literacy += details["literacy"]

        print("\nNATIONAL SUMMARY REPORT")

        print("Total Cities :", len(cities))
        print("Total Population :", total_population)
        print("Total Area :", total_area)

        print(
            "Average Literacy :",
            round(total_literacy / len(cities),2))

    # ======================================
    # 13. DENSITY RANKING
    # ======================================

    elif choice == 13:

        temp = cities.copy()

        rank = 1

        print("\nCITY DENSITY RANKING")

        while len(temp) > 0:

            first_city = list(temp.keys())[0]

            highest_city = first_city

            highest_density = (temp[first_city]["population"]/temp[first_city]["area"])

            for city, details in temp.items():

                density = (details["population"]/details["area"])

                if density > highest_density:

                    highest_density = density
                    highest_city = city

            print(rank,highest_city,round(highest_density, 2))

            del temp[highest_city]

            rank += 1

    # ======================================
    # 14. EXIT
    # ======================================

    elif choice == 14:

        print("\nProgram Ended Successfully")
        break

    else:

        print("\nInvalid Choice")
