'''Sample Data 
books = { 
    "Python Basics": 5, 
    "Data Structures": 0, 
    "Machine Learning": 3, 
    "Java Programming": 2, 
    "DBMS": 0, 
    "Operating Systems": 6, 
    "Networking": 4, 
    "Cloud Computing": 1, 
    "Cyber Security": 0, 
    "Web Development": 7 
} 
Tasks 
• Display books that are currently unavailable.  
• Count the number of available books.  
• Find the book with the maximum copies.  
• Create a list of books having less than 3 copies.  
• Calculate the total number of books available.  '''

'''
Library Book Analysis
'''

# Dictionary containing book names and available copies
books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# --------------------------------------------------
# Task 1: Display books that are currently unavailable
# --------------------------------------------------

print("Books currently unavailable:")

# Traverse dictionary
for book, copies in books.items():

    # Check if copies are zero
    if copies == 0:
        print(book)

print("-----------------------------------")

# --------------------------------------------------
# Task 2: Count the number of available books
# --------------------------------------------------

available_books = 0

# Traverse copy values
for copies in books.values():

    # Book is available if copies > 0
    if copies > 0:
        available_books += 1

print("Number of Available Books:", available_books)

print("-----------------------------------")

# --------------------------------------------------
# Task 3: Find the book with maximum copies
# --------------------------------------------------

# Assume first book has maximum copies
max_book = list(books.keys())[0]

# Store copies of first book
max_copies = books[max_book]

# Traverse dictionary
for book, copies in books.items():

    # Update maximum copies and book name
    if copies > max_copies:
        max_copies = copies
        max_book = book

print("Book with Maximum Copies:", max_book)
print("Copies:", max_copies)

print("-----------------------------------")

# --------------------------------------------------
# Task 4: Create a list of books
# having less than 3 copies
# --------------------------------------------------

low_stock_books = []

# Traverse dictionary
for book, copies in books.items():

    # Check if copies are less than 3
    if copies < 3:
        low_stock_books.append(book)

print("Books having less than 3 copies:")
print(low_stock_books)

print("-----------------------------------")

# --------------------------------------------------
# Task 5: Calculate total number of books available
# --------------------------------------------------

total_books = 0

# Add copies of all books
for copies in books.values():
    total_books += copies

print("Total Number of Books Available:", total_books)
