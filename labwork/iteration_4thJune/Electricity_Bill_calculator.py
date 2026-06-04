#program to calculate the electricity bill
units = int(input("Enter units: "))
#low category
if units <= 100:
    bill = units * 5
    category = "Low"
#medium category
elif units <= 200:
    bill = units * 7
    category = "Medium"
#high category
else:
    bill = units * 10
    category = "High"

print("Units Consumed =", units)
print("Total Bill = ₹", bill)
print("Category =", category)
