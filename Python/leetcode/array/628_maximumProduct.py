#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author: Xiang Fan
# Created Time: 4/1/2021
"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6
Example 2:
Input: nums = [-1,-2,-3]
Output: -6
"""


class Solution:
    def maximumProduct(self, nums: list) -> int:
        """排序方法，时间复杂度O(nlog(n))"""
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

    def maximumProduct_1(self, nums: list):
        """遍历，时间复杂度O(nlog(n))"""
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        print(max1, max2, max3, min1, min2)
        return max(max1 * max2 * max3, max1 * min1 * min2)


if __name__ == '__main__':
    # nums = [1, 7, 2, 3, 3, 5, -1]
    # nums = [-100, -98, -1, 2, 3, 4]
    nums = [7, 3, 1, 0, 0, 6]

    s = Solution().maximumProduct_1(nums)
    print(s)
