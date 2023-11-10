#
# @lc app=leetcode.cn id=1405 lang=python3
# @lcpr version=21913
#
# [1405] 最长快乐字符串
#
# https://leetcode.cn/problems/longest-happy-string/description/
#
# algorithms
# Medium (63.53%)
# Likes:    219
# Dislikes: 0
# Total Accepted:    30K
# Total Submissions: 47.3K
# Testcase Example:  '1\n1\n7'
#
# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
# 
# 给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
# 
# 
# s 是一个尽可能长的快乐字符串。
# s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
# s 中只含有 'a'、'b' 、'c' 三种字母。
# 
# 
# 如果不存在这样的字符串 s ，请返回一个空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 输入：a = 1, b = 1, c = 7
# 输出："ccaccbcc"
# 解释："ccbccacc" 也是一种正确答案。
# 
# 
# 示例 2：
# 
# 输入：a = 2, b = 2, c = 1
# 输出："aabbc"
# 
# 
# 示例 3：
# 
# 输入：a = 7, b = 1, c = 0
# 输出："aabaa"
# 解释：这是该测试用例的唯一正确答案。
# 
# 
# 
# 提示：
# 
# 
# 0 <= a, b, c <= 100
# a + b + c > 0
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
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        res = []
        # 每次优先尝试最多的能不能使用， 可以就用，不可以就用第二大
        while a or b or c:
            mx = max(a, b, c)
            if a == mx: 
                if not (len(res) >= 2 and res[-1] == 'a' and res[-2] == 'a'):
                    res.append('a')
                    a -= 1
                else:
                    if max(b, c) == 0:
                        break 
                    if b > c:
                        res.append('b')
                        b -= 1
                    else:
                        res.append('c')
                        c -= 1
            elif b == mx:
                if len(res) < 2 or res[-1] != 'b' or res[-2] != 'b':
                    res.append('b') 
                    b -= 1
                else:
                    if max(a, c) == 0:
                        break 
                    if a > c:
                        res.append('a')
                        a -= 1
                    else:
                        res.append('c')
                        c -= 1
            else:
                if len(res) < 2 or res[-1] != 'c' or res[-2] != 'c':
                    res.append('c')
                    c -= 1
                else:
                    if max(a, b) == 0:
                        break 
                    if a > b:
                        res.append('a')
                        a -= 1
                    else:
                        res.append('b')
                        b -= 1
        return "".join(res)
            

             

# @lc code=end



#
# @lcpr case=start
# 1\n1\n7\n
# @lcpr case=end

# @lcpr case=start
# 2\n2\n1\n
# @lcpr case=end

# @lcpr case=start
# 7\n1\n0\n
# @lcpr case=end

#

