from source.easy_check import c_fib


def test_f1():

    assert c_fib(6) == 8


def test_f2():

    assert c_fib(1) == 1


def test_f3():

    assert c_fib(3) == 2