#
# @lc app=leetcode.cn id=1392 lang=python3
# @lcpr version=21913
#
# [1392] 最长快乐前缀
#
# https://leetcode.cn/problems/longest-happy-prefix/description/
#
# algorithms
# Hard (44.61%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    14.6K
# Total Submissions: 32.6K
# Testcase Example:  '"level"'
#
# 「快乐前缀」 是在原字符串中既是 非空 前缀也是后缀（不包括原字符串自身）的字符串。
# 
# 给你一个字符串 s，请你返回它的 最长快乐前缀。如果不存在满足题意的前缀，则返回一个空字符串 "" 。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "level"
# 输出："l"
# 解释：不包括 s 自己，一共有 4 个前缀（"l", "le", "lev", "leve"）和 4 个后缀（"l", "el", "vel",
# "evel"）。最长的既是前缀也是后缀的字符串是 "l" 。
# 
# 
# 示例 2：
# 
# 输入：s = "ababab"
# 输出："abab"
# 解释："abab" 是最长的既是前缀也是后缀的字符串。题目允许前后缀在原字符串中重叠。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s 只含有小写英文字母
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
    def longestPrefix(self, s: str) -> str:

        # 拓展KMP 模板 
        # 求最长公共前缀
        def z_function(s: str) -> List[int]:
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r and z[i - l] < r - i + 1:
                    z[i] = z[i - l]
                else:
                    z[i] = max(0, r - i + 1)
                    while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                        z[i] += 1
                if i + z[i] - 1 > r:
                    l = i
                    r = i + z[i] - 1
            return z
        z = z_function(s)

        for i in range(len(z)):
            if i + z[i] == len(z):
                return s[:z[i]]
        return ""
# @lc code=end



#
# @lcpr case=start
# "level"\n
# @lcpr case=end

# @lcpr case=start
# "ababab"\n
# @lcpr case=end

#

