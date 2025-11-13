# Pandas Series Creation and Indexing
# Create a Series from a list of Celsius temperatures.
# Convert each to Fahrenheit using formula:
# F = (C × 9/5) + 32
# Store Fahrenheit values in another Series with the same index.
# Main idea: Series creation + mathematical conversion.

import pandas as pd

celsius = [25, 30, 28, 35, 32]
t_c = pd.Series(celsius)
print("Celsius Series:")
print(t_c)

# Convert to Fahrenheit
fahrenheit = []
for c in celsius:
    f = (c * 9/5) + 32
    fahrenheit.append(f)

t_f = pd.Series(fahrenheit, index=t_c.index)
print("\nFahrenheit Series:")
print(t_f)

# Output:
# C:\Users\chand\Mazenet\Pandas>python Exercise6.py
# Celsius Series:
# 0    25
# 1    30   
# 2    28
# 3    35
# 4    32
# dtype: int64
# Fahrenheit Series:
# 0    77.0
# 1    86.0
# 2    82.4
# 3    95.0
# 4    89.6
# dtype: float64



