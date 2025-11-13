# Pandas DataFrame Filtering
# Create a DataFrame with employee salaries.
# Find the 75th percentile salary using .quantile(0.75).
# Filter employees who earn more than that amount.
# Main idea: Statistical filtering using percentile.

import pandas as pd

data = {
    "name": ["Ansh", "Bheem", "Chandhu", "Deva", "shiva"],
    "department": ["HR", "IT", "IT", "Finance", "HR"],
    "salary": [30000, 45000, 50000, 70000, 65000]
}

df = pd.DataFrame(data)

p75 = df["salary"].quantile(0.75)

result = df[df["salary"] > p75]

print(result)

# Output:
# C:\Users\chand\Mazenet\Pandas>python Exercise7.py
#   name department  salary
# 3  Deva    Finance   70000

