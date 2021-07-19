from unittest import TestLoader, TestSuite, TextTestRunner, load_tests
import test_demo
from test_demo import MyTest

loader = TestLoader()
suite = TestSuite(
    [loader.loadTestsFromModule(test_demo),
    loader.loadTestsFromTestCase(MyTest)]
)
runner = TextTestRunner(verbosity=2)
runner.run(suite)
