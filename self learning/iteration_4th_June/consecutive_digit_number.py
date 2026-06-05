# Accept a number from the user
num = int(input("Enter a number: "))

# Assume the number is consecutive
is_consecutive = True

# Check each digit with the previous digit
for i in range(1, len(num)):
    
    # Current digit should be exactly 1 greater than previous digit
    if int(num[i]) != int(num[i - 1]) + 1:
        is_consecutive = False
        break

# Displaying result
if is_consecutive:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")
