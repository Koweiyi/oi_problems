#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=21913
#
# [70] 爬楼梯
#
# https://leetcode.cn/problems/climbing-stairs/description/
#
# algorithms
# Easy (54.09%)
# Likes:    3181
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2.2M
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 
# 
# 示例 1：
# 
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
# 
# 示例 2：
# 
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 45
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
        self.right = right\

# @lc code=start


# 这块代码只会执行一次
dp = [0 for i in range(50)]
dp[1], dp[2] = 1, 2
for i in range(3, 50):
    dp[i] = dp[i - 1] + dp[i - 2]
    

class Solution:
    def climbStairs(self, n: int) -> int:
        # 记忆化写法
        # @cache
        # def dfs(i: int) -> int:
        #     if i <= 2: return i
        #     return dfs(i - 1) + dfs(i - 2)
        # return dfs(n)

        # O(1)
        return dp[n]
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

