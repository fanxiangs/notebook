#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def insert_sort(nums):
    """
    插入排序:
        构建有序数组，对未排序数据，从后向前扫描找到对应位置插入
    时间复杂度:
        O(n^2)
    @param nums: 无序数组
    @return: 升序数组
    >>> import random
    >>> nums = random.sample(range(-50, 50), 50)
    >>> insert_sort(nums) == sorted(nums)
    True
    >>> insert_sort([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2])
    True
    >>> insert_sort([])
    []
    """
    length = len(nums)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums


if __name__ == '__main__':
    import doctest

    doctest.testmod()
