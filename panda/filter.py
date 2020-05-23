import pandas as pd


df = pd.DataFrame([[10,1], [20,2], [30,3], [40,4]], columns=['col1', 'col2'], index=['a', 'b', 'c', 'd'])
print(df)
print()


# bool filter
f = [True, False, True, False]
print(df[f])
print()

# 完全一致
print(df[df.col1 == 20])
print()

# 不等式
print(df[df.col1 > 20])
print()

# 正規表現
df.col1 = ["aa", "bb", "cc", "dd"]
print(df)
f = df.col1.str.contains('.*c')
print(df[f])
