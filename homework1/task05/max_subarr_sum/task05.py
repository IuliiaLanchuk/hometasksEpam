"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
import sys
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Return max subarray sum, where k is the length of subarray.

    :param nums: input list of integers, k: input int
    :return: int
    """
    max_sum = -sys.maxsize
    for i in range(len(nums) - k + 1):
        summ = sum(nums[i : i + k])
        if summ > max_sum:
            max_sum = summ
    return max_sum
