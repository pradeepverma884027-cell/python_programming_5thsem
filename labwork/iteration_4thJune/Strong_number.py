
#program to check a number is strong number or not
num = int(input("Enter a number: "))

n = num
factorial_sum = 0

while num > 0:
    #extracting last digit 
    digit = num % 10

    factorial = 1
    #calculating factorial
    for i in range(1, digit + 1):
        factorial *= i
    #calculating sum of factorial of digit
    factorial_sum += factorial
    num = num // 10
#checking strong condition 
if factorial_sum == n:
    print(n, "is a Strong Number")
else:
    print(n, "is not a Strong Number")
