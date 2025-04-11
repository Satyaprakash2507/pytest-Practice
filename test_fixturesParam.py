import pytest


def test_crossBrowser(crossBrowser): #will be executed 3 times, once for each browser
    print("Test case is executed")
    print(crossBrowser) #ist crome is printed, then firefox is printed, then IE is printed


def test_crossBrowser1(crossBrowser1):
    print("Test case is executed")
    print(crossBrowser1)
    print(crossBrowser1[0])
    print(crossBrowser1[1])