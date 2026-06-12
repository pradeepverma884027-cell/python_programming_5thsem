'''Daily Sales Performance Analyzer 
Problem Statement 
Daily sales figures (in ₹) for 10 days are stored in a list. 
Sample Data 
sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000] 
Tasks 
1. Find the highest sales.  
2. Find the lowest sales.  
3. Calculate average sales.  
4. Count days with sales above ₹20,000.  
5. Display sales figures below average.  
Sample Output 
Highest Sales: ₹30,000 
 
Lowest Sales: ₹15,000 
 
Average Sales: ₹22,100 
 
Days with Sales Above ₹20,000: 5 
 
Sales Below Average: 
[15000, 18000, 17000, 21000, 19000] 
 

# Daily Sales Performance Analyzer

# List storing daily sales figures
sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000]

# --------------------------------------------------
# Task 1: Find the highest sales
# --------------------------------------------------

highest_sales = sales[0]

for amount in sales:
    if amount > highest_sales:
        highest_sales = amount

print("Highest Sales: ₹", highest_sales)

# --------------------------------------------------
# Task 2: Find the lowest sales
# --------------------------------------------------

lowest_sales = sales[0]

for amount in sales:
    if amount < lowest_sales:
        lowest_sales = amount

print("\nLowest Sales: ₹", lowest_sales)

# --------------------------------------------------
# Task 3: Calculate average sales
# --------------------------------------------------

total_sales = 0

for amount in sales:
    total_sales += amount

average_sales = total_sales / len(sales)

print("\nAverage Sales: ₹", average_sales)

# --------------------------------------------------
# Task 4: Count days with sales above ₹20,000
# --------------------------------------------------

count = 0

for amount in sales:
    if amount > 20000:
        count += 1

print("\nDays with Sales Above ₹20,000:", count)

# --------------------------------------------------
# Task 5: Display sales figures below average
# --------------------------------------------------

below_average = []

for amount in sales:
    if amount < average_sales:
        below_average.append(amount)

print("\nSales Below Average:")
print(below_average)
