# List representing stock quantities of products
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# Counter for products that are out of stock
out_of_stocks = 0

# List to store products that need restocking
restock = []

# Counter for products that are currently available
available = 0

# List to store products with healthy stock levels
healthy_stock = []

# Traverse through each stock quantity
for i in stock:

    # Check if the product is out of stock
    if i == 0:
        out_of_stocks += 1

    # Check if the stock is low (less than 10)
    if i < 10:
        restock.append(i)

    # Count products that are available in stock
    if i > 0:
        available += 1

    # Store products having healthy stock (more than 15)
    if i > 15:
        healthy_stock.append(i)

# Display results
print("Out of Stock Products:", out_of_stocks)
print("Restock required:", restock)
print("Available Products:", available)
print("Healthy Products:", healthy_stock)
