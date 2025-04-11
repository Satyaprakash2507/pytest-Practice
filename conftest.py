#can write the Fixture in this file and this file will be available in all the test files in the folder
#the name of this file must be conftest.py only
#this file should be in the same folder as the test files
import pytest

@pytest.fixture(scope="class") #scope can be function, class, module, session
def setup():
    print("Setup method is called")
    yield
    print("Teardown method is called. it will be printed at the end of the test case")

@pytest.fixture()
def dataLoad():
    print("user profile data is getting created:")
    return ["Satya","Yadav","yadu.com"]


@pytest.fixture(params=["Chrome", "Firefox", "IE"]) #this will run the test case for all the browsers mentioned in the params, 3 times
def crossBrowser(request): #request is a built in fixture in pytest which is used to get the parameter passed in the fixture
    return request.param #this will return the parameter passed in the fixture, in this case it will return Chrome, Firefox, IE one by one



@pytest.fixture(params=[("Chrome","Satya","Yadav"), ("Firefox", "Prakash"), "IE"]) #passing multiple data to each browser
def crossBrowser1(request):
    return request.param