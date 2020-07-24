# -*- coding: UTF-8 -*-
"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
https://leetcode-cn.com/problems/minimum-path-sum/
"""


class Solution:
    def minPathSum(self, grid) -> int:
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        print(dp)
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        print(dp)
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        print(dp)
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        print(dp)
        return dp[rows - 1][columns - 1]


class Solution1:
    def minPathSum(self, grid) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    s = Solution1()
    r = s.minPathSum(grid)
    print(r)
