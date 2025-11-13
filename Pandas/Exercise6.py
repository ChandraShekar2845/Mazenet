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

