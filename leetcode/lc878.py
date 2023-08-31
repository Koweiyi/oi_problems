#
# @lc app=leetcode.cn id=878 lang=python3
# @lcpr version=21913
#
# [878] 第 N 个神奇数字
#
# https://leetcode.cn/problems/nth-magical-number/description/
#
# algorithms
# Hard (39.97%)
# Likes:    218
# Dislikes: 0
# Total Accepted:    24.2K
# Total Submissions: 60.5K
# Testcase Example:  '1\n2\n3'
#
# 一个正整数如果能被 a 或 b 整除，那么它是神奇的。
# 
# 给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 10^9 + 7 取模 后的值。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：n = 1, a = 2, b = 3
# 输出：2
# 
# 
# 示例 2：
# 
# 输入：n = 4, a = 2, b = 3
# 输出：6
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^9
# 2 <= a, b <= 4 * 10^4
# 
# 
# 
# 
#
from math import gcd
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
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # 二分
        lcm = a * b // (gcd(a, b))
        l = 0 
        r = min(a, b) * n 
        while l + 1 < r:
            mid = l + (r - l) // 2 
            if mid // a + mid // b - mid // lcm >= n:
                r = mid 
            else:
                l = mid
        return r % (10 ** 9 + 7)
# @lc code=end



#
# @lcpr case=start
# 1\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 4\n2\n3\n
# @lcpr case=end

#

