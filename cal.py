print("""
Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide
""")

a = input(f"Enter choice(1/2/3/4):")
x = float(input(f"Enter first number:"))
y = float(input(f"Enter second number:"))

if a == "1":
    print(x,"+",y,"=",x+y)
elif a == "2":
    print(x,"-",y,"=",x-y)
elif a == "3":
    print(x,"*",y,"=",x*y)
elif a == "4":
        print(x,"/",y,"=",x/y)
else:
    print("invalid syantax")

