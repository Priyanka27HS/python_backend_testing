import pytest


@pytest.mark.regression
def test11():
    print("hello1")

@pytest.mark.regression
def test22():
    print("hello2")

    @pytest.mark.sanity
    def test223():
        print("hello3")