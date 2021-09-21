import pandas as pd
import re

# load df from various sources
df = pd.read_csv("C://SMITA PERSONAL REPOSITORY//GITHUB CODE//PYTHON//PYTHON_PANDAS//sample.csv")  # csv
df = pd.read_excel("C://SMITA PERSONAL REPOSITORY//GITHUB CODE//PYTHON//PYTHON_PANDAS//sample.xlsx")  # excel
df = pd.read_csv("C://SMITA PERSONAL REPOSITORY//GITHUB CODE//PYTHON//PYTHON_PANDAS//sample.txt", delimiter="\t")  # txt

# view complete df or certain rows and/or columns
print(df)  # complete df
print(df.columns)  # column names
print(df["Name"])  # one column
print(df["Name"][0:5])  # one column and certain rows
print(df[["Name", "Type 1"]])  # multiple columns
print(df.iloc[1])  # one row by integer
print(df.iloc[1:4])  # multiple rows by slicing
print(df.head(3))  # multiple head rows
print(df.tail(3))  # multiple tail rows
print(df.iloc[2, 1])  # one row and column by integer
print(df.iloc[2:3, 1:2])  # many rows and columns by integer

# iterate through the rows
for index, row in df.iterrows():
    print(index, row)
    # print(index, row["Name"])

# get statistics for each column based on all rows
print(df.describe())

# sort rows
print(df.sort_values("Name", ascending=False))  # one col
print(df.sort_values(["Type 1", "HP"], ascending=[True, False]))  # multiple cols

# add column (aggregate function)
df["Total"] = df.iloc[:, 4:10].sum(axis=1)
print(df)

# drop column
df = df.drop(columns=["Total"])
print(df)

# rearrange columns
cols = df.columns
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df)

# modify data
df.loc[df["Type 1"] == "Fire", 'Legendary'] = True  # single column modification
print(df)
df.loc[df["Type 1"] == "Fire", ['Generation', 'Legendary']] = "test value"  # multiple column modification
print(df)

# save df to diff forms
df.to_csv("C://SMITA PERSONAL REPOSITORY//GITHUB CODE//.temp//dummy.csv", index=False)
df.to_excel("C://SMITA PERSONAL REPOSITORY//GITHUB CODE//.temp//dummy.xlsx", index=False)
df.to_csv("C://SMITA PERSONAL REPOSITORY//GITHUB CODE//.temp//dummy.txt", index=False, sep="\t")

# filter rows by conditions
print(df.loc[df["Type 1"] == "Fire"])  # single condition
print(df.loc[df["Name"].str.contains("Mega")])  # string condition
print(df.loc[df["Name"].str.contains("Fire|Grass", regex=True, flags=re.I)])  # string regex condition
print(df.loc[df["Name"].str.contains("^pi[a-z]*", regex=True, flags=re.I)])  # string regex condition
print(df.loc[~df["Name"].str.contains("Mega")])  # negative condition
print(df.loc[(df["Type 1"] == "Fire") & (df["Type 2"] == "Poison")])  # 2 conditions
print(df.loc[(df["Type 1"] == "Fire") | (df["Type 2"] == "Poison")])  # either conditions

# reset index (post filtering)
df.reset_index(drop=True, inplace=True)  # dont save old index as new column

# group by
print(df.groupby(["Type 1"]).mean())  # sum, # count  # single column
print(df.groupby(["Type 1", "Type 2"]).mean())  # sum, # count  # single column

# load in chunks
for df in pd.read_csv("C://SMITA PERSONAL REPOSITORY//GITHUB CODE//PYTHON//PYTHON_PANDAS//sample.csv", chunksize=5):
    print(df)

# new df (concat dfs)
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv("C://SMITA PERSONAL REPOSITORY//GITHUB CODE//PYTHON//PYTHON_PANDAS//sample.csv", chunksize=5):
    results = df.groupby(["Type 1"]).count()
    new_df = pd.concat([new_df, results])
print(new_df)
