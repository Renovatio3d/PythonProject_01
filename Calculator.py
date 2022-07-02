import math

print("""
1. Addition
2. Subtraction
3. Multiplication 
4. Division 
5. Exponent 
6. Calculate BMI
7. Calculate the area of triangle 
8. Calculate the area of square
9. Finding the square root

 For exit enter 0
 
""")

Operation = int(input(" Please choose operation you want to do: "))
if Operation == 1:
    Number_1 = int(input("Please enter first number: "))
    Number_2 = int(input("Please enter second number: "))

    print("Result: ", Number_1 + Number_2)

elif Operation == 2:
    Number_1 = int(input("Please enter first number: "))
    Number_2 = int(input("Please enter second number: "))

    print("Result: ", Number_1 - Number_2)

elif Operation == 3:
    Number_1 = int(input("Please enter first number: "))
    Number_2 = int(input("Please enter second number: "))

    print("Result: ", Number_1 * Number_2)

elif Operation == 4:
    Number_1 = int(input("Please enter first number: "))
    Number_2 = int(input("Please enter second number: "))

    print("Result: ", Number_1 / Number_2)

elif Operation == 5:
    Number_1 = int(input("Please enter a number: "))

    print("Result: ", Number_1 ** 2)

elif Operation == 6:
    Weight = int(input("Please enter Weight: "))
    Height = int(input("Please enter Height: "))

    print("Result: ", Weight / (Height ** 2))

elif Operation == 7:
    Base = int(input("Please enter the base: "))
    Height = int(input("Please enter the height: "))

    print("Result: ", Base / (Height ** 2))

elif Operation == 8:
    Side = int(input("Please enter the side: "))

    print("Result: ", Side ** 2)

elif Operation == 9:
    Number = int(input("Please enter a number: "))

    print("Result: ", Number ** 0.5)

elif Operation == 0:
    print("Program is shutting down....")

else:
    print("Invalid operation..")
