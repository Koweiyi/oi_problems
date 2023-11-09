#
# @lc app=leetcode.cn id=1316 lang=python3
# @lcpr version=21913
#
# [1316] 不同的循环子字符串
#
# https://leetcode.cn/problems/distinct-echo-substrings/description/
#
# algorithms
# Hard (48.72%)
# Likes:    52
# Dislikes: 0
# Total Accepted:    5.2K
# Total Submissions: 10.6K
# Testcase Example:  '"abcabcabc"'
#
# 给你一个字符串 text ，请你返回满足下述条件的 不同 非空子字符串的数目：
# 
# 
# 可以写成某个字符串与其自身相连接的形式（即，可以写为 a + a，其中 a 是某个字符串）。
# 
# 
# 例如，abcabc 就是 abc 和它自身连接形成的。
# 
# 
# 
# 示例 1：
# 
# 输入：text = "abcabcabc"
# 输出：3
# 解释：3 个子字符串分别为 "abcabc"，"bcabca" 和 "cabcab" 。
# 
# 
# 示例 2：
# 
# 输入：text = "leetcodeleetcode"
# 输出：2
# 解释：2 个子字符串为 "ee" 和 "leetcodeleetcode" 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= text.length <= 2000
# text 只包含小写英文字母。
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
    def distinctEchoSubstrings(self, text: str) -> int:
        res = set()
        # 拓展kmp 算法
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
        for i in range(len(text)):
            z = z_function(text[i:])
            for j, le in enumerate(z):
                if  le >= j and j:
                    res.add(text[i:i + j])
        return len(res)
        
# @lc code=end



#
# @lcpr case=start
# "abcabcabc"\n
# @lcpr case=end

# @lcpr case=start
# "leetcodeleetcode"\n
# @lcpr case=end

#

