# instantiate class only once
# eg: load db data
# factory class

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    # not right - called multiple times
    def __init__(self):
        print("loading db")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
