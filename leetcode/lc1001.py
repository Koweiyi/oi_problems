#
# @lc app=leetcode.cn id=1001 lang=python3
# @lcpr version=21913
#
# [1001] 网格照明
#
# https://leetcode.cn/problems/grid-illumination/description/
#
# algorithms
# Hard (44.89%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    19.6K
# Total Submissions: 43.5K
# Testcase Example:  '5\n[[0,0],[4,4]]\n[[1,1],[1,0]]'
#
# 在大小为 n x n 的网格 grid 上，每个单元格都有一盏灯，最初灯都处于 关闭 状态。
# 
# 给你一个由灯的位置组成的二维数组 lamps ，其中 lamps[i] = [rowi, coli] 表示 打开 位于 grid[rowi][coli]
# 的灯。即便同一盏灯可能在 lamps 中多次列出，不会影响这盏灯处于 打开 状态。
# 
# 当一盏灯处于打开状态，它将会照亮 自身所在单元格 以及同一 行 、同一 列 和两条 对角线 上的 所有其他单元格 。
# 
# 另给你一个二维数组 queries ，其中 queries[j] = [rowj, colj] 。对于第 j 个查询，如果单元格 [rowj, colj]
# 是被照亮的，则查询结果为 1 ，否则为 0 。在第 j 次查询之后 [按照查询的顺序] ，关闭 位于单元格 grid[rowj][colj] 上及相邻 8
# 个方向上（与单元格 grid[rowi][coli] 共享角或边）的任何灯。
# 
# 返回一个整数数组 ans 作为答案， ans[j] 应等于第 j 次查询 queries[j] 的结果，1 表示照亮，0 表示未照亮。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
# 输出：[1,0]
# 解释：最初所有灯都是关闭的。在执行查询之前，打开位于 [0, 0] 和 [4, 4] 的灯。第 0 次查询检查 grid[1][1]
# 是否被照亮（蓝色方框）。该单元格被照亮，所以 ans[0] = 1 。然后，关闭红色方框中的所有灯。
# 
# 第 1 次查询检查 grid[1][0] 是否被照亮（蓝色方框）。该单元格没有被照亮，所以 ans[1] = 0 。然后，关闭红色矩形中的所有灯。
# 
# 
# 
# 示例 2：
# 
# 输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
# 输出：[1,1]
# 
# 
# 示例 3：
# 
# 输入：n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
# 输出：[1,1,0]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^9
# 0 <= lamps.length <= 20000
# 0 <= queries.length <= 20000
# lamps[i].length == 2
# 0 <= rowi, coli < n
# queries[j].length == 2
# 0 <= rowj, colj < n
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter, defaultdict
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lap = set((x, y) for x, y in lamps)
        col = Counter()
        row = Counter()
        diff = Counter()
        s = Counter()
        for x, y in lap:
            row[x] += 1
            col[y] += 1
            diff[x - y] += 1
            s[x + y] += 1
        res = []
        for x, y in queries:
            if row[x] or col[y] or diff[x - y] or s[x + y]:
                res.append(1)
            else:
                res.append(0)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (x + i, y + j) in lap:
                        row[x + i] -= 1
                        col[y + j] -= 1
                        diff[x + i - (y + j)] -= 1
                        s[x + i + y + j] -= 1
                        lap.remove((x + i, y + j))
        return res 
# @lc code=end



#
# @lcpr case=start
# 5\n[[0,0],[4,4]]\n[[1,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,0],[4,4]]\n[[1,1],[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,0],[0,4]]\n[[0,4],[0,1],[1,4]]\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[2,5],[4,2],[0,3],[0,5],[1,4],[4,2],[3,3],[1,0]]\n[[4,3],[3,1],[5,3],[0,5],[4,4],[3,3]]\n
# @lcpr case=end
#

