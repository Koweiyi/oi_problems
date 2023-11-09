#
# @lc app=leetcode.cn id=1092 lang=python3
# @lcpr version=21917
#
# [1092] 最短公共超序列
#
# https://leetcode.cn/problems/shortest-common-supersequence/description/
#
# algorithms
# Hard (58.31%)
# Likes:    238
# Dislikes: 0
# Total Accepted:    18.4K
# Total Submissions: 31.5K
# Testcase Example:  '"abac"\n"cab"'
#
# 给你两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为 子序列 的最短字符串。如果答案不止一个，则可以返回满足条件的 任意一个
# 答案。
# 
# 如果从字符串 t 中删除一些字符（也可能不删除），可以得到字符串 s ，那么 s 就是 t 的一个子序列。
# 
# 
# 
# 示例 1：
# 
# 输入：str1 = "abac", str2 = "cab"
# 输出："cabac"
# 解释：
# str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。 
# str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
# 最终我们给出的答案是满足上述属性的最短字符串。
# 
# 
# 示例 2：
# 
# 输入：str1 = "aaaaaaaa", str2 = "aaaaaaaa"
# 输出："aaaaaaaa"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= str1.length, str2.length <= 1000
# str1 和 str2 都由小写英文字母组成。
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
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i 
        for j in range(n + 1):
            dp[0][j] = j 
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1 
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + 1 
        res = []
        x, y = m, n 
        while x > 0 and y > 0:
            if str1[x - 1] == str2[y - 1]:
                res.append(str1[x - 1])  
                x -= 1
                y -= 1
            elif dp[x][y] == dp[x - 1][y] + 1:
                res.append(str1[x - 1])
                x -= 1
            else:
                res.append(str2[y - 1]) 
                y -= 1 
        while x > 0:
            res.append(str1[x - 1])
            x -= 1
        while y:
            res.append(str2[y - 1])
            y -= 1 
        return "".join(res)[::-1]
# @lc code=end



#
# @lcpr case=start
# "abac"\n"cab"\n
# @lcpr case=end

# @lcpr case=start
# "aaaaaaaa"\n"aaaaaaaa"\n
# @lcpr case=end

#

