#
# @lc app=leetcode.cn id=233 lang=python3
# @lcpr version=21913
#
# [233] 数字 1 的个数
#
# https://leetcode.cn/problems/number-of-digit-one/description/
#
# algorithms
# Hard (49.18%)
# Likes:    537
# Dislikes: 0
# Total Accepted:    57.2K
# Total Submissions: 116.4K
# Testcase Example:  '13'
#
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 13
# 输出：6
# 
# 
# 示例 2：
# 
# 输入：n = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 10^9
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
    def countDigitOne(self, n: int) -> int:
        # 经典数位 DP
        s = str(n)
        @cache
        def dfs(i:int, cnt1: int, is_num: bool, is_limit: bool) -> int:
            if i == len(s):
                return cnt1 if is_num else 0
            res = 0 if is_num else dfs(i + 1, cnt1, False, False) 
            low = 0 if is_num else 1 
            up = int(s[i]) if is_limit else 9
            for d in range(low, up + 1):
                res += dfs(i + 1, cnt1 + int(d == 1), True, is_limit and d == up)
            return res 
        return dfs(0, 0, False, True)
# @lc code=end



#
# @lcpr case=start
# 13\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#

