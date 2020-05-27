import pandas as pd

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'], index=['a', 'b', 'c', 'd'])
s = pd.Series([1, 1, 1, 1], index=['a', 'b', 'c', 'd'])

print(df)
print()


# new column
df["col3"] = s
print(df)
print()


# new index
df2 = pd.DataFrame([[9, 99, 1]], columns=['col1', 'col2', 'col3'], index=['x'])
df = df.append(df2)
print(df)
print()


# remove index
df = df.drop('a')
print(df)
print()


# remove column
df = df.drop("col3", axis=1)
print(df)
print()


# change one
df.at['x', 'col2'] = 90
print(df)
print()
