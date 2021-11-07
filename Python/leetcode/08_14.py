# -*- coding: UTF-8 -*-
"""
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
https://leetcode.com/problems/two-sum
"""


class Solution(object):
    def twoSum(self, nums, target):
        lt = []
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums:
                lt.append(i)
        return lt

    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                # 为什么先后顺序是 lookup[target - num], i
                # 因为当前是i，而差值只能从 lookup 中找，而 lookup 是在 i 之前面入库的
                # 所以 顺序是 lookup[target - num], i
                return [lookup[target - num], i]
            lookup[num] = i
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15, 2]
    target = 9
    so = Solution()
    n = so.twoSum_1(nums, target)
    print("结果: ", n)
