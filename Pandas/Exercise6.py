# Pandas Series Creation and Indexing
import pandas as pd

celsius = [25, 30, 28, 35, 32]
t_c = pd.Series(celsius)
print("Celsius Series:")
print(t_c)

# Part B: Convert to Fahrenheit
fahrenheit = []
for c in celsius:
    f = (c * 9/5) + 32
    fahrenheit.append(f)

t_f = pd.Series(fahrenheit, index=t_c.index)
print("\nFahrenheit Series:")
print(t_f)

