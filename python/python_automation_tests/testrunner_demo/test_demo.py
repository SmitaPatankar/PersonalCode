from unittest import TestCase
import unittest

class MyTest(unittest.TestCase):
    def test_mytest(self):
        assert 1 == 1

if __name__ == "__main__":
    unittest.main()
