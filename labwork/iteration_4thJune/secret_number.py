import random
#secret number generator
secret_number = random.randint(1, 50)
#no. of attempts
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Correct Guess")
        print("Total Attempts:", attempts)
        break
