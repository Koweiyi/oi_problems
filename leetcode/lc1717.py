#
# @lc app=leetcode.cn id=1717 lang=python3
# @lcpr version=21913
#
# [1717] 删除子字符串的最大得分
#
# https://leetcode.cn/problems/maximum-score-from-removing-substrings/description/
#
# algorithms
# Medium (46.41%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 8.5K
# Testcase Example:  '"cdbcbbaaabab"\n4\n5'
#
# 给你一个字符串 s 和两个整数 x 和 y 。你可以执行下面两种操作任意次。
# 
# 
# 删除子字符串 "ab" 并得到 x 分。
# 
# 
# 比方说，从 "cabxbae" 删除 ab ，得到 "cxbae" 。
# 
# 
# 删除子字符串"ba" 并得到 y 分。
# 
# 比方说，从 "cabxbae" 删除 ba ，得到 "cabxe" 。
# 
# 
# 
# 
# 请返回对 s 字符串执行上面操作若干次能得到的最大得分。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "cdbcbbaaabab", x = 4, y = 5
# 输出：19
# 解释：
# - 删除 "cdbcbbaaabab" 中加粗的 "ba" ，得到 s = "cdbcbbaaab" ，加 5 分。
# - 删除 "cdbcbbaaab" 中加粗的 "ab" ，得到 s = "cdbcbbaa" ，加 4 分。
# - 删除 "cdbcbbaa" 中加粗的 "ba" ，得到 s = "cdbcba" ，加 5 分。
# - 删除 "cdbcba" 中加粗的 "ba" ，得到 s = "cdbc" ，加 5 分。
# 总得分为 5 + 4 + 5 + 5 = 19 。
# 
# 示例 2：
# 
# 输入：s = "aabbaaxybbaabb", x = 5, y = 4
# 输出：20
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# 1 <= x, y <= 10^4
# s 只包含小写英文字母。
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
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0 
        if x > y:
            prex = 'a'
        else:
            prex = 'b'
        def sovle(a:str)-> int:
            resa = 0
            sta = []
            for ch in a:
                if ch == prex:
                    sta.append(ch)
                else:
                    if sta and sta[-1] == prex:
                        resa += max(x, y)
                        sta.pop()
                    else:
                        sta.append(ch)
            cp = 0
            for ch in sta:
                if ch == prex:
                    cp += 1 
            cnt = min(cp, len(sta) - cp)
            resa += cnt * min(x, y)
            return resa

            pass 
        i = 0 
        while i < len(s):
            if s[i] == 'a' or s[i] == 'b':
                j = i 
                while j < len(s) and s[j] in "ab":
                    j += 1 
                res += sovle(s[i:j])
                i = j + 1
            else:
                i += 1
        return res 
            
# @lc code=end



#
# @lcpr case=start
# "cdbcbbaaabab"\n4\n5\n
# @lcpr case=end

# @lcpr case=start
# "aabbaaxybbaabb"\n5\n4\n
# @lcpr case=end

#

