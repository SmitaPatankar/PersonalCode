# read - big
# https://stackoverflow.com/a/16696317/10064174
import requests
with requests.get("https://jsonplaceholder.typicode.com/todos", stream=True) as r:
    r.raise_for_status()
    with open("C:/REPOSITORIES/MyRepo/.trash/output.txt", 'wb') as f:
        for chunk in r.iter_content(chunk_size=256):
            f.write(chunk)
