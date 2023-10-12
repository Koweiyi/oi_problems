#
# @lc app=leetcode.cn id=1293 lang=python3
# @lcpr version=21917
#
# [1293] 网格中的最短路径
#
# https://leetcode.cn/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
#
# algorithms
# Hard (38.48%)
# Likes:    241
# Dislikes: 0
# Total Accepted:    22.7K
# Total Submissions: 59K
# Testcase Example:  '[[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]\n1'
#
# 给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。
# 
# 如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1)
# 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入： grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# 输出：6
# 解释：
# 不消除任何障碍的最短路径是 10。
# 消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) ->
# (3,2) -> (4,2).
# 
# 
# 示例 2：
# 
# 
# 
# 输入：grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# 输出：-1
# 解释：我们至少需要消除两个障碍才能找到这样的路径。
# 
# 
# 
# 
# 提示：
# 
# 
# grid.length == m
# grid[0].length == n
# 1 <= m, n <= 40
# 1 <= k <= m*n
# grid[i][j] 是 0 或 1
# grid[0][0] == grid[m-1][n-1] == 0
# 
# 
#
from collections import Counter, defaultdict, deque
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
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = [(0, 0, k)]
        vis = set((0, 0, k))
        step = 0
        while q:
            tmp = q 
            q = []
            for x, y, left in tmp:
                if x == m - 1 and y == n - 1:
                    return step
                for nx, ny in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                    if 0 <= nx < m and 0 <= ny < n and left >= grid[nx][ny] and (nx, ny, left - grid[nx][ny]) not in vis:
                        vis.add((nx,ny,left - grid[nx][ny]))
                        q.append((nx, ny, left - grid[nx][ny]))
            step += 1 
        return -1
# @lc code=end



#
# @lcpr case=start
# [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,1],[1,1,1],[1,0,0]]\n1\n
# @lcpr case=end

#

