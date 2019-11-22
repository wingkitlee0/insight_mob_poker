def test_add():
    assert add(1, 1) == 2

def test_add_2():
    assert add(1, 2) == 3

def test_multiply():
    assert multiply(1, 1) == 1


def add(x, y):
    return x+y

def multiply(x, y):
    return x * y