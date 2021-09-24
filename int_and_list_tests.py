import pytest


def test_list_1():
    try:
        assert [1, 2, 3][6]
    except IndexError:
        pass


def test_list_2():
    assert [3, 1, 2].drop_item()


@pytest.mark.parametrize("arr", [[1, 2, 3], [1, "2", 3], {1, 2, 3}])
def test_list_3(arr):
    try:
        assert all(1 if type(i) == int else 0 for i in arr)
    except AssertionError:
        pass
    except TypeError:
        pass


def test_int_1():
    try:
        assert 5 + "123"
    except TypeError:
        pass


def test_int_2():
    assert 8 + 1.9 == int


@pytest.mark.parametrize("a,b", [(3, 8), (1, 0), ("3", 4), (1.0, 4.5)])
def test_int_3(a, b):
    try:
        assert type(-b / a) == int
    except TypeError:
        pass
    except AssertionError:
        pass



