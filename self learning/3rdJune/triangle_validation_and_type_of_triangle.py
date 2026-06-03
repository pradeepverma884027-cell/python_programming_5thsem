a=float(input("enter side a"))
if(a<=0):
    exit("side cannot be negative")
b= float(input("enter side b"))
if(b<=0):
    exit("side cannot be negative")
c=float(input("enter side c"))
if(c<=0):
    exit("side cannot be negative")

if (b+c>a and c+a>b and a+b>c):
    if (a!=b!=c):
        print("Scalene Triangle")
    elif a==b and b==c and c==a  :
        print("Equilateral Triangle")
    else:
        print("Isoscales Triangle")
