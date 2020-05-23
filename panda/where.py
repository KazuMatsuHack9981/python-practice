import pandas as pd


df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'])

# print(df.where(df['col1'] > 2))   NaN
pad = pd.DataFrame([[0, "00"]] * len(df), columns=df.columns, index=df.index)
print(df.where(df['col1'] > 2, pad))
