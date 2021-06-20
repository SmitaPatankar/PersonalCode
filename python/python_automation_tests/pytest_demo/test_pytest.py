# installation-------------------->
# pip install pytest
# pip install pytest-xdist (for parallel execution)
# pip install pytest-html (for reporting)

# help-------------------->
# pytest -h

# constraints-------------------->
# test file name must begin with test_ for pytest command without test file name to detect it
# test method name must begin with test_ for tes methods to be detected in general

# run all tests in a file-------------------->
# pytest test_pytest.py

# run specific test in a file-------------------->
# pytest test_pytest.py::test_add_int

# run all tests in a dir-------------------->
# pytest

# run in verbose mode-------------------->
# pytest -v

# run tests with specific pattern(s) in name-------------------->
# pytest -k add
# pytest -k "add or product"
# pytest -k "add and int"

# run tests with specific marker(s) in decorator-------------------->
# pytest -m "number"

# exit on first failed test-------------------->
# pytest -x

# exit on nth failed test-------------------->
# pytest --maxfail=2

# skip stack trace-------------------->
# pytest --tb=no

# show print statements-------------------->
# pytest -s
# pytest --capture=no

# run in quiet mode-------------------->
# pytest -q

# run tests parallelly-------------------->
# pytest -n 9  # number of cpus
# pytest -n auto

# generate html report-------------------->
# pytest --html=results.html

# run easily from pycharm-------------------->
# file - settings - project - interpreter - + - pytest
# file - settings - tools - python integrated tools - default test runner = pytest
# right click on file and run all tests
# run individual test from results or by right clicking inside file
# edit run configurations from top - additional arguments - -v -s

# markers (skip, skipif, parametrize, xyz)
# asserts (==, in, is)
# setup_module and teardown_module methods (better to use fixtures)
# fixtures
# mock.patch
# below

# customizing constraints
# pytest.ini

# sharing fixtures across files
# conftest.py

import pytest
import sys
from python.python_automation_tests.pytest_demo import dev
from python.python_automation_tests.pytest_demo.dev import StudentDB
from unittest import mock


@pytest.mark.skip(reason="this is a dummy test")
def test_dummy_one():
    pass


@pytest.mark.skipif(sys.version < "4.0", reason="needs higher python version")
def test_dummy_two():
    pass


@pytest.mark.parametrize("x,y,result", [
    (7, 3, 10),
    (2, 3, 5)
])
@pytest.mark.number
def test_add_int(x, y, result):
    assert dev.add(x, y) == result


@pytest.mark.number
def test_product_int():
    assert dev.product(5, 5) > 20


@pytest.mark.letter
def test_add_str():
    result = dev.add("hello", "world")
    assert type(result) is str


@pytest.mark.letter
def test_product_str():
    print("###############")
    assert "****" in dev.product("*", 5)


######################################################


# db = None
# def setup_module():
#     print("-----------setup method-----------")
#     global db
#     db = StudentDB()
#     db.connect("dev.json")
#
#
# def teardown_module():
#     print("-----------teardown method-----------")
#     db.close()

@pytest.fixture(scope="module")
def db():
    print("----------setup fixture---------------")
    db = StudentDB()
    db.connect("dev.json")
    yield db
    print("----------teardown fixture---------------")
    db.close()


def test_scott_data(db):
    scott_data = db.get_data("Scott")
    assert scott_data["id"] == 1


def test_mark_data(db):
    scott_data = db.get_data("Mark")
    assert scott_data["result"] == "fail"

########################################


def test_dummy(myfixture):
    assert myfixture == 1

########################################


# autospec ensures the function that was mocked has proper arguments i.e. is close to real use
@mock.patch("python.python_automation_tests.pytest_demo.dev.randint", return_value=2, autospec=True)
def test_add_to_random_int(mock_randint):
    assert dev.add_to_random_int(1, 10, 5) == 7
    mock_randint.assert_called_once_with(1, 10)
