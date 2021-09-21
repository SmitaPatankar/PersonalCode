import pandas as pd

# read big
# https://stackoverflow.com/a/25962187/10064174
with pd.read_csv("C:/REPOSITORIES/MyRepo/PYTHON/python_big_files_handling_web_scraping/sample.csv", chunksize=2) as reader:
    for chunk in reader:
        print(chunk)


# write big
# https://stackoverflow.com/a/38531304/10064174
def get_chunk():
    yield pd.DataFrame({"a": [1,2], "b": [11,22], "c": [111,222]})
    yield pd.DataFrame({"a": [3,4], "b": [33,44], "c": [333,444]})
    yield pd.DataFrame({"a": [5], "b": [55], "c": [555]})


header = True
for chunk in get_chunk():
    chunk.to_csv("C:/REPOSITORIES/MyRepo/.trash/output.csv", mode="a", index=False,header=header)
    header=False