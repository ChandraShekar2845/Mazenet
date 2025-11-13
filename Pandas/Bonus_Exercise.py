# Combined Data Structures and Pandas
import pandas as pd

students = {
    "Chandhu": [85, 90, 92],
    "Shiva": [70, 75, 80],
    "Ram": [88, 85, 91]
}

df = pd.DataFrame(students).T   # transpose to make names as rows
df.columns = ["Test1", "Test2", "Test3"]

df["Average"] = df.mean(axis=1)

print(df)
