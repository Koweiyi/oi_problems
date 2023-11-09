#
# @lc app=leetcode.cn id=65 lang=python3
# @lcpr version=21913
#
# [65] 有效数字
#
# https://leetcode.cn/problems/valid-number/description/
#
# algorithms
# Hard (27.60%)
# Likes:    362
# Dislikes: 0
# Total Accepted:    67.3K
# Total Submissions: 243.7K
# Testcase Example:  '"0"'
#
# 有效数字（按顺序）可以分成以下几个部分：
# 
# 
# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数
# 
# 
# 小数（按顺序）可以分成以下几个部分：
# 
# 
# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
# 
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
# 
# 
# 
# 
# 整数（按顺序）可以分成以下几个部分：
# 
# 
# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
# 
# 
# 部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3",
# "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
# 
# 部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
# 
# 给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "0"
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：s = "e"
# 输出：false
# 
# 
# 示例 3：
# 
# 输入：s = "."
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 20
# s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。
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
    def isNumber(self, s: str) -> bool:
        if "inf" in s or "Infinity" in s or "nan" in s:
            return False
        try:
            float(s)
            return True
        except:
            return False

# @lc code=end



#
# @lcpr case=start
# "0"\n
# @lcpr case=end

# @lcpr case=start
# "e"\n
# @lcpr case=end

# @lcpr case=start
# "."\n
# @lcpr case=end

#

