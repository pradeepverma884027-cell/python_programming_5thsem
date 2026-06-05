# Accept number from user
num = input("Enter a number: ")

# Start from the first digit
i = 0

# Move while digits are increasing
while i < len(num) - 1 and num[i] < num[i + 1]:
    i += 1

# Peak cannot be the first or last digit
if i == 0 or i == len(num) - 1:
    print("Not a Mountain Number")

else:
    # Move while digits are decreasing
    while i < len(num) - 1 and num[i] > num[i + 1]:
        i += 1

    # If we reached the last digit, it's a mountain
    if i == len(num) - 1:
        print("Mountain Number")
    else:
        print("Not a Mountain Number")
