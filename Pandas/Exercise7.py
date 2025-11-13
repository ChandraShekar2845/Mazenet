# Pandas DataFrame Filtering
import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "department": ["HR", "IT", "IT", "Finance", "HR"],
    "salary": [30000, 45000, 50000, 70000, 65000]
}

df = pd.DataFrame(data)

p75 = df["salary"].quantile(0.75)

result = df[df["salary"] > p75]

print(result)
