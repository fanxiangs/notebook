#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: fan
# time: 11/14/2021

def selection_sort(nums):
    """
    选择排序:
        依次选出最小元素
    时间复杂度:
        O(n^2)
    @param nums: 无序数组
    @return: 升序数组
    >>> import random
    >>> nums = random.sample(range(-50, 50), 50)
    >>> selection_sort(nums) == sorted(nums)
    True
    >>> selection_sort([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2])
    True
    >>> selection_sort([])
    []
    """
    length = len(nums)
    for i in range(0, length - 1):
        min_index = i
        for j in range(i + 1, length):
            if nums[min_index] > nums[j]:
                min_index = j
        if min_index != i:
            nums[min_index], nums[i] = nums[i], nums[min_index]
    return nums


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
