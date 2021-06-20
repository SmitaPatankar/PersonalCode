# small
total = 0
with open("sample_data.csv", "r") as f:
    header = f.readline()
    while True:
        line = f.readline()
        if not line:
            break
        total += float(line.split(",")[4])
print(total)

# big
total = 0
import pandas as pd
chunk_data = pd.read_csv("C:\REPOSITORIES\MyRepo\python\python_algorithm_questions\sample_data.csv", sep=",", chunksize=3)
for chunk in chunk_data:
    total+=chunk["amount"].sum()
print(total)