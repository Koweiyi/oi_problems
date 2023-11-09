#
# @lc app=leetcode.cn id=1631 lang=python3
# @lcpr version=21914
#
# [1631] 最小体力消耗路径
#
# https://leetcode.cn/problems/path-with-minimum-effort/description/
#
# algorithms
# Medium (50.91%)
# Likes:    378
# Dislikes: 0
# Total Accepted:    44.7K
# Total Submissions: 87.9K
# Testcase Example:  '[[1,2,2],[3,8,2],[5,3,5]]'
#
# 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子
# (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0
# 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。
# 
# 一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。
# 
# 请你返回从左上角走到右下角的最小 体力消耗值 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
# 输出：2
# 解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
# 这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
# 输出：1
# 解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
# 
# 
# 示例 3：
# 
# 输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# 输出：0
# 解释：上图所示路径不需要消耗任何体力。
# 
# 
# 
# 
# 提示：
# 
# 
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 10^6
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
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # 二分答案)
        m, n = len(heights), len(heights[0])
        def check(md: int) -> bool:
            vis = [[False] * n for _ in range(m)]
            def dfs(x: int, y: int) -> bool:
                if x == m - 1 and y == n - 1:
                    return True
                

                for nx, ny in (x+1, y), (x, y+1), (x-1, y), (x, y-1):
                    # print(nx, ny, m, n)
                    if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny] and abs(heights[nx][ny] - heights[x][y]) <= md:
                        vis[nx][ny] = True 
                        if dfs(nx, ny):
                            return True 
                return False
            vis[0][0] = True
            return dfs(0, 0)
    

        l, r = -1, 10 ** 7 
        while l + 1 < r:
            mid = (l + r) // 2 
            if check(mid) :
                r = mid 
            else:
                l = mid 
        return r  
# @lc code=end



#
# @lcpr case=start
# [[1,2,2],[3,8,2],[5,3,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[3,8,4],[5,3,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[10,8],[10,8],[1,2],[10,3],[1,3],[6,3],[5,2]]
# @lcpr case=end

#

