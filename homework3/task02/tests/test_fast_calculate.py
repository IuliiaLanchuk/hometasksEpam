from time import perf_counter

from homework3.task02.project2.task2 import fast_calculate


def test_fast_calculate():
    time_start = perf_counter()
    sum_result = fast_calculate()
    time_end = perf_counter()

    assert time_end - time_start < 60
    assert sum_result == 1025932
