"""
50 apis
run through each
record time taken

3 recordings

tabular format

5 apis
3 recordings

# output
api    time1   time2  time3  avg
first   1       1       8    8
sec     2       1       1    9
third   3       2       2    10
fourth  2       3       3    1
fifth   1       4       4    0

# like tdd
"""

import pandas
import requests
from datetime import datetime

def fetch_data(url, token):
    start = datetime.datetime.now()
    requests.get(url, headers={"X-Auth-Token": token}).status_code
    end = datetime.datetime.now()
    return end - start

def fetch_all_data(urls, token):
    time_taken_list = []
    for url in urls:
        time_taken = fetch_data(url, token)
        time_taken_list.append(time_taken)

def get_time_taken(urls, token):
    all_timings = []
    for _ in range(3):
        all_timings.append(fetch_all_data(urls, token))

def format_result(urls, timings):
    df = pandas.DataFrame({"api_url": urls, "timings_1": timings[0], "timings_2": timings[1], "timings_3": timings[2]})
    df["avg"] = df["timings_1"] + df["timings_2"] + df["timings_3"]
    return df

urls = ["url1", "url2", "url3", "url4", "url5"]
timings = get_time_taken(urls, "token")
print(format_result(urls, timings))

# urls = ["url1", "url2", "url3", "url4", "url5"]
# result = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
"""
api    time1   time2  time3  avg
first   1       1       8    8
sec     2       1       1    9
third   3       2       2    10
fourth  2       3       3    1
fifth   1       4       4    0
"""
