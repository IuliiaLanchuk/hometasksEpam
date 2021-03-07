from project4.task4 import cache, function, multiply, operations

cache_function = cache(function)
cache_multiply = cache(multiply)
cache_operations = cache(operations)

some = 2, 4
val_1 = cache_function(*some)
val_4 = cache_function(*some)

val_2 = cache_multiply(*some)
val_5 = cache_multiply(*some)

val_3 = cache_operations(*some)
val_6 = cache_operations(*some)


def test_func():
    assert val_1 is val_4


def test_multiply():
    assert val_2 is val_5


def test_sum():
    assert val_3 is val_6
