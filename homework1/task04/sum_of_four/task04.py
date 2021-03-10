"""
Classic task, a kind of walnut for you.

Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 <= N <= 1000.
"""
from collections import defaultdict
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Return the amount of tuples where sum of elements is zero."""
    ab_sums = defaultdict(int)
    counter = 0
    for i in a:
        for j in b:
            ab = -i - j
            ab_sums[ab] += 1

    for i in c:
        for j in d:
            cd = i + j
            if cd in ab_sums:
                counter += ab_sums[cd]
    return counter
