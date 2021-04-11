import json

d = {"a": "b"}
s = '{"a": "b"}'

dumped = json.dumps(d)
print(type(dumped))  # <class 'str'>

loaded = json.loads(s)
print(type(loaded))  # <class 'dict'>

with open("dummy.json", "w") as f:
    json.dump(d, f)

with open("dummy.json", "r") as f:
    print(type(json.load(f)))  # <class 'dict'>
