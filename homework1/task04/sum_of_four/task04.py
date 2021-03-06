"""
Classic task, a kind of walnut for you.

Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 <= N <= 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Return the amount of tuples where sum of elements is zero."""
    ab = []
    cd = []
    counter = 0
    for i in range(len(a)):
        for j in range(len(c)):
            ab.append(a[i] + b[j])
            cd.append(c[i] + d[j])
    for i in ab:
        for j in cd:
            if i == 0 - j:
                counter += 1
    return counter
