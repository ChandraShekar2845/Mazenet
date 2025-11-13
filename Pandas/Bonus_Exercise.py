# Combined Data Structures and Pandas
# You start with a dictionary containing student names and their test scores.
# Convert the dictionary into a DataFrame and transpose it so each student becomes a row.
# Rename the score columns for clarity.
# Calculate the average score for each student and add it as a new column.
# Print the final DataFrame showing all scores and averages.

import pandas as pd

students = {
    "Chandhu": [85, 90, 92],
    "Shiva": [70, 75, 80],
    "Ram": [88, 85, 91]
}

df = pd.DataFrame(students).T   
df.columns = ["Test1", "Test2", "Test3"]

df["Average"] = df.mean(axis=1)

print(df)
