import pytest

@pytest.fixture()
def setup():
    print("Setup method is called")
    yield
    print("Teardown method is called. it will be printed at the end of the test case")

def test_fixtureDemo1(setup):
    print("Test case 1 is executed, it will be printed after setup method")