# Stage 2: Calculator + result sign check

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

result = None  # To store valid computed result

if op == "+":
    result = num1 + num2

elif op == "-":
    result = num1 - num2

elif op == "*":
    result = num1 * num2

elif op == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2

else:
    print("Invalid operator! Please use +, -, *, /")

# Sign check only if result was computed successfully
if result is not None:
    print("Result =", result)

    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")
