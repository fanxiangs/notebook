#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author: fan
# time: 04/03/2021

class Solution:
    def findErrorNums(self, nums: list) -> list:
        n1 = sum(nums) - sum(set(nums))  # 找出重复的数字
        n2 = sum(range(len(nums) + 1)) - sum(set(nums))  # 找出缺失的数字
        return [n1, n2]


if __name__ == '__main__':
    nums = [5, 3, 6, 1, 5, 4, 7, 8]
    s = Solution()
    r = s.findErrorNums(nums)
    print(r)
