sales=float(input("Enter sales:$"))
while sales<0:
    print("Invalid sales")
    sales=float(input("Enter sales:$ "))
if sales<1000:
    bonus=sales*0.1
    print("your bonus is",bonus)
elif sales>=1000:
    bonus=sales*0.15
    print("your bonus is",bonus)
