'''Write a program that acts as a simple calculator. It should take two
numbers and an operator (+, -, *, /) as input and print the result.'''

num1 = float(input("Enter the first number: "))


num2 = float(input("Enter the second number: "))


operator = input("Enter an operator (+, -, *, /): ")


if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."


print("Result:", result)
