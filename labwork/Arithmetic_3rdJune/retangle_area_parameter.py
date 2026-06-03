l=int(input("enter the length"))
if (l<0):
    exit("length cannot be negative")
b=int(input("enter the breadth"))
if(b<0):
    exit("breadth cannot be  negative")
else:
    print("area is :", l*b)
    print("perimeter is:", 2*(l+b))
