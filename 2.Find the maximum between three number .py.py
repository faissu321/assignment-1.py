a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b and a > c:
    print("Maximum is:", a)
elif b > c:
    print("Maximum is:", b)
else:
    print("Maximum is:", c)