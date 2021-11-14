#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: fan
# time: 11/14/2021
from typing import List


def bubble_sort(nums: List[int]):
    """
    冒泡排序:
        比较相邻的元素，如果第一个比第二个大(升序)，就交换位置。
    时间复杂度: O(n2)
    @param nums: 无序数组
    @return: 升序数组
    >>> import random
    >>> nums = random.sample(range(-50, 50), 50)
    >>> bubble_sort(nums) == sorted(nums)
    [...]
    True
    >>> bubble_sort([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2])
    [...]
    True
    """
    length = len(nums)
    for i in range(length - 1):
        for j in range(i, length):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    print(nums)
    return nums


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
