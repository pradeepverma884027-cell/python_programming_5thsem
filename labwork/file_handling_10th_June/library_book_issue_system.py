# ---------------------------------------------------------
# LIBRARY BOOK ISSUE SYSTEM
# ---------------------------------------------------------

FILE_NAME = "books.txt"  # Name of the file where book data is stored


# -------------------------------------------------------
# Function to load books from file
# Returns a list of book dictionaries
# -------------------------------------------------------
def load_books():

    books = []  # Empty list to store all books

    try:
        file = open(FILE_NAME, "r")  # Open file in read mode

        for line in file:

            data = line.strip().split(",")  # Remove whitespace and split by comma

            # Only process lines that have exactly 3 values (id, name, copies)
            if len(data) == 3:

                book = {
                    "id":     data[0],        # Book ID (e.g. B001)
                    "name":   data[1],        # Book Name
                    "copies": int(data[2])    # Number of copies (converted to int)
                }

                books.append(book)  # Add book to list

        file.close()  # Always close the file after reading

    except FileNotFoundError:
        # If books.txt doesn't exist, inform user and return empty list
        print("Warning: books.txt not found. Starting with empty book list.")

    return books  # Return the list of books


# -------------------------------------------------------
# Function to save updated book list back to file
# Overwrites the file with latest data
# -------------------------------------------------------
def save_books(books):

    file = open(FILE_NAME, "w")  # Open file in write mode (overwrites existing content)

    for book in books:

        # Format each book as: id,name,copies
        line = book["id"] + "," + book["name"] + "," + str(book["copies"]) + "\n"

        file.write(line)  # Write line to file

    file.close()  # Close file after writing


# -------------------------------------------------------
# Function to display all books in the library
# -------------------------------------------------------
def display_books():

    books = load_books()  # Load latest data from file

    print("\nALL BOOKS")
    print("-" * 40)

    if len(books) == 0:
        print("No books found in the system.")
        return

    # Print header
    print(f"{'ID':<10} {'NAME':<30} {'COPIES'}")
    print("-" * 40)

    for book in books:
        # Neatly formatted output
        print(f"{book['id']:<10} {book['name']:<30} {book['copies']}")


# -------------------------------------------------------
# Function to search a book using Book ID
# -------------------------------------------------------
def search_book():

    books = load_books()  # Load books from file

    book_id = input("Enter Book ID to search: ").strip()  # .strip() removes accidental spaces

    found = False  # Flag to track if book was found

    for book in books:

        if book["id"] == book_id:  # Match book ID

            print("\nBook Found:")
            print(f"  ID     : {book['id']}")
            print(f"  Name   : {book['name']}")
            print(f"  Copies : {book['copies']}")

            found = True
            break  # Stop searching once found

    if not found:
        print("Book not found. Please check the ID and try again.")


# -------------------------------------------------------
# Function to issue a book (reduce copy count by 1)
# -------------------------------------------------------
def book_issuing():

    books = load_books()  # Load books from file

    book_id = input("Enter Book ID to issue: ").strip()

    found = False

    for book in books:

        if book["id"] == book_id:

            found = True

            if book["copies"] > 0:  # Check if copies are available

                book["copies"] -= 1  # Reduce copy count by 1

                save_books(books)  # Save updated data to file

                print("\nBook Issued Successfully!")
                print(f"  Book Name       : {book['name']}")
                print(f"  Remaining Copies: {book['copies']}")

            else:
                # No copies available
                print(f"Sorry! '{book['name']}' is currently unavailable.")

            break  # Stop loop after finding the book

    if not found:
        print("Book not found. Please check the ID and try again.")


# -------------------------------------------------------
# Function to return a book (increase copy count by 1)
# -------------------------------------------------------
def book_returned():

    books = load_books()  # Load books from file

    book_id = input("Enter Book ID to return: ").strip()

    found = False

    for book in books:

        if book["id"] == book_id:

            found = True

            book["copies"] += 1  # Increase copy count by 1

            save_books(books)  # Save updated data to file

            print("\nBook Returned Successfully!")
            print(f"  Book Name      : {book['name']}")
            print(f"  Available Copies: {book['copies']}")

            break  # Stop loop after finding the book

    if not found:
        print("Book not found. Please check the ID and try again.")


# -------------------------------------------------------
# Function to display books with 0 copies (unavailable)
# -------------------------------------------------------
def unavailable_books():

    books = load_books()  # Load books from file

    print("\nUNAVAILABLE BOOKS (Copies = 0)")
    print("-" * 40)

    found = False

    for book in books:

        if book["copies"] == 0:  # Check for zero copies

            print(f"  {book['id']}  |  {book['name']}")

            found = True

    if not found:
        print("All books are currently available.")  # No unavailable books


# -------------------------------------------------------
# Function to display books that need restocking
# (books with less than 2 copies)
# -------------------------------------------------------
def book_restocking():

    books = load_books()  # Load books from file

    print("\nBOOKS REQUIRING RESTOCKING (Copies < 2)")
    print("-" * 40)

    found = False

    for book in books:

        if book["copies"] < 2:  # Less than 2 copies = needs restocking

            print(f"  {book['id']}  |  {book['name']}  |  Copies: {book['copies']}")

            found = True

    if not found:
        print("No books require restocking at this time.")


# -------------------------------------------------------
# MAIN MENU - Runs in a loop until user chooses to exit
# -------------------------------------------------------

while True:

    # Display menu options
    print("\n========================================")
    print("       LIBRARY BOOK ISSUE SYSTEM        ")
    print("========================================")
    print("  1. Display All Books")
    print("  2. Search Book by ID")
    print("  3. Issue Book")
    print("  4. Return Book")
    print("  5. Display Unavailable Books")
    print("  6. Display Books Requiring Restocking")
    print("  7. Exit")
    print("========================================")

    choice = input("Enter Your Choice (1-7): ").strip()  # Get user input

    if choice == "1":
        display_books()

    elif choice == "2":
        search_book()

    elif choice == "3":
        book_issuing()

    elif choice == "4":
        book_returned()

    elif choice == "5":
        unavailable_books()

    elif choice == "6":
        book_restocking()

    elif choice == "7":
        print("\nThank you for using the Library System. Goodbye!")
        break  # Exit the loop and end the program

    else:
        print("Invalid Choice! Please enter a number between 1 and 7.")
