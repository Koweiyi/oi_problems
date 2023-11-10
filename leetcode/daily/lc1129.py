#
# @lc app=leetcode.cn id=1129 lang=python3
# @lcpr version=21913
#
# [1129] 颜色交替的最短路径
#
# https://leetcode.cn/problems/shortest-path-with-alternating-colors/description/
#
# algorithms
# Medium (48.56%)
# Likes:    284
# Dislikes: 0
# Total Accepted:    29.2K
# Total Submissions: 60.2K
# Testcase Example:  '3\n[[0,1],[1,2]]\n[]'
#
# 给定一个整数 n，即有向图中的节点数，其中节点标记为 0 到 n - 1。图中的每条边为红色或者蓝色，并且可能存在自环或平行边。
# 
# 给定两个数组 redEdges 和 blueEdges，其中：
# 
# 
# redEdges[i] = [ai, bi] 表示图中存在一条从节点 ai 到节点 bi 的红色有向边，
# blueEdges[j] = [uj, vj] 表示图中存在一条从节点 uj 到节点 vj 的蓝色有向边。
# 
# 
# 返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X
# 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# 输出：[0,1,-1]
# 
# 
# 示例 2：
# 
# 输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# 输出：[0,1,-1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 100
# 0 <= redEdges.length, blueEdges.length <= 400
# redEdges[i].length == blueEdges[j].length == 2
# 0 <= ai, bi, uj, vj < n
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter, defaultdict, deque
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1] * n
        q = [(0, 1), (0, -1)]
        s = set(q)
        gr = [[] for _ in range(n)]
        gb = [[] for _ in range(n)]
        for x, y in redEdges:
            gr[x].append(y)
        for x, y in blueEdges:
            gb[x].append(y)
       


        step = 0
        while q:
            tmp = q 
            q = []
            for id, dir in tmp:
                if res[id] == -1:
                    res[id] = step 
                if dir == 1:
                    for y in gr[id]:
                        if (y, -1) not in s:
                            s.add((y, -1))
                            q.append((y, -1))
                else:
                    for y in gb[id]:
                        if (y, 1) not in s:
                            s.add((y, 1))
                            q.append((y, 1))
            step += 1
        return res 



# @lc code=end



#
# @lcpr case=start
# 3\n[[0,1],[1,2]]\n[]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1]]\n[[2,1]]\n
# @lcpr case=end

#

