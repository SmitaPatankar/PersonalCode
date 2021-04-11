import splunklib.client as client
import splunklib.results as results
import io
import json

service = client.connect(host="splunk_host", port=8089, username="username", password="password", owner="splunk_app_owner", app="splunk_app_name", autologin=True)

#########
# query #
#########

jobs = service.jobs
splunk_query = "search index=xx sourcetype=xx xx"

# one shot search
kwargs_search = {"search_mode": "normal", "output_mode": "csv"}
splunk_query_results = jobs.export(splunk_query, **kwargs_search).read()

# paged search
kwargs_blockingsearch = {'exec_mode': 'blocking'}
job = jobs.create(splunk_query, **kwargs_blockingsearch)
offset = 0
count = 1000
while offset < int(job['resultCount']):
    kwargs_paginate = {'count': count, 'offset': offset}
    rs = job.results(**kwargs_paginate)
    reader = results.ResultsReader(io.BufferedReader(rs))
    for item in reader:
        print(item)
    offset += count

####################
# kv store connect #
####################

data = {"test": "test"}
collection = service.kvstore["kv_store_name"]
collection.data.insert(json.dumps(data))
collection.data.query(json.dumps({"_key": "foo"}))
collection.data.update("key", json.dumps(data))
collection.data.delete(json.dumps({"_key": "key"}))