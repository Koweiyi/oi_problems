#
# @lc app=leetcode.cn id=866 lang=python3
# @lcpr version=21914
#
# [866] 回文素数
#
# https://leetcode.cn/problems/prime-palindrome/description/
#
# algorithms
# Medium (23.94%)
# Likes:    97
# Dislikes: 0
# Total Accepted:    11.6K
# Total Submissions: 48.4K
# Testcase Example:  '6'
#
# 求出大于或等于 N 的最小回文素数。
# 
# 回顾一下，如果一个数大于 1，且其因数只有 1 和它自身，那么这个数是素数。
# 
# 例如，2，3，5，7，11 以及 13 是素数。
# 
# 回顾一下，如果一个数从左往右读与从右往左读是一样的，那么这个数是回文数。
# 
# 例如，12321 是回文数。
# 
# 
# 
# 示例 1：
# 
# 输入：6
# 输出：7
# 
# 
# 示例 2：
# 
# 输入：8
# 输出：11
# 
# 
# 示例 3：
# 
# 输入：13
# 输出：101
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 10^8
# 答案肯定存在，且小于 2 * 10^8。
# 
# 
# 
# 
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
from math import isqrt
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False 
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False 
            return True 

        for l in range(1, 6):
            if l * 2 < len(str(n)):continue
            for root in range(10 ** (l - 1), 10 ** l):
                s = str(root)
                x = int(s + s[-2::-1])
                if x >= n and is_prime(x):
                    return x 
            for root in range(10 ** (l - 1), 10 ** l):
                s = str(root)
                x = int(s + s[::-1])

                if x >= n and is_prime(x):
                    return x
        

# @lc code=end



#
# @lcpr case=start
# 6\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

#

