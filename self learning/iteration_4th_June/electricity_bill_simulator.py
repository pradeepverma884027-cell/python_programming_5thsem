# Accept the number of units consumed from the user
units = int(input("Enter the number of units: "))

# Calculate the bill based on unit slabs

# For 0 to 100 units, rate = ₹5 per unit
if units <= 100 and units >= 0:
    bill = units * 5

# For 101 to 200 units:
# First 100 units at ₹5/unit
# Remaining units at ₹7/unit
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

# For units above 200:
# First 100 units at ₹5/unit
# Next 100 units at ₹7/unit
# Remaining units at ₹10/unit
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Add 10% surcharge if bill exceeds ₹5000
if bill > 5000:
    surcharge = bill * 0.10
    bill += surcharge

# Display the final payable bill amount
print("Final Bill Amount = ₹", bill)
