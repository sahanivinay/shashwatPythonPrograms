# Importing numpy module
import numpy as np

# Taking a 3x3 matrix
A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

# Taking a 3x3 matrix
B = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

# Result matrix will be 3x3

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
# Multiplying the matrix A with matrix B
result = np.dot(A, B)
print("Multiplication of matrix")
for mul in result:
    print(mul)

# Taking a 3x3 matrix
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
# Taking a 3x3 matrix
Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
# Addition of matrix X with matrix Y
result = np.array(X) + np.array(Y)

print("Addition of Matrix\n",result)