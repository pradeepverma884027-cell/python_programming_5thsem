'''
Inventory Analysis
'''

# Creating sample inventory data
# Key   -> Product Name
# Value -> Stock Available
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# --------------------------------------------------
# Task 1: Display products with stock less than 10
# --------------------------------------------------

print("Products with stock less than 10:")

# Traverse the dictionary
for product, stock in inventory.items():

    # Check if stock is less than 10
    if stock < 10:
        print(product)

print("------------------------------------")

# --------------------------------------------------
# Task 2: Count products having stock more than 50
# --------------------------------------------------

# Counter variable
count = 0

print("Number of products with stock more than 50:")

# Traverse only stock values
for stock in inventory.values():

    # Check if stock is greater than 50
    if stock > 50:
        count += 1

# Display count
print(count)

print("-----------------------------------")

# --------------------------------------------------
# Task 3: Find product with minimum stock
# --------------------------------------------------

# Assume first product has minimum stock initially
min_product = list(inventory.keys())[0]

# Get stock of first product
min_stock = inventory[min_product]

# Traverse dictionary
for product, stock in inventory.items():

    # Update minimum stock product if smaller stock found
    if stock < min_stock:
        min_stock = stock
        min_product = product

# Display product with minimum stock
print("Product with Minimum Stock:", min_product)
print("Stock:", min_stock)

print("-----------------------------------")

# --------------------------------------------------
# Task 4: Create list of products that require
# restocking (stock < 20)
# --------------------------------------------------

print("Products that need restocking:")

# Empty list to store products needing restock
restocking = []

# Traverse dictionary
for product, stock in inventory.items():

    # Check if stock is below 20
    if stock < 20:
        restocking.append(product)

# Display list
print(restocking)

print("-----------------------------------")

# --------------------------------------------------
# Task 5: Calculate total inventory count
# --------------------------------------------------

print("Total inventory stock:")

# Variable to store total stock
total = 0

# Add stock of all products
for stock in inventory.values():
    total += stock

# Display total stock
print(total)
