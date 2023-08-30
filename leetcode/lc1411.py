#
# @lc app=leetcode.cn id=1411 lang=python3
# @lcpr version=21913
#
# [1411] 给 N x 3 网格图涂色的方案数
#
# https://leetcode.cn/problems/number-of-ways-to-paint-n-3-grid/description/
#
# algorithms
# Hard (57.42%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    10.1K
# Total Submissions: 17.5K
# Testcase Example:  '1'
#
# 你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿
# 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。
# 
# 给你网格图的行数 n 。
# 
# 请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 1
# 输出：12
# 解释：总共有 12 种可行的方法：
# 
# 
# 
# 示例 2：
# 
# 输入：n = 2
# 输出：54
# 
# 
# 示例 3：
# 
# 输入：n = 3
# 输出：246
# 
# 
# 示例 4：
# 
# 输入：n = 7
# 输出：106494
# 
# 
# 示例 5：
# 
# 输入：n = 5000
# 输出：30228214
# 
# 
# 
# 
# 提示：
# 
# 
# n == grid.length
# grid[i].length == 3
# 1 <= n <= 5000
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        strs = ["rbg","rbr","rgb","rgr","brg","bgr","bgb","brb","gbr","grb","gbg","grg"]
        mapping = [[] for _ in range(12)]
        for i in range(12):
            for j in range(12):
                if all(x != y for x, y in zip(strs[i], strs[j])):
                    mapping[i].append(j)
        dp = [[1] * 12 for _ in range(2)]
        for i in range(2, n + 1):
            for j in range(12):
                dp[i % 2][j] = sum(dp[(i + 1) % 2][x] for x in mapping[j]) % mod
        return sum(dp[n % 2]) % mod
# @lc code=end



#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 7\n
# @lcpr case=end

# @lcpr case=start
# 5000\n
# @lcpr case=end

#

