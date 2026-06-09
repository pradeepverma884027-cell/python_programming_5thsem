''' Vehicle Number Plate Verification 
Problem Statement 
A vehicle number plate is entered: 
MH12AB4589 
Tasks 
Write a program to: 
1. Extract state code.  
2. Extract district code.  
3. Extract vehicle series.  
4. Extract vehicle number.  
5. Count letters and digits separately.  
6. Verify:  
o First 2 characters must be alphabets.  
o Next 2 must be digits.  
o Next 2 must be alphabets.  
o Last 4 must be digits.  
7. Display whether the number plate is valid.  
'''
# storing vehicle number plate
vehicle_number = "MH12AB4589"

#--------------------------------------------------
# Task-1 : Extract state code

print("State Code :",vehicle_number[:2] )

#--------------------------------------------------
# Task-2 : Extract district code
print("District Code :", vehicle_number[2:4])

#--------------------------------------------------
# Task-3 : Extract vehicle series

print("Series :",vehicle_number[4:6])

#--------------------------------------------------
# Task-4 : Extract vehicle number

print("Vehicle Number :", vehicle_number[6:])

#--------------------------------------------------
# Task-5 : Count letters and digits separately

letter_count = 0
digit_count = 0

# traverse vehicle number plate
for ch in vehicle_number:

    # count alphabets
    if ch.isalpha():
        letter_count += 1

    # count digits
    elif ch.isdigit():
        digit_count += 1

print("\nTotal Letters :", letter_count)
print("Total Digits :", digit_count)

#--------------------------------------------------
# Task-6 : Verify vehicle number plate format

is_valid = (
    vehicle_number[:2].isalpha() and      # state code
    vehicle_number[2:4].isdigit() and     # district code
    vehicle_number[4:6].isalpha() and     # series
    vehicle_number[6:].isdigit() and      # vehicle number
    len(vehicle_number[6:]) == 4          # exactly 4 digits
)

#--------------------------------------------------
# Task-7 : Display validity status

if is_valid:
    print("\nVehicle Number Status : Valid")
else:
    print("\nVehicle Number Status : Invalid")

#--------------------------------------------------

'''
Output:

State Code : MH
District Code : 12
Series : AB
Vehicle Number : 4589

Total Letters : 4
Total Digits : 6

Vehicle Number Status : Valid
'''



