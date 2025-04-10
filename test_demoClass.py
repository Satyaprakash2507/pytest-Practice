import pytest

#instead of send the SETUP FIXTURE in each test case, we can use the fixture in the class and it will be available for all the test cases in the class
#there must be a file with name as conftest.py in the same folder as the test file, and the fixture should be in that file
@pytest.mark.usefixtures("setup") #this will use the setup fixture in the class and it will be available for all the test cases


#class and method/function  name must start with Test
class TestFixtureExample:
    def test_firstProgram(self):
        print("Hello, World! 1")

    def test_firstProgram1(self):
        print("Hello, World! 2")
        assert True
    def test_firstProgram2(self):
        print("Hello, World!3")
        assert True
    def test_firstProgram3(self):
        print("Hello, World! 4")
        assert True

    def test_firstProgram4(self):
        print("Hello, World! 5")
        assert True

    def test_firstProgram5(self):
        print("Hello, World! 6")
        assert True

    def test_firstProgram6(self):
       print("Hello, World! 7")
       assert True