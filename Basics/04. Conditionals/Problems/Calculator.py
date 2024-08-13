
# Arithmetic Calculator

num1 = float(input("Enter a First Number: "))
num2 = float(input("Enter a Second Number: "))
operator = input("Enter Operator ( +, -, *, /) ")

if operator == "+":
    print("Addition: " , num1 + num2)

elif  operator == "-":
    print("Subtraction: ", num1 - num2)

elif operator == "*":
    print("Multiplication: ", num1*num2)

elif operator == "/":
    if num2 != 0:
        print("Division: ", num1/num2)
    else:
        print("0 is not divisible. ")
