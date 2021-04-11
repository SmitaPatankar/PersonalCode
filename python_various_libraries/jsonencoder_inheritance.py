import json


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


print(json.dumps({1, 2, 3, 4, 5}, cls=SetEncoder))
# [1, 2, 3, 4, 5]
