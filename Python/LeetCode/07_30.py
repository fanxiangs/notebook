# -*- coding: UTF-8 -*-
"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
示例 1:
    输入: 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:
    输入: 10
    输出: 36
    解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
    说明: 你可以假设 n 不小于 2 且不大于 58。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        s = n // 3
        y = n % 3
        if n == 2:
            return 1
        if n == 3:
            return 2
        if y == 1:
            res = 3 ** (s - 1) * 4
        elif y == 0:
            res = 3 ** s
        else:
            res = 3 ** s * y
        return res

    def integerBreak1(self, n):
        s, y = n // 3, n % 3
        if n < 3:
            return n - 1
        if y == 0:
            return 3 ** s
        if y == 1:
            return 3 ** (s - 1) * 4
        return 3 ** s * y

    def integerBreak2(self, n):
        """动态规划"""
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
                print(dp)
        print(dp[n])
        print(dp)
        return dp[n]


if __name__ == '__main__':
    n = 3
    s = Solution()
    s.integerBreak2(n)
