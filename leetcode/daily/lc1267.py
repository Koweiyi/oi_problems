#
# @lc app=leetcode.cn id=1267 lang=python3
# @lcpr version=21913
#
# [1267] 统计参与通信的服务器
#
# https://leetcode.cn/problems/count-servers-that-communicate/description/
#
# algorithms
# Medium (61.96%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    25K
# Total Submissions: 36.7K
# Testcase Example:  '[[1,0],[0,1]]'
#
# 这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，1 表示单元格上有服务器，0 表示没有。
# 
# 如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。
# 
# 请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：grid = [[1,0],[0,1]]
# 输出：0
# 解释：没有一台服务器能与其他服务器进行通信。
# 
# 示例 2：
# 
# 
# 
# 输入：grid = [[1,0],[1,1]]
# 输出：3
# 解释：所有这些服务器都至少可以与一台别的服务器进行通信。
# 
# 
# 示例 3：
# 
# 
# 
# 输入：grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# 输出：4
# 解释：第一行的两台服务器互相通信，第三列的两台服务器互相通信，但右下角的服务器无法与其他服务器通信。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1
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
    def countServers(self, grid: List[List[int]]) -> int:

        sumrow = [sum(row) for row in grid]
        sumcol = [sum(col) for col in zip(*grid)]
        res = sum(x for x in sumrow if x > 1) + sum(x for x in sumcol if x > 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if sumrow[i] > 1 and sumcol[j] > 1 and grid[i][j]:
                    res -= 1
        return res 
# @lc code=end



#
# @lcpr case=start
# [[1,0],[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0],[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]\n
# @lcpr case=end

#

