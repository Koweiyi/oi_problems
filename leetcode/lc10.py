#
# @lc app=leetcode.cn id=10 lang=python3
# @lcpr version=21913
#
# [10] 正则表达式匹配
#
# https://leetcode.cn/problems/regular-expression-matching/description/
#
# algorithms
# Hard (30.72%)
# Likes:    3698
# Dislikes: 0
# Total Accepted:    383.3K
# Total Submissions: 1.2M
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# 
# 
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 
# 
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
# 
# 
# 示例 1：
# 
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2:
# 
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 
# 
# 示例 3：
# 
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s 只包含从 a-z 的小写字母。
# p 只包含从 a-z 的小写字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符
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

        def match(i: int, j: int) -> bool:
            if p[j]== '.':
                return True
            return s[i] == p[j]

        @cache
        def dfs(i: int, j: int) -> bool:
            if i == 0 and j == 0:
                return True
            if j == 0:
                return False
            if i == 0 :
                if p[j - 1] != "*":
                    return False
                return dfs(i, j - 2)
            if p[j - 1] == '.':
                return dfs(i - 1, j - 1)
            if p[j - 1] == '*':
                res = dfs(i, j - 2)  #匹配0次
                if match(i - 1, j - 2):
                    res = res or dfs(i - 1, j)
                return res 
            return s[i - 1] == p[j - 1] and dfs(i - 1, j - 1)
        return dfs(len(s), len(p))
        
# @lc code=end



#
# @lcpr case=start
# "aa"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"a*"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n".*"\n
# @lcpr case=end

#

