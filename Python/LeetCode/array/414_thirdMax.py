#!usr/bin/env python
# -*- coding: UTF-8 -*-

"""
author: fan
time: 2021 03 28

给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

https://leetcode-cn.com/problems/third-maximum-number/
"""


class Solution:
    def thirdMax(self, nums: list) -> int:
        nums = list(set(nums))
        print(nums)
        if len(nums) <= 3:
            return max(nums)
        else:
            del nums[nums.index(max(nums))]
            del nums[nums.index(max(nums))]
            return max(nums)

    def thirdMax_1(self, nums):
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)

    def thirdMax_2(self, nums):
        nums = sorted(list(set(nums)))
        return nums[-1] if len(nums) <= 2 else nums[-3]


if __name__ == '__main__':
    s = Solution()
    # ls = [1, 2, 5, 6, 3, 4, 4]
    # ls = [3, 2, 1]
    ls = [1, 2]

    r = s.thirdMax(ls)
    print(r)
