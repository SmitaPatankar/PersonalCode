# small
chunk_list = []
import pandas as pd
chunk_data = pd.read_csv("C:\REPOSITORIES\MyRepo\python\python_algorithm_questions\sample_data.csv", sep=",", chunksize=3)
for chunk in chunk_data:
    chunk_list.append(chunk[chunk.state == "maharashtra"])
result = pd.concat(chunk_list)
print(result)

# big
n = 0
import pandas as pd
chunk_data = pd.read_csv("C:\REPOSITORIES\MyRepo\python\python_algorithm_questions\sample_data.csv", sep=",", chunksize=3)
for chunk in chunk_data:
    need_data = chunk[chunk.state=="maharashtra"]
    if n == 0:
        need_data.to_csv("C:\REPOSITORIES\MyRepo\python\python_algorithm_questions\sample_data_filtered.csv", index=None)
        n+=1
    else:
        need_data.to_csv("C:\REPOSITORIES\MyRepo\python\python_algorithm_questions\sample_data_filtered.csv", index=None, mode="a", header=None)