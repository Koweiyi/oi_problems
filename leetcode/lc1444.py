#
# @lc app=leetcode.cn id=1444 lang=python3
# @lcpr version=21913
#
# [1444] 切披萨的方案数
#
# https://leetcode.cn/problems/number-of-ways-of-cutting-a-pizza/description/
#
# algorithms
# Hard (54.46%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    8K
# Total Submissions: 13.6K
# Testcase Example:  '["A..","AAA","..."]\n3'
#
# 给你一个 rows x cols 大小的矩形披萨和一个整数 k ，矩形包含两种字符： 'A' （表示苹果）和 '.' （表示空白格子）。你需要切披萨
# k-1 次，得到 k 块披萨并送给别人。
# 
# 
# 切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。
# 
# 请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：pizza = ["A..","AAA","..."], k = 3
# 输出：3 
# 解释：上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。
# 
# 
# 示例 2：
# 
# 输入：pizza = ["A..","AA.","..."], k = 3
# 输出：1
# 
# 
# 示例 3：
# 
# 输入：pizza = ["A..","A..","..."], k = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= rows, cols <= 50
# rows == pizza.length
# cols == pizza[i].length
# 1 <= k <= 10
# pizza 只包含字符 'A' 和 '.' 。
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])

        pre = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = pre[i + 1][j] + pre[i][j + 1] - pre[i][j] + int(pizza[i][j] == 'A')

        MOD = 10 ** 9 + 7

        dp = [[[0 for i in range(k)] for j in range(n + 1)] for o in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if pre[m][n] - pre[i][n] - pre[m][j] + pre[i][j] > 0:
                    dp[i][j][k - 1] = 1
        
        for o in range(k - 2, -1, -1):
            for i in range(m):
                for j in range(n):
                    for x in range(i, m):
                        if pre[x + 1][n] - pre[x + 1][j] - pre[i][n] + pre[i][j] > 0:
                            dp[i][j][o] += dp[x + 1][j][o + 1]
                    for y in range(j, n):
                        if pre[m][y + 1] - pre[m][j] - pre[i][y + 1] + pre[i][j] > 0:
                            dp[i][j][o] += dp[i][y + 1][o + 1]
                    dp[i][j][o] %= MOD
        return dp[0][0][0]
        # 记忆化写法
        # @cache
        # def dfs(i, j, c):
        #     res = 0
        #     if c == k - 1:
        #         if pre[m][n] - pre[i][n] - pre[m][j] + pre[i][j]:
        #             return 1
        #         return 0
        #     for x in range(i, m):
        #         if pre[x + 1][n] - pre[x + 1][j] - pre[i][n] + pre[i][j] > 0:
        #             res += dfs(x + 1, j, c + 1)
        #     for y in range(j, n):
        #         if pre[m][y + 1] - pre[m][j] - pre[i][y + 1] + pre[i][j] > 0:
        #             res += dfs(i, y + 1, c + 1)
        #     return res % MOD
        # return dfs(0, 0, 0)
            
# @lc code=end



#
# @lcpr case=start
# ["A..","AAA","..."]\n3\n
# @lcpr case=end

# @lcpr case=start
# ["A..","AA.","..."]\n3\n
# @lcpr case=end

# @lcpr case=start
# ["A..","A..","..."]\n1\n
# @lcpr case=end

#

