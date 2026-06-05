# Take the number as input
num = input("Enter a number: ")

# Find the length of the number
n = len(num)

# A mirror number must have an even number of digits
if n % 2 != 0:
    print("Not a Mirror Number")
else:
    # Assume the number is a mirror number initially
    mirror = True

    # Compare each digit in the left half
    # with the corresponding digit in the right half
    for i in range(n // 2):
        if num[i] != num[i + n // 2]:
            mirror = False  # Mismatch found
            break

    # Display the result
    if mirror:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")
