units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
    category = "Low"

elif units <= 200:
    bill = units * 7
    category = "Medium"

else:
    bill = units * 10
    category = "High"

print("Units Consumed =", units)
print("Total Bill = ₹", bill)
print("Category =", category)
