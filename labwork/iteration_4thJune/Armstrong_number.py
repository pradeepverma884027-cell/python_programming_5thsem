
#program to check a number is armstrong or not
number= int(input("Enter the number :"))
n = number
#finding number of digits 
digits = len(str(number))
sum_of_powers = 0

while number > 0:
    #extracting digits from the number
    digit = number % 10
    sum_of_powers += digit ** digits
    #number after last digit is removed
    number = number // 10
#chechikng armstrong condition
if sum_of_powers == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
