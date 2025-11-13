import pandas as pd
import numpy as np
 
data = [10, 20, 30, 40, 50]
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
 
data = {'x': 100, 'y': 200, 'z': 300}
s = pd.Series(data)
print(s)
 
arr = np.array([1, 2, 3, 4])
s = pd.Series(arr)
print(s)
 
s = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print(s[0])      # Access by position
print(s['b'])    # Access by label
print(s[0:2])    # Slice by position
 
s = pd.Series([10, 20, np.nan, 40], index=['a', 'b', 'c', 'd'])
 
print("Index:", s.index)
print("Values:", s.values)
print("Dtype:", s.dtype)
print("Shape:", s.shape)
print("Dimension:", s.ndim)
print("Size:", s.size)
print("Itemsize:", s.values.itemsize)
print("Total Bytes:", s.nbytes)
print("Is Empty:", s.empty)
print("Has NaNs:", s.hasnans)
 
s = pd.Series([10, 20, 30, 40, 50])
 
print("Sum:", s.sum())
print("Mean:", s.mean())
print("Max:", s.max())
print("Min:", s.min())
print("Describe:\n", s.describe())
print("Head(3):\n", s.head(3))
print("Tail(2):\n", s.tail(2))
 
data = {
    'Name': ['Aaryan', 'Riya', 'Sam'],
    'Age': [21, 22, 20],
    'Marks': [85, 90, 95]
}
df = pd.DataFrame(data)
df['English'] = [23, 34, 45]
del df['Marks']
df.drop('Marks', axis=1, inplace=True)
df.loc[len(df)] = ['Kirti', 34, 80, 89]
print(df)
print(df[df['Age'] > 20])
 
# Using dictionary of DataFrames
panel_dict = {
    'Item1': pd.DataFrame(np.random.randn(2, 2)),
    'Item2': pd.DataFrame(np.random.randn(2, 2))
}
 
# Access one frame
print(panel_dict['Item2'])
 
# loc -> labels
# iloc -> index position
 
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Aaryan', 'Riya', 'Sam']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Marks': [85, 90, 88]})
 
merged = pd.merge(df1, df2, on='ID', how='inner')
print(merged)
 
df1 = df1.set_index('ID')
df2 = df2.set_index('ID')
joined = df1.join(df2, how='outer')
# joined.fillna(value=0, inplace=True)
joined.dropna(inplace=True)
print(joined)
 
df1 = pd.DataFrame({'A': [1, np.nan, 3]})
df2 = pd.DataFrame({'A': [10, 20, 30]})
print(df1.combine_first(df2))
 
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
 
result = pd.concat([df1, df2], axis=0)
print(result)
 
dates = pd.date_range('2025-01-01', periods=5, freq='D')
print(dates)
 
date_str = ['2025-01-01', '2025-01-05', '2025-02-01']
dt_series = pd.to_datetime(date_str)
print(dt_series)
 
ts = pd.Series(np.random.randn(3), index=pd.date_range('2025-01-01', periods=3))
print("Original:\n", ts)
print("Shifted by 1 day:\n", ts.shift(1))
 
p = pd.Period('2025-01', freq='M')
print(p)
print(p - 3)  # 3 months ahead
 
df[df['English'] > 30]
print(df.sort_values(by='Maths', ascending=False))
group_df = df.groupby('Maths').sum()
print(group_df)
print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Std Deviation:\n", df.std())
print("Correlation:\n", df.corr())