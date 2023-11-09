#
# @lc app=leetcode.cn id=1278 lang=python3
# @lcpr version=21917
#
# [1278] 分割回文串 III
#
# https://leetcode.cn/problems/palindrome-partitioning-iii/description/
#
# algorithms
# Hard (62.48%)
# Likes:    122
# Dislikes: 0
# Total Accepted:    6.5K
# Total Submissions: 10.4K
# Testcase Example:  '"abc"\n2'
#
# 给你一个由小写字母组成的字符串 s，和一个整数 k。
# 
# 请你按下面的要求分割字符串：
# 
# 
# 首先，你可以将 s 中的部分字符修改为其他的小写英文字母。
# 接着，你需要把 s 分割成 k 个非空且不相交的子串，并且每个子串都是回文串。
# 
# 
# 请返回以这种方式分割字符串所需修改的最少字符数。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "abc", k = 2
# 输出：1
# 解释：你可以把字符串分割成 "ab" 和 "c"，并修改 "ab" 中的 1 个字符，将它变成回文串。
# 
# 
# 示例 2：
# 
# 输入：s = "aabbc", k = 3
# 输出：0
# 解释：你可以把字符串分割成 "aa"、"bb" 和 "c"，它们都是回文串。
# 
# 示例 3：
# 
# 输入：s = "leetcode", k = 8
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= k <= s.length <= 100
# s 中只含有小写英文字母。
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
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s) 
        @cache
        def cost(i, j): # 将 s[i:j + 1] 变为回文串需要修改的次数 
            if i >= j: return 0  
            return cost(i + 1, j - 1) + int(s[i] != s[j])
        @cache
        def dfs(i, k):  # 将前 i 个字符分割为 k 个子字符串最少需要修改的次数 
            if k == 1: return cost(0, i - 1)
            return min(dfs(j, k - 1) + cost(j, i - 1) for j in range(k - 1, i))
        return dfs(len(s), k) 

            


# @lc code=end



#
# @lcpr case=start
# "abc"\n2\n
# @lcpr case=end

# @lcpr case=start
# "aabbc"\n3\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n8\n
# @lcpr case=end

#

