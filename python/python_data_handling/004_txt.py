# read big
# https://stackoverflow.com/a/6475407/10064174
with open("C:/REPOSITORIES/MyRepo/PYTHON/python_big_files_handling_web_scraping/sample.txt") as f:
    for line in f:
        print(line, end="")

# write big
# https://stackoverflow.com/a/3168436/10064174
"""buffer is present by default but we can customize it"""
import time
with open("C:/REPOSITORIES/MyRepo/.trash/output.txt", "w", buffering=5) as f:
    count = 1
    while True:
        f.write(str(count)*1000)
        count += 1
        if count == 1000:
            break
        if count % 10 == 0:
            time.sleep(1)

# f.readline()
# f.tell() - shows where pointer is in file
# f.seek(0) - move pointer to a position
