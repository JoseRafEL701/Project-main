import sys
print("Welcome to calculator.py")

while True:
    options=["Plus (0)","Subtract (1)","Multiplication (2)","Division (3)","Exit (4)"]
    for op in options:
        print(op)
    try:
        option = int(input("Choose any operation: "))
        if option == 4:
            print("Closing program..")
            break
    except ZeroDivisionError:
        print("Cant handle zero division")
    except:
        print("Invalid input, returning to menu")
print("Program terminated.")