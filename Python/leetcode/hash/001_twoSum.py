#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author: fan
# time: 04/06/2021

from typing import List


class Solution:
    """
    way1:list
        判断(target - j)是否在在数组中，并返回index
    way2:hash
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in enumerate(nums):
            if target - j in nums[i + 1:]:
                return [i, nums[i + 1:].index(target - j) + i + 1]

    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


if __name__ == '__main__':
    nums = [2, 11, 15, 7]
    target = 9
    r = Solution().twoSum_1(nums, target)
    print(r)
