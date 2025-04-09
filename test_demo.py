#any  pytest file should start with test_ or end with .py
#pytest methos/function name should start with test_
#any code in the file should be in a function or class

def test_firstProgram():
    print("Hello, World!")
    assert True
#as the assert in this is false therefore the test will fail
def test_secondProgram():
    print("Hello, World!")
    assert False

def test_thirdProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because msg is not equal to Hello"