num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print(num, "is a Prime Number")
else:
    print("Factors:", end=" ")

    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")

    print()
    print(num, "is not a Prime Number")
