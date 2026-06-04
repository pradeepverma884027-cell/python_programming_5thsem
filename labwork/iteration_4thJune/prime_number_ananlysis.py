#program to check if a number is prime or not. if not prime then display factors
num = int(input("Enter a number: "))

count = 0
#counting number of factors
for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1
# condition  for prime number
if count == 2:
    print(num, "is a Prime Number")
#condition for non-prime
else:
    print("Factors:", end=" ")
    #displaying factors of non-prime number
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")

    print()
    print(num, "is not a Prime Number")
