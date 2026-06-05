# Input the amount
amount = int(input("Enter the amount: "))

# Calculate number of ₹500 notes
notes_500 = amount // 500
amount = amount % 500

# Calculate number of ₹200 notes
notes_200 = amount // 200
amount = amount % 200

# Calculate number of ₹100 notes
notes_100 = amount // 100
amount = amount % 100

# Calculate number of ₹50 notes
notes_50 = amount // 50
amount = amount % 50

# Calculate number of ₹20 notes
notes_20 = amount // 20
amount = amount % 20

# Calculate number of ₹10 notes
notes_10 = amount // 10
amount = amount % 10

# Display the result
print("500 x", notes_500)
print("200 x", notes_200)
print("100 x", notes_100)
print("50 x", notes_50)
print("20 x", notes_20)
print("10 x", notes_10)
