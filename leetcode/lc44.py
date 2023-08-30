#
# @lc app=leetcode.cn id=44 lang=python3
# @lcpr version=21913
#
# [44] 通配符匹配
#
# https://leetcode.cn/problems/wildcard-matching/description/
#
# algorithms
# Hard (33.82%)
# Likes:    1077
# Dislikes: 0
# Total Accepted:    142.4K
# Total Submissions: 421.1K
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个输入字符串 (s) 和一个字符模式 (p) ，请你实现一个支持 '?' 和 '*' 匹配规则的通配符匹配：
# 
# 
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符序列（包括空字符序列）。
# 
# 
# 
# 
# 判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2：
# 
# 输入：s = "aa", p = "*"
# 输出：true
# 解释：'*' 可以匹配任意字符串。
# 
# 
# 示例 3：
# 
# 输入：s = "cb", p = "?a"
# 输出：false
# 解释：'?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length, p.length <= 2000
# s 仅由小写英文字母组成
# p 仅由小写英文字母、'?' 或 '*' 组成
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
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def dfs(i: int, j: int) -> bool:
            if i == 0 and j == 0:
                return True
            if i == 0:
                return p[j - 1] == "*" and dfs(i, j - 1)
            if j == 0:
                return False
            if p[j - 1] == '?':
                return dfs(i - 1, j - 1)
            if p[j - 1] == '*':
                return dfs(i - 1, j) or dfs(i, j - 1)
            return s[i - 1] == p[j - 1] and dfs(i - 1, j - 1)
        return dfs(len(s), len(p))
# @lc code=end



#
# @lcpr case=start
# "aa"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"*"\n
# @lcpr case=end

# @lcpr case=start
# "cb"\n"?a"\n
# @lcpr case=end

#

