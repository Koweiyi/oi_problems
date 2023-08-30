#
# @lc app=leetcode.cn id=85 lang=python3
# @lcpr version=21913
#
# [85] 最大矩形
#
# https://leetcode.cn/problems/maximal-rectangle/description/
#
# algorithms
# Hard (54.78%)
# Likes:    1569
# Dislikes: 0
# Total Accepted:    182.3K
# Total Submissions: 332.8K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 
# 
# 示例 1：
# 
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
# 
# 
# 示例 2：
# 
# 输入：matrix = []
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：matrix = [["0"]]
# 输出：0
# 
# 
# 示例 4：
# 
# 输入：matrix = [["1"]]
# 输出：1
# 
# 
# 示例 5：
# 
# 输入：matrix = [["0","0"]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# rows == matrix.length
# cols == matrix[0].length
# 1 <= row, cols <= 200
# matrix[i][j] 为 '0' 或 '1'
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
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0]) 
        s = [[0] * (n + 1) for _ in range(m + 1)]

        # for j in range(n + 1): 
        #     s[0][j] = inf
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    s[i + 1][j + 1] = 0
                else:
                    s[i + 1][j + 1] = s[i + 1][j] + int(matrix[i][j] == '1') 
        res = 0
        for i in range(m):
            for j in range(n):
                k = i
                cur_min = s[i + 1][j + 1]
                while k >= 0:
                    cur_min = min(s[k + 1][j + 1], cur_min)
                    res = max(res, cur_min * (i - k + 1))
                    # if res == 8:
                        # print(i, j, cur_min)
                    k -= 1
        return res  

# @lc code=end



#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end



# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0","0"]]\n
# @lcpr case=end

#

