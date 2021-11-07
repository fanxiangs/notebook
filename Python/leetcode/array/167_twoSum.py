#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Author: Xiang Fan
# Created Time: 4/11/2021

from typing import List

"""
双指针:
    时间复杂度：O(n)，其中 n 是数组的长度。两个指针移动的总次数最多为 n 次
    空间复杂度：O(1)
二分法:
    时间复杂度：O(nlogn)，其中 n 是数组的长度。需要遍历数组一次确定第一个数，时间复杂度是 O(n)，寻找第二个数使用二分查找，时间复杂度是 O(logn)，因此总时间复杂度是 (nlogn)
    空间复杂度：O(1)

"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total > target:
                high -= 1
            elif total < target:
                low += 1

    def twoSum_1(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            low = i + 1
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1


if __name__ == '__main__':
    numbers, target = [0, 0, 3, 4], 0
    r = Solution().twoSum_1(numbers, target)
    print(r)
