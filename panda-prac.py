import pandas as pd


# s = pd.Series([1,2,3], index=['a', "b", "c"])
s = pd.Series({'a':1, 'b':2, 'c':3})
# print(s)
# print((s+1)>2)


# df = pd.DataFrame([[1,10], [2,20], [3,30]])
data  = [[1,10], [2,20], [3,30]]
index = ['a', 'b', 'c']
col   = ['col1', 'col2']
df    = pd.DataFrame(data, index=index, columns=col)
# print(df)

s1 = pd.Series([2,3,4])
s2 = pd.Series([5,6,7])
df = pd.DataFrame({'col1':s1, 'col2':s2})
print(df)
# print(df.describe())
# print("ave of col2 is :",df.mean().col2)
# print(df.col2[2])
# print(df[1:3])
# print(df.loc[0])
print(df.at[0, "col1"])
