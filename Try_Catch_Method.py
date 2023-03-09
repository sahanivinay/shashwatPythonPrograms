# While loop for iterative execution
while True:
    # Try method
    try:
        # Taking input from the user
        num1 = float(input("Enter the first number (between 0 and 10000): "))
        num2 = float(input("Enter the second number (between 0 and 10000): "))

        # If condition to raise error
        if num1 < 0 or num1 > 10000 or num2 < 0 or num2 > 10000:
            raise ValueError
        break
    # Except method to catch the error
    except ValueError:
        print("Please enter a valid number between 0 and 10000. ")
# Taking input for the mathematical operation
operation = input("Enter the mathematical operation you want to perform (+, -, *, /,**,%): ")
if operation == '+':                        # Addition operation
    result = num1 + num2
elif operation == '-':                      # Subtraction operation
    result = num1 - num2
elif operation == '*':                      # Multiplication operation
    result = num1 * num2
elif operation == '%':                      # Modulus operation
    result = num1 % num2
elif operation == '**':                     # Power operation
    result = num1 ** num2
elif operation == '/':                      # Division operation
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")
else:
    print("Invalid operation. Please enter +, -, *, or /.")

if operation != '/':
    print(f"{num1} {operation} {num2} ={result:.2f}")
