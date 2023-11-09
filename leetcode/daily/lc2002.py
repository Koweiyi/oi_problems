#
# @lc app=leetcode.cn id=2002 lang=python3
# @lcpr version=21913
#
# [2002] 两个回文子序列长度的最大乘积
#
# https://leetcode.cn/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/description/
#
# algorithms
# Medium (60.59%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 10K
# Testcase Example:  '"leetcodecom"'
#
# 给你一个字符串 s ，请你找到 s 中两个 不相交回文子序列 ，使得它们长度的 乘积最大 。两个子序列在原字符串中如果没有任何相同下标的字符，则它们是
# 不相交 的。
# 
# 请你返回两个回文子序列长度可以达到的 最大乘积 。
# 
# 子序列
# 指的是从原字符串中删除若干个字符（可以一个也不删除）后，剩余字符不改变顺序而得到的结果。如果一个字符串从前往后读和从后往前读一模一样，那么这个字符串是一个
# 回文字符串 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：s = "leetcodecom"
# 输出：9
# 解释：最优方案是选择 "ete" 作为第一个子序列，"cdc" 作为第二个子序列。
# 它们的乘积为 3 * 3 = 9 。
# 
# 
# 示例 2：
# 
# 输入：s = "bb"
# 输出：1
# 解释：最优方案为选择 "b" （第一个字符）作为第一个子序列，"b" （第二个字符）作为第二个子序列。
# 它们的乘积为 1 * 1 = 1 。
# 
# 
# 示例 3：
# 
# 输入：s = "accbcaxxcxx"
# 输出：25
# 解释：最优方案为选择 "accca" 作为第一个子序列，"xxcxx" 作为第二个子序列。
# 它们的乘积为 5 * 5 = 25 。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= s.length <= 12
# s 只含有小写英文字母。
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
    def maxProduct(self, s: str) -> int:
        # 暴力吗， 只有 12 欸 
        # 暴力思路是，枚举每个字符在哪个集合 , 然后每个集合内求一个最长回文子序列 相乘就好了 
        # 时间复杂度是 O(2^n)*n^2
        a = []
        b = []
        res = 0
        # 返回最长回文子序列 
        def solve(arr:List[str]) -> int:
            # 也就是求arr 和 arr[::-1] 的最长公共子序列 
            s = "".join(arr)
            t = "".join(arr[::-1])
            @cache
            def lcs(i: int, j: int):
                if i == 0 or j == 0:
                    return 0 
                if s[i - 1] == t[j - 1]:
                    return lcs(i - 1, j - 1) + 1
                return max(lcs(i - 1, j), lcs(i, j - 1))
            return lcs(len(s), len(t))
        def dfs(i: int):
            nonlocal res 
            if i == len(s):
                res = max(res, solve(a) * solve(b))
                return 
            a.append(s[i])
            dfs(i + 1)
            a.pop()
            b.append(s[i])
            dfs(i + 1)
            b.pop()
        dfs(0)
        return res 
    
        # 有没有更优秀的解法 
# @lc code=end



#
# @lcpr case=start
# "leetcodecom"\n
# @lcpr case=end

# @lcpr case=start
# "bb"\n
# @lcpr case=end

# @lcpr case=start
# "accbcaxxcxx"\n
# @lcpr case=end

#

