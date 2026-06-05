# Take the secret code as input from the user
code = input("Enter a 6-digit code: ")

# Check if the code has exactly 6 digits and contains only numbers
if len(code) == 6 and code.isdigit():

    # Calculate the sum of the first 3 digits
    first_sum = int(code[0]) + int(code[1]) + int(code[2])

    # Calculate the sum of the last 3 digits
    last_sum = int(code[3]) + int(code[4]) + int(code[5])

    # Compare both sums
    if first_sum == last_sum:
        print("Valid Code")    # Code is valid
    else:
        print("Invalid Code")  # Sums are not equal

# If the input is not exactly 6 digits
else:
    print("Invalid Code")
