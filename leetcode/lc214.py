#
# @lc app=leetcode.cn id=214 lang=python3
# @lcpr version=21913
#
# [214] 最短回文串
#
# https://leetcode.cn/problems/shortest-palindrome/description/
#
# algorithms
# Hard (40.09%)
# Likes:    545
# Dislikes: 0
# Total Accepted:    47.6K
# Total Submissions: 118.6K
# Testcase Example:  '"aacecaaa"'
#
# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
#
#
#
# 示例 1：
#
# 输入：s = "aacecaaa"
# 输出："aaacecaaa"
#
#
# 示例 2：
#
# 输入：s = "abcd"
# 输出："dcbabcd"
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 5 * 10^4
# s 仅由小写英文字母组成
#
#
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s[::-1] == s:
            return s
        # O(n) 寻找最长的前缀回文串
        mx_pre = 0
        ss = []
        for x in s:
            ss.append('#')
            ss.append(x)
        ss.append('#')
        ss = "".join(ss)
        n = len(ss)
        # manacher 算法
        mx = 0
        d1 = [0] * n
        l, r = 0, -1
        for i in range(0, n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while 0 <= i - k and i + k < n and ss[i - k] == ss[i + k]:
                k += 1
            d1[i] = k
            if d1[i] > i:
                # 找到了一个前缀回文
                if ss[i] == '#':
                    mx_pre = d1[i] // 2 * 2
                else:
                    mx_pre = d1[i] - 1
            k -= 1
            if i + k > r:
                l = i - k
                r = i + k
        return s[mx_pre - len(s):][::-1] + s

# @lc code=end


#
# @lcpr case=start
# "aacecaaa"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end
#
