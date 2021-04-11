# theory
# more flexible and scalable than excel

# install
# pip install pandas

# import
import pandas as pd

# extra import
import re
import numpy as np

# extra settings
# pd.options.display.max_rows = None
# pd.options.display.max_columns = None

# read files/webpage as df
# df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
df = pd.read_csv("input.csv")
df = pd.read_excel("input.xlsx")  # sheet_name="xx"
df = pd.read_csv("input.txt", delimiter="\t")

# read file as df in chunks
for chunked_df in pd.read_csv("input.csv", chunksize=5):
    print(chunked_df)

# create df from scratch
my_df = pd.DataFrame(columns=["id", "name"])

# describe df
print(df.describe())
print(df.info())
print(df.index)
print(df.is_null())
print(df.index.names)

# display complete df
print(df)

# display complete df via iteration
for index, row in df.iterrows():
    print(index, row)

# display specific df rows
print(df.head(5))
print(df.tail(5))
print(df[0:5])
print(df.iloc[1])
print(df.iloc[1:4])
print(df.iloc[2, 1])
print(df.loc[df["Type 1"] == "Fire"])
print(df.loc[(df["Type 1"] == "Grass")&(df["Type 2"] == "Poison")])
print(df.loc[(df["Type 1"] == "Grass")|(df["Type 2"] == "Poison")])
print(df.loc[df["Name"].str.contains("Mega")])
print(df.loc[~df["Name"].str.contains("Mega")])
print(df.loc[df["Type 1"].str.contains("Fire|Grass", regex=True)])
print(df.loc[df["Name"].str.contains("^pi[a-z]$")])
print(df.loc[df["Type 1"].str.contains("fire|grass", regex=True, flags=re.I)])
print(df.loc["A"])
print(df.loc[["A", "B"]])

# group df rows
print(df.groupby(["Type 1", "Type 2"]).count())
print(df.groupby("Type 1").mean())
print(df.groupby("Type 1").sum())

# add rows to df
for i in range(3):
    my_df.loc[i] = pd.Series({"id": i, "name": "smita"})
print(my_df)
print(my_df.append(pd.Series({"id": 3, "name": "neha"}), ignore_index=True))

# print column names from df
print(df.columns)

# print specific columns from df
print(df["Name"])
print(df[["Name", "#"]])
cols = list(df.columns)
print(df[cols[0:4] + [cols[-1]] + cols[4:12]])

# functions of df columns
print(df["Name"].unique())
print(df["Name"].nunique())
print(df["Name"].value_counts())

# sort values in columns
print(df.sort_values("Name"))
print(df.sort_values("Name", ascending=False))
print(df.sort_values(["Type 1", "HP"], ascending=[1,0]))

# add new columns
df["Total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"]
print(df)
df["count"] = 1
print(df)
df["Total"] = df.iloc[:,4:10].sum(axis=1)
print(df)
my_df["surname"] = ['patankar','patankar','patankar']
print(my_df)

# modify column values
df.loc[df["Type 1"] == "Fire", "Legendary"] = "True"
print(df)
df.loc[df["Type 1"] == "Fire", ["Legendary", "Generation"]] = "Test"
print(df)
df.loc[df["Type 1"] == "Fire", ["Legendary", "Generation"]] = ["Test1","Test2"]
print(df)

# apply functions on columns
print(df["Name"].apply(len))

# delete columns
print(df.drop(columns=["Legendary"]))

# set index
print(my_df.set_index("id"))

# reset index
print(my_df.reset_index())

# drop index
print(my_df.reset_index(drop=True))
my_df.reset_index(drop=True, inplace=True)
print(my_df)

# write df to file
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)  # sheet_name="xx"
df.to_csv("output.txt", index=False, sep="\t")

# concatenate 2 dfs (vertical)
print(pd.concat((df, df)))

# merge 2 dfs (on column, horizontal)
print(pd.merge(df, df, on="Name"))  # how=inner, outer, right, left

# join 2 dfs (on index, horizontal)
print(pd.join(df, df))  # how=inner, outer, right, left

# create series from scratch
my_data = [10, 20, 30]
arr = np.array(my_data)
labels = ['a', 'b', 'c']
d = {'a': 10, 'b': 20, 'c': 30}

print(pd.Series(data=my_data))
print(pd.Series(data=my_data, index=labels))
print(pd.Series(arr))
print(pd.Series(arr, labels))
print(pd.Series(d))
print(pd.Series([sum,print,len]))  # holding references to builtin functions as data points

# create dataframe from scratch
data ={"Company": ["GOOG", "GOOG", "MSFT", "MSFT", "FB", "FB"],
       "Person": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Sarah"],
       "Sales": [200,120,340,124,243,350]}
d = {'A': [1,2,np.nan],
     'B': [5,np.nan, np.nan],
     'C': [1,2,3]}

print(pd.DataFrame(data))
print(pd.DataFrame(data, index=[2,3,4,5,6,7]))
print(pd.DataFrame(d))

# modify df with null values
print(df.dropna())
print(df.dropna(axis=1))
print(df.dropna(thresh=2))
print(df.fillna("fill value"))
print(df.drop('new', axis=1))
df.drop('new', axis=1, inplace=True)

# df operations
print(df > 0)
print(df[df>0])
print(df['W']>0)
print(df[df['W']>0])
print(df[(df['W'] > 0) & (df['Y'] > 1)])
