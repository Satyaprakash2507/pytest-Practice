#any  pytest file should start with test_ or end with .py
#pytest methos/function name should start with test_
#any code in the file should be in a function or class
#method name should have some meaning
# -k stand for method name execution, -s is for print the output on console, -v is for more info metadata


#python -m pytest test_demo.py will run all the test cases in the current directory
#python -m pytest will run all the test cases in the folder
#python -m pytest -k test_forthProgram will run the test case with the name test_forthProgram
#python -m pytest -k test_forthProgram -s will run the test case with the name test_forthProgram and print the output on console
#python -m pytest -k test_forthProgram -s -v will run the test case with the name test_forthProgram and print the output on console with more info metadata

#python -m pytest -m Learning -v  will run all the test cases in the folder with the name group Learnig

#can skip the test case using @pytest.mark.skip
#with @pytest.mark.xfail can mark the test case as skip but it will run and will not fail the test case
import pytest


@pytest.mark.Learning
def test_firstProgram(setup):
    print("Hello, World!")
    assert True
#as the assert in this is false therefore the test will fail
def test_secondProgram():
    print("Hello, World!")
    assert False

@pytest.mark.skip #skip the test case
def test_thirdProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because msg is not equal to Hello"