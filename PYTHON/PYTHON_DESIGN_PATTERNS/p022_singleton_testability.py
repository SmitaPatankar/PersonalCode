import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        print("reading file once")
        with open("C://SMITA PERSONAL REPOSITORY//GITHUB CODE//PYTHON//PYTHON_DESIGN_PATTERNS//p022_data.txt", "r") as f:
            lines = f.readlines()
            for i in range(0, len(lines), 2):
                self.population[lines[i].strip()] = lines[i+1].strip()


class ConfigurableRecordFinder:
    def __init__(self, db=Database()):
        self.db = db

    def total_population(self, cities):
        result = 0
        for city in cities:
            result += int(self.db.population[city])
        return result


class DummyDatabase:
    population = {
        "alpha": 100,
        "beta": 50,
        "gamma": 20
    }

    def get_population(self, name):
        return self.population[name]


class SingletonTests(unittest.TestCase):
    ddb = DummyDatabase()

    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        r = ConfigurableRecordFinder(self.ddb)
        pop = r.total_population(["alpha", "gamma"])
        self.assertEqual(pop, 120)
