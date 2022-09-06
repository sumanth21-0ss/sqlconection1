import pytest
def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput",["abc",12])


def test_alphab(stringinput):
    assert stringinput.isalpha()


def test_numer(stringinput):
    assert type(stringinput)==int