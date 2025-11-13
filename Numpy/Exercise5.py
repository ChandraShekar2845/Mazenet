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
