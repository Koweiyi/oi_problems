#
# @lc app=leetcode.cn id=1895 lang=python3
# @lcpr version=21913
#
# [1895] 最大的幻方
#
# https://leetcode.cn/problems/largest-magic-square/description/
#
# algorithms
# Medium (56.53%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 5.9K
# Testcase Example:  '[[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]'
#
# 一个 k x k 的 幻方 指的是一个 k x k 填满整数的方格阵，且每一行、每一列以及两条对角线的和 全部相等 。幻方中的整数 不需要互不相同
# 。显然，每个 1 x 1 的方格都是一个幻方。
# 
# 给你一个 m x n 的整数矩阵 grid ，请你返回矩阵中 最大幻方 的 尺寸 （即边长 k）。
# 
# 
# 
# 示例 1：
# 
# 输入：grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
# 输出：3
# 解释：最大幻方尺寸为 3 。
# 每一行，每一列以及两条对角线的和都等于 12 。
# - 每一行的和：5+1+6 = 5+4+3 = 2+7+3 = 12
# - 每一列的和：5+5+2 = 1+4+7 = 6+3+3 = 12
# - 对角线的和：5+4+3 = 6+4+2 = 12
# 
# 
# 示例 2：
# 
# 输入：grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 10^6
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter, defaultdict
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + grid[i][j]

        def check(i:int, j:int, k:int) -> bool:
                
            a = [s[x + 1][j + 1] - s[x][j + 1] - s[x + 1][j - k + 1] + s[x][j - k + 1] for x in range(i - k + 1, i + 1)]
            b = [s[i + 1][y + 1] - s[i + 1][y] - s[i - k + 1][y + 1] + s[i - k + 1][y] for y in range(j - k + 1, j + 1)]
            s1 = sum(grid[x][i + j - k + 1 - x] for x in range(i - k + 1, i + 1))
            s2 = sum(grid[x][x - i + j] for x in range(i - k + 1, i + 1))
            return len(set(a + b + [s1, s2])) == 1
            
        for k in range(min(m, n), 1, -1):
            for i in range(k -1, m):
                for j in range(k - 1, n):
                    if check(i, j, k):
                        return k
        return 1 
# @lc code=end



#
# @lcpr case=start
# [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,3,1],[9,3,3,1],[1,3,3,8]]\n
# @lcpr case=end

#

