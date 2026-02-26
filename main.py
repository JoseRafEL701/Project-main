import sys
print("Welcome to calculator.py")

options=["Plus (0)","Subtract (1)","Exit (4)"]
for op in options:
    print(op)
try:
    option = int(input("Choose any operation: "))
    if option== 4:
        print("Closing program..")
        sys.exit()
    num1= float(input("Type any number: "))
    num2= float(input("Type another number: "))
    if option== 0:
        print(f"Plus: {num1 + num2}")
    elif option== 1:
        print(f"Subtract: {num1 - num2}")
except:
    print("Bye")