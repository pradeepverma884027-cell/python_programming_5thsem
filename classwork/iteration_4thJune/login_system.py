corr_pass = "admin123"
while(corr_pass):
    password = str(input("Enter Password :"))
    if(password ==corr_pass):
        print("Access Granted")
        break
    else:
        print("Incorrect PIN. Try Again ")
