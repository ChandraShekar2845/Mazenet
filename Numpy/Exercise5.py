# NumPy Array Manipulation
import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)
print("Matrix:\n", matrix)

diag = np.diag(matrix)
print("Diagonal elements:", diag)

total = np.sum(diag)
print("Sum of diagonal:", total)
