import pandas as pd

data = {"a": [1,2,3], "b": [1,2,3]}

df1 = pd.DataFrame(data, columns=["a", "b"])
df2 = pd.DataFrame(data, columns=["a", "b"])

print(df1.equals(df2))