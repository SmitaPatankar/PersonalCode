def collectstrings(obj):
    result = []
    for _, v in obj.items():
        if type(v) == str:
            result.append(v)
        elif type(v) == dict:
            result.extend(collectstrings(v))
    return result

obj = {
    "stuff": "foo",
    "data": {
        "val": {
            "thing": {
                "info": "bar",
                "moreinfo": {
                    "evenmoreinfo": {
                        "wemadeit": "baz"
                    }
                }
            }
        }
    }
}
print(collectstrings(obj))
