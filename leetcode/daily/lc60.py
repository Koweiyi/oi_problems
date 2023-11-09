#
# @lc app=leetcode.cn id=60 lang=python3
# @lcpr version=21913
#
# [60] 排列序列
#
# https://leetcode.cn/problems/permutation-sequence/description/
#
# algorithms
# Hard (53.51%)
# Likes:    797
# Dislikes: 0
# Total Accepted:    132K
# Total Submissions: 246.7K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
# 
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 给定 n 和 k，返回第 k 个排列。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 3, k = 3
# 输出："213"
# 
# 
# 示例 2：
# 
# 输入：n = 4, k = 9
# 输出："2314"
# 
# 
# 示例 3：
# 
# 输入：n = 3, k = 1
# 输出："123"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 9
# 1 <= k <= n!
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
    def getPermutation(self, n: int, k: int) -> str:
        
        res = []
        used = [False] * (n + 1)

        fac = [1] * (n + 1)
        for i in range(1, n + 1):
            fac[i] = fac[i - 1] * i 
        def dfs(i: int, k:int) :
            if i == n:
                return 
            cnt = fac[n - i - 1]
            for j in range(1, n + 1):
                if not used[j]:
                    if k > cnt:
                        k -= cnt
                    else:
                        res.append(j)
                        used[j] = True
                        dfs(i + 1, k)
                        break 
        dfs(0, k)
        return "".join(map(str, res))
# @lc code=end



#
# @lcpr case=start
# 3\n3\n
# @lcpr case=end

# @lcpr case=start
# 4\n9\n
# @lcpr case=end

# @lcpr case=start
# 3\n1\n
# @lcpr case=end

#

