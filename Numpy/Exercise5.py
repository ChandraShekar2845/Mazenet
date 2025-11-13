# NumPy Array Manipulation
# Create a 5×5 matrix with numbers 1 to 25 using NumPy.
# Extract the diagonal values.
# Add them together.
# Main idea: Matrix creation + diagonal extraction + summation.

import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)
print("Matrix:\n", matrix)

diag = np.diag(matrix)
print("Diagonal elements:", diag)

total = np.sum(diag)
print("Sum of diagonal:", total)

# Output:
# C:\Users\chand\Mazenet\Numpy>python Exercise5.py
# Matrix:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]
# Diagonal elements: [ 1  7 13 19 25]
# Sum of diagonal: 65

