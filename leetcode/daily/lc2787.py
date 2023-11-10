#
# @lc app=leetcode.cn id=2787 lang=python3
# @lcpr version=21913
#
# [2787] 将一个数字表示成幂的和的方案数
#
# https://leetcode.cn/problems/ways-to-express-an-integer-as-sum-of-powers/description/
#
# algorithms
# Medium (43.44%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 6.8K
# Testcase Example:  '10\n2'
#
# 给你两个 正 整数 n 和 x 。
# 
# 请你返回将 n 表示成一些 互不相同 正整数的 x 次幂之和的方案数。换句话说，你需要返回互不相同整数 [n1, n2, ..., nk]
# 的集合数目，满足 n = n1^x + n2^x + ... + nk^x 。
# 
# 由于答案可能非常大，请你将它对 10^9 + 7 取余后返回。
# 
# 比方说，n = 160 且 x = 3 ，一个表示 n 的方法是 n = 2^3 + 3^3 + 5^3^ 。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 10, x = 2
# 输出：1
# 解释：我们可以将 n 表示为：n = 3^2 + 1^2 = 10 。
# 这是唯一将 10 表达成不同整数 2 次方之和的方案。
# 
# 
# 示例 2：
# 
# 输入：n = 4, x = 1
# 输出：2
# 解释：我们可以将 n 按以下方案表示：
# - n = 4^1 = 4 。
# - n = 3^1 + 1^1 = 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 300
# 1 <= x <= 5
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
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0] * (n + 1) 
        dp[0] = 1 
        for i in range(1, n + 1):
            if i ** x > n:
                break
            for j in range(n, pow(i, x) - 1, -1):
                dp[j] += dp[j - pow(i, x)]
        return dp[n] % (10 ** 9 + 7)
# @lc code=end



#
# @lcpr case=start
# 10\n2\n
# @lcpr case=end

# @lcpr case=start
# 4\n1\n
# @lcpr case=end

# @lcpr case=start
# 153\n1\n
# @lcpr case=end
#

