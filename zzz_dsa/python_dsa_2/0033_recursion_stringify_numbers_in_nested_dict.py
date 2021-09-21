def stringify(obj):
    for k,v in obj.items():
        if type(v) is int:
            obj[k] = str(v)
        elif type(v) is dict:
            stringify(v)

obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}

stringify(obj)
print(obj)
