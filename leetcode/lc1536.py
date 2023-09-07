#
# @lc app=leetcode.cn id=1536 lang=python3
# @lcpr version=21913
#
# [1536] 排布二进制网格的最少交换次数
#
# https://leetcode.cn/problems/minimum-swaps-to-arrange-a-binary-grid/description/
#
# algorithms
# Medium (46.46%)
# Likes:    51
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 11.7K
# Testcase Example:  '[[0,0,1],[1,1,0],[1,0,0]]'
#
# 给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。
# 
# 一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。
# 
# 请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。
# 
# 主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 
# 输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# 输出：-1
# 解释：所有行都是一样的，交换相邻行无法使网格符合要求。
# 
# 
# 示例 3：
# 
# 
# 
# 输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# n == grid.length
# n == grid[i].length
# 1 <= n <= 200
# grid[i][j] 要么是 0 要么是 1 。
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
    def minSwaps(self, grid: List[List[int]]) -> int:
        # 相邻交换排序的最少移动次数
        n = len(grid)
        arr = []
        for g in grid:
            lg = 0
            for j in range(n - 1, -1, -1):
                if g[j] == 0:
                    lg += 1
                else:
                    break 
            arr.append(lg)
        b = sorted(arr) 
        for j in range(n - 1, -1, -1):
            if b[j] < j :
                return -1 
        res = 0 
        for i in range(n - 1):
            for j in range(i, n):
                if arr[j] >= n - i - 1:
                    while j > i:
                        res += 1
                        arr[j], arr[j - 1] = arr[j - 1], arr[j]
                        j -= 1 
                    break
        return res 




# @lc code=end



#
# @lcpr case=start
# [[0,0,1],[1,1,0],[1,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0],[1,1,0],[1,1,1]]\n
# @lcpr case=end

#

