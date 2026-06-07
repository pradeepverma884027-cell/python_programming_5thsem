'''Sample Data 
prices = { 
    "Laptop": 55000, 
    "Mouse": 800, 
    "Keyboard": 1800, 
    "Monitor": 12000, 
    "Printer": 9000, 
    "Tablet": 28000, 
    "Speaker": 3500, 
    "Webcam": 2500, 
    "Headphones": 4200, 
    "Router": 3200 
} 
Tasks 
• Display products costing more than ₹5000.  
• Count products costing less than ₹3000.  
• Find the most expensive product.  
• Create a list of products priced between ₹2000 and ₹10000.  
• Calculate the total value of all products'''

'''
Product Price Analysis
'''

# Dictionary containing product names and prices
prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# --------------------------------------------------
# Task 1: Display products costing more than ₹5000
# --------------------------------------------------

print("Products costing more than ₹5000:")

# Traverse dictionary
for product, price in prices.items():

    # Check if price is greater than 5000
    if price > 5000:
        print(product)

print("-----------------------------------")

# --------------------------------------------------
# Task 2: Count products costing less than ₹3000
# --------------------------------------------------

count = 0

# Traverse price values
for price in prices.values():

    # Check if price is less than 3000
    if price < 3000:
        count += 1

print("Number of products costing less than ₹3000:")
print(count)

print("-----------------------------------")

# --------------------------------------------------
# Task 3: Find the most expensive product
# --------------------------------------------------

# Assume first product is the most expensive
max_product = list(prices.keys())[0]

# Store price of first product
max_price = prices[max_product]

# Traverse dictionary
for product, price in prices.items():

    # Update maximum price and product
    if price > max_price:
        max_price = price
        max_product = product

print("Most Expensive Product:")
print(max_product,"-> Price:", max_price)

print("-----------------------------------")

# --------------------------------------------------
# Task 4: Create a list of products priced between ₹2000 and ₹10000
# --------------------------------------------------

products_range = []

# Traverse dictionary
for product, price in prices.items():

    # Check if price lies between 2000 and 10000
    if (2000 <= price and price  <= 10000):
        products_range.append(product)

print("Products priced between ₹2000 and ₹10000:")
print(products_range)

print("-----------------------------------")

# --------------------------------------------------
# Task 5: Calculate total value of all products
# --------------------------------------------------

total_value = 0

# Add all product prices
for price in prices.values():
    total_value += price

print("Total Value of All Products:")
print(total_value)
