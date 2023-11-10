#
# @lc app=leetcode.cn id=1559 lang=python3
# @lcpr version=21913
#
# [1559] 二维网格图中探测环
#
# https://leetcode.cn/problems/detect-cycles-in-2d-grid/descrip+tion/
#
# algorithms
# Medium (40.83%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    7.2K
# Total Submissions: 17.7K
# Testcase Example:  '[["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]'
#
# 给你一个二维字符网格数组 grid ，大小为 m x n ，你需要检查 grid 中是否存在 相同值 形成的环。
# 
# 一个环是一条开始和结束于同一个格子的长度 大于等于 4
# 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这两个格子有 相同的值 。
# 
# 同时，你也不能回到上一次移动时所在的格子。比方说，环  (1, 1) -> (1, 2) -> (1, 1) 是不合法的，因为从 (1, 2) 移动到
# (1, 1) 回到了上一次移动时的格子。
# 
# 如果 grid 中有相同值形成的环，请你返回 true ，否则返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：grid =
# [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# 输出：true
# 解释：如下图所示，有 2 个用不同颜色标出来的环：
# 
# 
# 
# 示例 2：
# 
# 
# 
# 输入：grid =
# [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# 输出：true
# 解释：如下图所示，只有高亮所示的一个合法环：
# 
# 
# 
# 示例 3：
# 
# 
# 
# 输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m <= 500
# 1 <= n <= 500
# grid 只包含小写英文字母。
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
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m,n = len(grid), len(grid[0])
        # 不是深搜,应该广搜

        vis = [[False] * n for _ in range(m)]

        def bfs(i: int, j: int) -> bool:
            q = [(i, j)]
            while q:
                tmp = q 
                q = []
                scur = set()
                for x, y in tmp:
                    for nx, ny in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                        if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny] and grid[nx][ny] == grid[x][y]:
                            if (nx, ny) in scur:
                                return True 
                            scur.add((nx, ny))
                            q.append((nx, ny))
                for x, y in scur:
                    vis[x][y] = True 
            return False 
            
        for i in range(m):
            for j in range(n):
                if not vis[i][j]:
                    vis[i][j] = True 
                    if bfs(i, j):
                        return True 
        return False 



# @lc code=end



#
# @lcpr case=start
# [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]\n
# @lcpr case=end

# @lcpr case=start
# [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b","b"],["b","z","b"],["b","b","a"]]\n
# @lcpr case=end

# @lcpr case=start
# [["b","a","c"],["c","a","c"],["d","d","c"], ["b", "c","c"]]\n
# @lcpr case=end

# @lcpr case=start
# [["f","a","a","c","b"],["e","a","a","e","c"],["c","f","b","b","b"],["c","e","a","b","e"],["f","e","f","b","f"]]\n
# @lcpr case=end

#

