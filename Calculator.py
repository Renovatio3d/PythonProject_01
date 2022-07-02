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
