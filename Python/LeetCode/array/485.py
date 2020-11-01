# -*- coding: UTF-8 -*-

"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：
输入的数组只包含0 和1。
输入数组的长度是正整数，且不超过 10,000。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-consecutive-ones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        """
        用一个计数器 count 记录 1 的数量，另一个计数器 maxCount 记录当前最大的 1 的数量。
        当我们遇到 1 时，count 加一。
        当我们遇到 0 时：
        将 count 与 maxCount 比较，maxCoiunt 记录较大值。
        将 count 设为 0。
        返回 maxCount
        """
        count = maxCount = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
        return max(maxCount, count)

    def findMaxConsecutiveOnes_1(self, nums) -> int:
        """
        在 Python 中可以使用 map 和 join 来解决此问题。
        使用 splits 函数在 0 处分割将数组转换成字符串。
        在获取子串的最大长度就是最大连续 1 的长度。
        """
        s = map(str, nums)
        r = map(len, ''.join(s).split('0'))
        return max(r)
        # return max(map(len, ''.join(map(str, nums)).split('0')))


if __name__ == '__main__':
    s = Solution()
    l = [1, 1, 0, 1, 1, 1]
    r = s.findMaxConsecutiveOnes_1(l)
    print(r)
