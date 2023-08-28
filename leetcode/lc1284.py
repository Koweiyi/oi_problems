#
# @lc app=leetcode.cn id=1284 lang=python3
# @lcpr version=21913
#
# [1284] 转化为全零矩阵的最少反转次数
#
# https://leetcode.cn/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/description/
#
# algorithms
# Hard (68.32%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 6.1K
# Testcase Example:  '[[0,0],[0,1]]'
#
# 给你一个 m x n 的二进制矩阵 mat。每一步，你可以选择一个单元格并将它反转（反转表示 0 变 1 ，1 变 0
# ）。如果存在和它相邻的单元格，那么这些相邻的单元格也会被反转。相邻的两个单元格共享同一条边。
# 
# 请你返回将矩阵 mat 转化为全零矩阵的最少反转次数，如果无法转化为全零矩阵，请返回 -1 。
# 
# 二进制矩阵 的每一个格子要么是 0 要么是 1 。
# 
# 全零矩阵 是所有格子都为 0 的矩阵。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：mat = [[0,0],[0,1]]
# 输出：3
# 解释：一个可能的解是反转 (1, 0)，然后 (0, 1) ，最后是 (1, 1) 。
# 
# 
# 示例 2：
# 
# 输入：mat = [[0]]
# 输出：0
# 解释：给出的矩阵是全零矩阵，所以你不需要改变它。
# 
# 
# 示例 3：
# 
# 输入：mat = [[1,0,0],[1,0,0]]
# 输出：-1
# 解释：该矩阵无法转变成全零矩阵
# 
# 
# 
# 
# 提示：
# 
# 
# m == mat.length
# n == mat[0].length
# 1 <= m <= 3
# 1 <= n <= 3
# mat[i][j] 是 0 或 1 。
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
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        res = m * n + 1
        def dfs(id: int, cnt: int):
            nonlocal res 
            i, j = id // n, id % n   
            if id == m * n:
                if sum(sum(row) for row in mat) == 0:
                    res = min(res, cnt)
                return 
            dfs(id + 1, cnt)
            mat[i][j] ^= 1
            for nx, ny in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if 0 <= nx < m and 0 <= ny < n:
                    mat[nx][ny] ^= 1 
            dfs(id + 1, cnt + 1)
            mat[i][j] ^= 1
            for nx, ny in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if 0 <= nx < m and 0 <= ny < n:
                    mat[nx][ny] ^= 1 
        dfs(0, 0)

        return -1 if res == m*n + 1 else res 

# @lc code=end



#
# @lcpr case=start
# [[0,0],[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0],[1,0,0]]\n
# @lcpr case=end

#

