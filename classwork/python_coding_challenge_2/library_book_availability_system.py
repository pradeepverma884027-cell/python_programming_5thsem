'''Library Book Availability System 
Problem Statement 
The number of available copies of books in a library is stored below. 
Sample Data 
books = { 
    "Python": 5, 
    "Java": 2, 
    "DBMS": 4, 
    "Networking": 1, 
    "OS": 3, 
    "AI": 6, 
    "ML": 2, 
    "Cloud": 5, 
    "Cyber Security": 1, 
    "Web Development": 4 
} 
Tasks 
1. Display books with fewer than 3 copies.  
2. Find the book with maximum copies.  
3. Find the book with minimum copies.  
4. Count total books available.  
5. Generate a restocking list.  
Sample Output 
Books Requiring Attention: 
Java 
Networking 
ML 
Cyber Security 
 
Book with Maximum Copies: 
AI (6 copies) 
 
Book with Minimum Copies: 
Networking (1 copy) 
 
Total Copies Available: 33 
 
Generate a restocking list.  
['Java', 'Networking', 'ML', 'Cyber Security']'''



#creating dictionary of sample data of books

books = { 
    "Python": 5, 
    "Java": 2, 
    "DBMS": 4, 
    "Networking": 1, 
    "OS": 3, 
    "AI": 6, 
    "ML": 2, 
    "Cloud": 5, 
    "Cyber Security": 1, 
    "Web Development": 4 
}

#1. Display books with fewer than 3 copies.  

for book,stock in books.items():
    if stock<3:
        print(book)

#  2. Find the book with maximum copies.  

book_max=list(books.keys())[0]
copy_max=books[book_max]

for book,stock in books.items():
    if stock>copy_max:
        book_max=book
        copy_max=stock

print("Book with Maximum Copies: ")
print(book_max, copy_max, "copies")

#  2. Find the book with minimum copies.  

book_min=list(books.keys())[0]
copy_min=books[book_min]

for book,stock in books.items():
    if stock<copy_min:
        book_min=book
        copy_min=stock

print("Book with Minimum Copies: ")
print(book_min, copy_min, "copies")


#Count total books available.

total=sum(books.values())

print("Total Copies Available: ",total)

#Generate a restocking list.  
restock=[]
for book ,stock in books.items():
    if stock<3:
        restock.append(book)
print("Generate a restocking list. ")
print(restock)
