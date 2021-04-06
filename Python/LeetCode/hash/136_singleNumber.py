#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author: fan
# time: 04/06/2021
from functools import reduce
from typing import List


class Solution:
    """
    位运算：
        任何数和0异或，仍为本身：a⊕0 = a
        任何数和本身异或，为0：a⊕a = 0
        异或运算满足交换律和结合律：a⊕b⊕a = (a⊕a)⊕b = 0⊕b = b
    reduce：先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
    """

    def singleNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            sum = i ^ sum
        return sum

    def singleNumber_1(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    r = Solution().singleNumber_1(nums)
    print(r)
