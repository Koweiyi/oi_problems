#
# @lc app=leetcode.cn id=1727 lang=python3
# @lcpr version=21914
#
# [1727] 重新排列后的最大子矩阵
#
# https://leetcode.cn/problems/largest-submatrix-with-rearrangements/description/
#
# algorithms
# Medium (59.47%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    5K
# Total Submissions: 8.4K
# Testcase Example:  '[[0,0,1],[1,1,1],[1,0,1]]'
#
# 给你一个二进制矩阵 matrix ，它的大小为 m x n ，你可以将 matrix 中的 列 按任意顺序重新排列。
# 
# 请你返回最优方案下将 matrix 重新排列后，全是 1 的子矩阵面积。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：matrix = [[0,0,1],[1,1,1],[1,0,1]]
# 输出：4
# 解释：你可以按照上图方式重新排列矩阵的每一列。
# 最大的全 1 子矩阵是上图中加粗的部分，面积为 4 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：matrix = [[1,0,1,0,1]]
# 输出：3
# 解释：你可以按照上图方式重新排列矩阵的每一列。
# 最大的全 1 子矩阵是上图中加粗的部分，面积为 3 。
# 
# 
# 示例 3：
# 
# 输入：matrix = [[1,1,0],[1,0,1]]
# 输出：2
# 解释：由于你只能整列整列重新排布，所以没有比面积为 2 更大的全 1 子矩形。
# 
# 示例 4：
# 
# 输入：matrix = [[0,0],[0,0]]
# 输出：0
# 解释：由于矩阵中没有 1 ，没有任何全 1 的子矩阵，所以面积为 0 。
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 10^5
# matrix[i][j] 要么是 0 ，要么是 1 。
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
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] and i :
                    matrix[i][j] += matrix[i - 1][j]
        res = 0
        for i in range(m):
            matrix[i].sort()
            mn = inf
            for j in range(n - 1, -1, -1):
                mn = min(matrix[i][j], mn)
                res = max(res, mn * (n - j))
        return res 
# @lc code=end



#
# @lcpr case=start
# [[0,0,1],[1,1,1],[1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,0],[1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0],[0,0]]\n
# @lcpr case=end

#

