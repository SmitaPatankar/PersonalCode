import json
registry = {}

def register_class(target_class):
    registry[target_class.__name__] = target_class

class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args,
        })
    def __repr__(self):
        pass  # ...

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls
class RegisteredSerializable(BetterSerializable,
                             metaclass=Meta):
    pass

class Vector3D(RegisteredSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x, y, z

def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])

v3 = Vector3D(10, -7, 3)
print('Before:    ', v3)
data = v3.serialize()
print('Serialized:', data)
print('After:     ', deserialize(data))

# Before:     Vector3D(10, -7, 3)
# Serialized: {"class": "Vector3D", "args": [10, -7, 3]}
# After:      Vector3D(10, -7, 3)