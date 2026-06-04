number= int(input("Enter the number :"))
n = number
digits = len(str(number))
sum_of_powers = 0

while number > 0:
    digit = number % 10
    sum_of_powers += digit ** digits
    number = number // 10

if sum_of_powers == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
