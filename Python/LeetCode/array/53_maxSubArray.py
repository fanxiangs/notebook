#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Author: Xiang Fan
# Created Time: 4/14/2021

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)

    def maxSubArray_1(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


if __name__ == '__main__':
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [5, 4, -1, 7, 8]
    r = Solution().maxSubArray_1(nums)
    print(r)
