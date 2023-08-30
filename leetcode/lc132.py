#
# @lc app=leetcode.cn id=132 lang=python3
# @lcpr version=21913
#
# [132] 分割回文串 II
#
# https://leetcode.cn/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (49.95%)
# Likes:    700
# Dislikes: 0
# Total Accepted:    80.1K
# Total Submissions: 160.4K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
# 
# 返回符合要求的 最少分割次数 。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# 
# 
# 示例 2：
# 
# 输入：s = "a"
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：s = "ab"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 2000
# s 仅由小写英文字母组成
# 
# 
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
    def minCut(self, s: str) -> int:
        # 
        n = len(s)
        @cache
        def dfs(i:int, j: int) -> bool:
            if i >= j :
                return True 
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            else:
                return False

        # print(dfs(0, 3))
        dp = [inf] * (n + 1) 
        dp[0] = 0
        for i in range(n):
            if dfs(0, i):
                dp[i + 1] = 1
            else:
                for j in range(i + 1):
                    if dfs(j, i):
                        dp[i + 1] = min(dp[i + 1], dp[j] + 1)
        return dp[n] - 1
# @lc code=end



#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "abbab"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n
# @lcpr case=end

#

