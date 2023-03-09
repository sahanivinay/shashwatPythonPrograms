# Taking user input for the rows of the matrix
row = int(input("Enter the number of rows:"))
# Taking user input for the columns of the matrix
column = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input a for loop for row entries
for i in range(row):
    a = []
    # A for loop for column entries
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)
print("Matrix Data")
# For printing the matrix
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")
    print()