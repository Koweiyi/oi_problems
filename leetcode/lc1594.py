#
# @lc app=leetcode.cn id=1594 lang=python3
# @lcpr version=21913
#
# [1594] 矩阵的最大非负积
#
# https://leetcode.cn/problems/maximum-non-negative-product-in-a-matrix/description/
#
# algorithms
# Medium (34.08%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 19.7K
# Testcase Example:  '[[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]'
#
# 给你一个大小为 m x n 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。
# 
# 在从左上角 (0, 0) 开始到右下角 (m - 1, n - 1) 结束的所有路径中，找出具有 最大非负积
# 的路径。路径的积是沿路径访问的单元格中所有整数的乘积。
# 
# 返回 最大非负积 对 10^9 + 7 取余 的结果。如果最大积为 负数 ，则返回 -1 。
# 
# 注意，取余是在得到最大积之后执行的。
# 
# 
# 
# 示例 1：
# 
# 输入：grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
# 输出：-1
# 解释：从 (0, 0) 到 (2, 2) 的路径中无法得到非负积，所以返回 -1 。
# 
# 示例 2：
# 
# 输入：grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
# 输出：8
# 解释：最大非负积对应的路径如图所示 (1 * 1 * -2 * -4 * 1 = 8)
# 
# 
# 示例 3：
# 
# 输入：grid = [[1,3],[0,-4]]
# 输出：0
# 解释：最大非负积对应的路径如图所示 (1 * 0 * -4 = 0)
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 15
# -4 <= grid[i][j] <= 4
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
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # 存下到某个的最大正路径和绝对值最大的负路径和 
        m, n = len(grid), len(grid[0])
        dp = [[[0] * 2 for _ in range(n)] for __ in range(m)]
        if grid[0][0] > 0:
            dp[0][0][0] = grid[0][0]
        else : dp[0][0][1] = grid[0][0]

        flag = any(grid[x][y] == 0 for x in range(m) for y in range(n))
        for i in range(1, m):
            if grid[i][0] > 0:
                dp[i][0][0] = dp[i-1][0][0] * grid[i][0]
                dp[i][0][1] = dp[i-1][0][1] * grid[i][0]
            else: 
                dp[i][0][0] = dp[i-1][0][1] * grid[i][0]
                dp[i][0][1] = dp[i-1][0][0] * grid[i][0]
        for j in range(1, n):
            if grid[0][j] > 0:
                dp[0][j][0] = dp[0][j-1][0] * grid[0][j] 
                dp[0][j][1] = dp[0][j-1][1] * grid[0][j]
            else:
                dp[0][j][0] = dp[0][j-1][1] * grid[0][j] 
                dp[0][j][1] = dp[0][j-1][0] * grid[0][j] 

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] > 0:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0]) * grid[i][j]
                    dp[i][j][1] = min(dp[i-1][j][1], dp[i][j-1][1]) * grid[i][j]
                else:
                    dp[i][j][0] = min(dp[i-1][j][1], dp[i][j-1][1]) * grid[i][j]
                    dp[i][j][1] = max(dp[i-1][j][0], dp[i][j-1][0]) * grid[i][j]
        if  dp[m - 1][n -1][0] == 0:
            if flag:
                return 0 
            return -1
        return dp[-1][-1][0] % (10**9+7)



        
# @lc code=end



#
# @lcpr case=start
# [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,-2,1],[1,-2,1],[3,-4,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[0,-4]]\n
# @lcpr case=end

#

