#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Author: Xiang Fan
# Created Time: 4/7/2021

from typing import List


class Solution:
    """双指针"""
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    r = Solution().removeElement(nums, val)
    print(r)
