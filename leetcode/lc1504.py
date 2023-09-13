#
# @lc app=leetcode.cn id=1504 lang=python3
# @lcpr version=21913
#
# [1504] 统计全 1 子矩形
#
# https://leetcode.cn/problems/count-submatrices-with-all-ones/description/
#
# algorithms
# Medium (62.55%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    12.2K
# Total Submissions: 19.5K
# Testcase Example:  '[[1,0,1],[1,1,0],[1,1,0]]'
#
# 给你一个 m x n 的二进制矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：mat = [[1,0,1],[1,1,0],[1,1,0]]
# 输出：13
# 解释：
# 有 6 个 1x1 的矩形。
# 有 2 个 1x2 的矩形。
# 有 3 个 2x1 的矩形。
# 有 1 个 2x2 的矩形。
# 有 1 个 3x1 的矩形。
# 矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
# 输出：24
# 解释：
# 有 8 个 1x1 的子矩形。
# 有 5 个 1x2 的子矩形。
# 有 2 个 1x3 的子矩形。
# 有 4 个 2x1 的子矩形。
# 有 2 个 2x2 的子矩形。
# 有 2 个 3x1 的子矩形。
# 有 1 个 3x2 的子矩形。
# 矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= m, n <= 150
# mat[i][j] 仅包含 0 或 1
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
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)] 
        for i in range(m):
            for j in range(n):
                s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + mat[i][j]
        left_len = [[0] * (n) for _ in range(m)]
        for i in range(m):
            left_len[i][0] = mat[i][0]
        for i in range(m):
            for j in range(1, n):
                left_len[i][j] = left_len[i][j - 1]  + 1 if mat[i][j] else 0 
        res = 0 
        for i in range(m):
            for j in range(n):
                k = i 
                min_len = left_len[i][j]
                while k >= 0 and left_len[k][j]:
                    min_len = min(min_len, left_len[k][j])
                    res += min_len
                    k -= 1 
        return res 
        
# @lc code=end



#
# @lcpr case=start
# [[1,0,1],[1,1,0],[1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,1,0],[0,1,1,1],[1,1,1,0]]\n
# @lcpr case=end

#

