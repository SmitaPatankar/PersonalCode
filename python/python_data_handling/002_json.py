# read big
# https://stackoverflow.com/a/17326199/10064174
import ijson
for prefix, type_, value in ijson.parse(open("C:/REPOSITORIES/MyRepo/python/python_big_files_handling_web_scraping/sample.json")):
    if prefix == "item" and type_ == "map_key":
        print(value, end=" >>>> ")
    elif type_ == "string":
        print(value)

# write big
# https://stackoverflow.com/a/65131145/10064174
# (complex version - https://stackoverflow.com/a/45143995/10064174)
import json
def get_chunk():
    for i in range(5):
        data = {'number': i}
        print(f"yielding {data}")
        yield data

with open("C:/REPOSITORIES/MyRepo/.trash/output2.json", "w") as f:
    f.write("[")
    i = 0
    for chunk in get_chunk():
        if i > 0:
            f.write(",")
        json.dump(chunk, f)
        i = i + 1
    f.write("]")
