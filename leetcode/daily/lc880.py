#
# @lc app=leetcode.cn id=880 lang=python3
# @lcpr version=21917
#
# [880] 索引处的解码字符串
#
# https://leetcode.cn/problems/decoded-string-at-index/description/
#
# algorithms
# Medium (27.20%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    9K
# Total Submissions: 33K
# Testcase Example:  '"leet2code3"\n10'
#
# 给定一个编码字符串 S。请你找出 解码字符串 并将其写入磁带。解码时，从编码字符串中 每次读取一个字符 ，并采取以下步骤：
# 
# 
# 如果所读的字符是字母，则将该字母写在磁带上。
# 如果所读的字符是数字（例如 d），则整个当前磁带总共会被重复写 d-1 次。
# 
# 
# 现在，对于给定的编码字符串 S 和索引 K，查找并返回解码字符串中的第 K 个字母。
# 
# 
# 
# 示例 1：
# 
# 输入：S = "leet2code3", K = 10
# 输出："o"
# 解释：
# 解码后的字符串为 "leetleetcodeleetleetcodeleetleetcode"。
# 字符串中的第 10 个字母是 "o"。
# 
# 
# 示例 2：
# 
# 输入：S = "ha22", K = 5
# 输出："h"
# 解释：
# 解码后的字符串为 "hahahaha"。第 5 个字母是 "h"。
# 
# 
# 示例 3：
# 
# 输入：S = "a2345678999999999999999", K = 1
# 输出："a"
# 解释：
# 解码后的字符串为 "a" 重复 8301530446056247680 次。第 1 个字母是 "a"。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= S.length <= 100
# S 只包含小写字母与数字 2 到 9 。
# S 以字母开头。
# 1 <= K <= 10^9
# 题目保证 K 小于或等于解码字符串的长度。
# 解码后的字符串保证少于 2^63 个字母。
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
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = len(s) 
        cur = 0 
        for i in range(n):
            if s[i].isdigit():
                d = int(s[i])
                if cur * d >= k:
                    return self.decodeAtIndex(s[:i], k % cur + cur * int(k % cur == 0))
                cur *= d 
            else:
                if cur + 1 == k:
                    return s[i]
                cur += 1 
        return s[-1]
# @lc code=end



#
# @lcpr case=start
# "leet2code3"\n10\n
# @lcpr case=end

# @lcpr case=start
# "ha22"\n5\n
# @lcpr case=end

# @lcpr case=start
# "a2345678999999999999999"\n1\n
# @lcpr case=end

#

