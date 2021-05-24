"""
Redis is an opensource in memory data store.
It can be used as a database, cache store or message broker.
It supports data structures such as strings, hashes, lists, sets etc.

It can be installed as below.
- sudo apt-get update
- sudo apt-get install redis-server
OR (better)
- download redis tar - "wget (url)"
- unzip tar - "tar xzf (file)"
- install redis from source - "make"
- test - "make test"

It can be launched as below.
- "src/redis-server"

Its CLI can be accessed as below:
- launch command line - "src/redis-cli"
- we get connected to redis running on local host at port 6379
- we can set key value as: "set mykey myvalue"
- we can get a key's value as: "get mykey"
- we can get multiple key values as: "mget [key1, key2]"
- we can delete a key value pair as: "del key"
- we can delete multiple key value pairs as: "del key1 key2"
- we can see multiple keys as: "keys *"
- we can set key and its value in a hash store as: "hset hashtorename key value"
- we can get key's value from hashstore as: "hget hashtorename key"
- we can get multiple key's values from hashstore as: "hmget hashtorename [key, key2]"
- we can get complete hashstore keys and values as "hgetall hashstorename"
- we can delete a hashstore key value pair as: "hdel hashstorename key"
- we can delete multiple hashstore key value pairs as: "hdel hashstorename key1 key2"
- we can delete hashstore as "hdelete hashtorename"
"""

import redis
r = redis.Redis(host="localhost", password=None, port=6379)

r.set("key", "value")
r.get("key")
r.mget(["key"])
r.scan_iter("key_pattern")
r.delete("key")

r.hset("hashstorename", "key", "value")
r.hget("hashtorename", "key")
r.hmget("hashstorename", ["key"])
r.hgetall("hashstorename")
r.hdel("hashstorename", "key")
