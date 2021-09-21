class _Tigger:
    def __str__(self):
        return "I am the only one"

    def roar(self):
        return "grrrrr"


_instance = None


def Tigger():
    global _instance
    if not _instance:
        _instance = _Tigger()
    return _instance
