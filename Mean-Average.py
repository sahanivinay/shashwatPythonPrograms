# Defining the function and parameter
def avgOfNumber(num1,num2):
    # Calculating average
    avg = (num1+num2)/2
    # Print the average of two
    print("Average of Two Numbers",avg)

# While loop for Infinite execution of program
while(1):
    # Input the number 1
    first = float(input("Input Number 1: "))
    # Input the number 2
    second = float(input("Input Number 2: "))
    # Calling the function avgOfNumber and passing the argument
    avgOfNumber(first, second)