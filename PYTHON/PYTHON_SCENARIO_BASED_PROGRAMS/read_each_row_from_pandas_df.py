import pandas as pd

data = {"a": [1,2,3], "b": [4,5,6]}

df = pd.DataFrame(data)

for index, row in df.iterrows():
    print(f"{index}-->{row['a']}, {row['b']}")
