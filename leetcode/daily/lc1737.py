#
# @lc app=leetcode.cn id=1737 lang=python3
# @lcpr version=21914
#
# [1737] 满足三条件之一需改变的最少字符数
#
# https://leetcode.cn/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/description/
#
# algorithms
# Medium (36.10%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 16.6K
# Testcase Example:  '"aba"\n"caa"'
#
# 给你两个字符串 a 和 b ，二者均由小写字母组成。一步操作中，你可以将 a 或 b 中的 任一字符 改变为 任一小写字母 。
# 
# 操作的最终目标是满足下列三个条件 之一 ：
# 
# 
# a 中的 每个字母 在字母表中 严格小于 b 中的 每个字母 。
# b 中的 每个字母 在字母表中 严格小于 a 中的 每个字母 。
# a 和 b 都 由 同一个 字母组成。
# 
# 
# 返回达成目标所需的 最少 操作数。
# 
# 
# 
# 示例 1：
# 
# 输入：a = "aba", b = "caa"
# 输出：2
# 解释：满足每个条件的最佳方案分别是：
# 1) 将 b 变为 "ccc"，2 次操作，满足 a 中的每个字母都小于 b 中的每个字母；
# 2) 将 a 变为 "bbb" 并将 b 变为 "aaa"，3 次操作，满足 b 中的每个字母都小于 a 中的每个字母；
# 3) 将 a 变为 "aaa" 并将 b 变为 "aaa"，2 次操作，满足 a 和 b 由同一个字母组成。
# 最佳的方案只需要 2 次操作（满足条件 1 或者条件 3）。
# 
# 
# 示例 2：
# 
# 输入：a = "dabadd", b = "cda"
# 输出：3
# 解释：满足条件 1 的最佳方案是将 b 变为 "eee" 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= a.length, b.length <= 10^5
# a 和 b 只由小写字母组成
# 
# 
#
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate, pairwise
from functools import cache
from string import ascii_lowercase
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
    def minCharacters(self, a: str, b: str) -> int:
        ca = Counter(a)
        cb = Counter(b)
        res = len(a) + len(b) - max(ca[x] + cb[x] for x in ascii_lowercase)
        for x, y in pairwise(ascii_lowercase):
            ca[y] += ca[x]
            cb[y] += cb[x]
    
        for ch in ascii_lowercase:
            res = min(res, len(a) - ca[ch] + cb[ch] if ch != "z" else inf, len(b) - cb[ch] + ca[ch] if ch != "z" else inf)
        return res 


# @lc code=end



#
# @lcpr case=start
# "aba"\n"caa"\n
# @lcpr case=end

# @lcpr case=start
# "dabadd"\n"cda"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"\n
# @lcpr case=end

# @lcpr case=start
# "d"\n"c"\n
# @lcpr case=end
#

