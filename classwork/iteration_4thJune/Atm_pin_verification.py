valid_pin = 1234
while (valid_pin):
    pin = int(input("Enter PIN: "))

    if pin == valid_pin:
        print("Access Granted.")
        break
    else:
        print("Incorrect PIN. Try Again.")
