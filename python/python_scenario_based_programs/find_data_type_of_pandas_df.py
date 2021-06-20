import pandas as pd

d = {"a": [1,2], "b": [3,4]}
df = pd.DataFrame(data=d, columns=["a", "b"])
print(df.dtypes)

# shows column data type
# bool --> bool
# int --> int64
# datetime --> datetime64  # object when taken from csv
# float or float+int --> float64
# string or string + anything --> object