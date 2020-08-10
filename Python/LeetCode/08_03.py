# -*- coding: UTF-8 -*-
"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
注意：
    num1 和num2 的长度都小于 5100.
    num1 和num2 都只包含数字 0-9.
    num1 和num2 都不包含任何前导零。
    你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            temp = n1 + n2 + carry
            carry = temp // 10
            res = str(temp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res

    def addStrings_1(self, num1: str, num2: str) -> str:
        str_map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
        ord_0 = 48
        i, j, temp = len(num1) - 1, len(num2) - 1, 1
        r1, r2 = 0, 0
        while i >= 0 or j >= 0:
            n1 = ord(num1[i]) - ord_0
            n2 = ord(num1[i]) - ord_0
            r1 = r1 + n1 * 10 ** i
            r2 = r2 + n2 * 10 ** i
            r = r1 + r2
            i, j, temp = i - 1, j - 1, temp + 1
        return str(r)


if __name__ == '__main__':
    s = Solution()
    r = s.addStrings_1(num1='123', num2='123')
    print(r)
