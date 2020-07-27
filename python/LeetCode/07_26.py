# -*- coding: UTF-8 -*-
"""
给定一个整数矩阵，找出最长递增路径的长度。
对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
示例 1:
输入: nums =
    [
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:
    输入: nums =
    [
      [3,4,5],
      [3,2,6],
      [2,2,1]
    ]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
"""


class Solution:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix) -> int:
        if not matrix:
            return 0

        # @lru_cache(None)
        def dfs(row: int, column: int) -> int:
            best = 1
            for dx, dy in Solution.DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    best = max(best, dfs(newRow, newColumn) + 1)
            return best

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans


if __name__ == '__main__':
    nums = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    s = Solution()
    r = s.longestIncreasingPath(nums)
    print(r)
