#
# @lc app=leetcode.cn id=790 lang=python3
# @lcpr version=21913
#
# [790] 多米诺和托米诺平铺
#
# https://leetcode.cn/problems/domino-and-tromino-tiling/description/
#
# algorithms
# Medium (54.94%)
# Likes:    321
# Dislikes: 0
# Total Accepted:    28.3K
# Total Submissions: 51.4K
# Testcase Example:  '3'
#
# 有两种形状的瓷砖：一种是 2 x 1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。
# 
# 
# 
# 给定整数 n ，返回可以平铺 2 x n 的面板的方法的数量。返回对 10^9 + 7 取模 的值。
# 
# 平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 输入: n = 3
# 输出: 5
# 解释: 五种不同的方法如上所示。
# 
# 
# 示例 2:
# 
# 输入: n = 1
# 输出: 1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 1000
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
    def numTilings(self, n: int) -> int:
        # 有点事 没睡好，看会儿书
        if n < 2:
            return 1

        mod = 10 ** 9 + 7 
        dp = [[0] for _ in range(n + 1)]  
        dp[0] = dp[1] = 1
        dp[2] = 2 
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % mod
        return dp[n]
        
        

        
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

