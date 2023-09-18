#
# @lc app=leetcode.cn id=873 lang=python3
# @lcpr version=21913
#
# [873] 最长的斐波那契子序列的长度
#
# https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/description/
#
# algorithms
# Medium (56.23%)
# Likes:    375
# Dislikes: 0
# Total Accepted:    50.6K
# Total Submissions: 90.1K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# 如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
# 
# 
# n >= 3
# 对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
# 
# 
# 给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
# 
# （回想一下，子序列是从原序列 arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8]
# 是 [3, 4, 5, 6, 7, 8] 的一个子序列）
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入: arr = [1,2,3,4,5,6,7,8]
# 输出: 5
# 解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。
# 
# 
# 示例 2：
# 
# 输入: arr = [1,3,7,11,12,14,18]
# 输出: 3
# 解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= arr.length <= 1000
# 
# 1 <= arr[i] < arr[i + 1] <= 10^9
# 
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
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        mp = {}
        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i - 1, -1, -1):
                k = arr[i] - arr[j]
                if k < arr[j] and k in mp:
                    dp[i][j] = max(dp[i][j], dp[j][mp[k]] + 1)
            res = max(res, max(dp[i]))
            
            mp[arr[i]] = i 
        # print(dp)
        return res if res > 2 else 0
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,7,11,12,14,18]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,5,6,7,8,11,13,14,15,21,22,34]
# @lcpr case=end

#

