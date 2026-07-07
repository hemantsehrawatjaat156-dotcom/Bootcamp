import pandas as pd

data = { 'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10] }
df = pd.DataFrame(data)
s = pd.Series([1, 2, 3, 4, 5])
# print(df.add(s, axis=0))
# print(df.add(s, axis=1))
print(df.apply(lambda x: x*2))
print(df.applymap(lambda x: x*2))