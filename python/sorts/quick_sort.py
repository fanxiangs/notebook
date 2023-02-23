#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def quick_sort(nums):
    """
    快速排序:
        从数组中找出一个基准，把数组与基准比较分成大小两组，递归排序
    时间复杂度:
        O(n^2)
    @param nums: 无序数组
    @return: 升序数组
    >>> import random
    >>> nums = random.sample(range(-50, 50), 50)
    >>> quick_sort(nums) == sorted(nums)
    True
    >>> quick_sort([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2])
    True
    >>> quick_sort([])
    []
    """
    if len(nums) < 2:
        return nums
    # cur = nums.pop()
    cur = nums[0]
    low_list = []
    high_list = []
    for num in nums[1:]:
        (high_list if num > cur else low_list).append(num)
        # if num > cur:
        #     high_list.append(num)
        # else:
        #     low_list.append(num)
    return quick_sort(low_list) + [cur] + quick_sort(high_list)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
