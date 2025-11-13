# DataFrame Plotting
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "category": ["Electronics", "Clothing", "Electronics", "Grocery", "Clothing"],
    "sales": [5000, 2000, 3000, 1500, 2500]
}

df = pd.DataFrame(data)

summary = df.groupby("category")["sales"].sum()

print(summary)

summary.plot(kind="bar")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Sales by Category")
plt.show()
