'''Movie Rating Analysis System 
Problem Statement 
Ratings given by users for movies are stored below. 
Sample Data 
ratings = { 
    "Inception": 4.8, 
    "Avatar": 4.3, 
    "Titanic": 4.5, 
    "Joker": 4.7, 
    "Frozen": 3.8, 
    "Interstellar": 4.9, 
    "Dune": 4.6, 
    "Up": 4.1, 
    "Coco": 4.4, 
    "Cars": 3.9 
} 
Tasks 
1. Display movies rated above 4.5.  
2. Find the highest-rated movie.  
3. Find the lowest-rated movie.  
4. Calculate average rating.  
5. Create a recommendation list (rating ≥ 4.5).  
Sample Output 
Movies Rated Above 4.5: 
Inception 
Joker 
Interstellar 
Dune 
 
Highest Rated Movie: 
Interstellar (4.9) 
 
Lowest Rated Movie: 
Frozen (3.8) 
 
Average Rating: 4.4 
 
Recommended Movies: 
['Inception', 'Titanic', 'Joker', 'Interstellar', 'Dune']'''
# Movie Rating Analysis System

# Dictionary storing movie names and their ratings
ratings = {
    "Inception": 4.8,
    "Avatar": 4.3,
    "Titanic": 4.5,
    "Joker": 4.7,
    "Frozen": 3.8,
    "Interstellar": 4.9,
    "Dune": 4.6,
    "Up": 4.1,
    "Coco": 4.4,
    "Cars": 3.9
}

# --------------------------------------------------
# Task 1: Display movies rated above 4.5
# --------------------------------------------------

print("Movies Rated Above 4.5:")

# Traverse the dictionary and check movie ratings
for movie, rating in ratings.items():
    if rating > 4.5:
        print(movie)

# --------------------------------------------------
# Task 2: Find the highest-rated movie
# --------------------------------------------------

# Assume the first movie has the highest rating initially
highest_movie = list(ratings.keys())[0]
highest_rating = ratings[highest_movie]

# Compare ratings of all movies
for movie, rating in ratings.items():
    if rating > highest_rating:
        highest_rating = rating
        highest_movie = movie

print("\nHighest Rated Movie:")
print(highest_movie, f"({highest_rating})")

# --------------------------------------------------
# Task 3: Find the lowest-rated movie
# --------------------------------------------------

# Assume the first movie has the lowest rating initially
lowest_movie = list(ratings.keys())[0]
lowest_rating = ratings[lowest_movie]

# Compare ratings of all movies
for movie, rating in ratings.items():
    if rating < lowest_rating:
        lowest_rating = rating
        lowest_movie = movie

print("\nLowest Rated Movie:")
print(lowest_movie, f"({lowest_rating})")

# --------------------------------------------------
# Task 4: Calculate average rating
# --------------------------------------------------

total_rating = 0

# Add ratings of all movies
for rating in ratings.values():
    total_rating += rating

# Calculate average rating
average_rating = total_rating / len(ratings)

print("\nAverage Rating:", round(average_rating, 1))

# --------------------------------------------------
# Task 5: Create a recommendation list
# (Movies with rating greater than or equal to 4.5)
# --------------------------------------------------

recommended_movies = []

# Check eligibility for recommendation
for movie, rating in ratings.items():
    if rating >= 4.5:
        recommended_movies.append(movie)

print("\nRecommended Movies:")
print(recommended_movies)
