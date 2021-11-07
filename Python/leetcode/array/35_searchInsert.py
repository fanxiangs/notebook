#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Author: Xiang Fan
# Created Time: 4/11/2021

from typing import List

"""
searchInsert_2: 二分查找
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0]:
                return 0
            elif target > nums[-1]:
                return len(nums)
            else:
                for i in range(1, len(nums)):
                    if nums[i - 1] < target < nums[i]:
                        return i

    def searchInsert_1(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        return nums.index(target)

    def searchInsert_2(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return left


if __name__ == '__main__':
    # nums, target = [1, 3, 5, 6], 5
    nums, target = [1, 3, 5, 6], 7
    r = Solution().searchInsert(nums, target)
    print(r)
