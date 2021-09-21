from collections import defaultdict
l = [-3, 0,-1,"smita", "neha", "smita", 0, 100, -1 ,-2]
d = defaultdict(int)
for i in l:
    d[i] = d[i] + 1
for k,v in d.items():
    if v > 1:
        print(k)