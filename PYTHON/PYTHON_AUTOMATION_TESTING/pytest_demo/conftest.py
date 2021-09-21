import pytest


@pytest.fixture(scope="session")
def myfixture():
    print("-----myfixture------------")
    yield 1
    pass
