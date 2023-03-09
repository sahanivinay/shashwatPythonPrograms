# Defining the function named as _If_Else_Function
def _If_Else_Function(x,y,z):
    # If statement to compare the X values is greater than 10 or not
    if x > 10:
        # Finding the sum of Y and Z
        sum = y+z
        # Printing the sum of Y and Z
        print("Sum of Y and Z : ",sum)
    # Else statement
    else:
        # Finding the difference of Y and Z
        diff = y+z
        # Printing the difference of Y and Z
        print("Difference of Y and Z : ", diff)

# While loop for Infinite execution of program
while(1):
    # Taking input value of X
    X = int(input("Input the value of X : "))
    # Taking input value of Y
    Y = int(input("Input the value of Y : "))
    # Taking input value of Z
    Z = int(input("Input the value of Z : "))
    # Calling the function _If_Else_Function and passing arguments
    _If_Else_Function(X, Y, Z)
