#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author: fan
# time: 04/06/2021


from typing import List


class Solution:
    """
    双指针
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    r = Solution().removeDuplicates(nums)
    print(r)
