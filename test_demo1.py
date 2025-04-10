import pytest

def test_forthProgram():
    msg = "Hello"
    assert msg == "Hello", "Test failed because msg is not equal to Hello"

@pytest.mark.Learning
def test_fifthProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because msg is not equal to Hello"