# Input list
nums = [5, 8, 10, 12, 3, 4, 5, 6, 1]

# Current increasing sequence length
current_length = 1

# Maximum sequence length found so far
max_length = 1

# Compare each element with the next one
for i in range(len(nums) - 1):

    # Check if sequence is increasing
    if nums[i] < nums[i + 1]:
        current_length += 1

    else:
        # Update maximum length if needed
        if current_length > max_length:
            max_length = current_length

        # Reset current length
        current_length = 1

# Final check for a sequence ending at the last element
if current_length > max_length:
    max_length = current_length

print("Longest Sequence Length =", max_length)
