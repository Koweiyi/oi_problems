#
# @lc app=leetcode.cn id=2328 lang=python3
# @lcpr version=21917
#
# [2328] 网格图中递增路径的数目
#
# https://leetcode.cn/problems/number-of-increasing-paths-in-a-grid/description/
#
# algorithms
# Hard (51.35%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    6.8K
# Total Submissions: 13.2K
# Testcase Example:  '[[1,1],[3,4]]'
#
# 给你一个 m x n 的整数网格图 grid ，你可以从一个格子移动到 4 个方向相邻的任意一个格子。
# 
# 请你返回在网格图中从 任意 格子出发，达到 任意 格子，且路径中的数字是 严格递增 的路径数目。由于答案可能会很大，请将结果对 10^9 + 7 取余
# 后返回。
# 
# 如果两条路径中访问过的格子不是完全相同的，那么它们视为两条不同的路径。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：grid = [[1,1],[3,4]]
# 输出：8
# 解释：严格递增路径包括：
# - 长度为 1 的路径：[1]，[1]，[3]，[4] 。
# - 长度为 2 的路径：[1 -> 3]，[1 -> 4]，[3 -> 4] 。
# - 长度为 3 的路径：[1 -> 3 -> 4] 。
# 路径数目为 4 + 3 + 1 = 8 。
# 
# 
# 示例 2：
# 
# 输入：grid = [[1],[2]]
# 输出：3
# 解释：严格递增路径包括：
# - 长度为 1 的路径：[1]，[2] 。
# - 长度为 2 的路径：[1 -> 2] 。
# 路径数目为 2 + 1 = 3 。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 10^5
# 1 <= grid[i][j] <= 10^5
# 
# 
#
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate
from functools import cache
from typing import Optional
from typing import List
from cmath import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        m, n = len(grid), len(grid[0]) 
        @ cache 
        def dfs(x, y):
            res = 1
            for nx, ny in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] < grid[x][y]:
                    res += dfs(nx, ny) 
            return res % mod 
        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod

# @lc code=end



#
# @lcpr case=start
# [[1,1],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1],[2]]\n
# @lcpr case=end

#

