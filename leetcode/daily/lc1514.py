#
# @lc app=leetcode.cn id=1514 lang=python3
# @lcpr version=21913
#
# [1514] 概率最大的路径
#
# https://leetcode.cn/problems/path-with-maximum-probability/description/
#
# algorithms
# Medium (40.95%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    20.6K
# Total Submissions: 50.2K
# Testcase Example:  '3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.2]\n0\n2'
#
# 给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，其中 edges[i] = [a, b] 表示连接节点 a 和 b
# 的一条无向边，且该边遍历成功的概率为 succProb[i] 。
# 
# 指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。
# 
# 如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0,
# end = 2
# 输出：0.25000
# 解释：从起点到终点有两条路径，其中一条的成功概率为 0.2 ，而另一条为 0.5 * 0.5 = 0.25
# 
# 
# 示例 2：
# 
# 
# 
# 输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0,
# end = 2
# 输出：0.30000
# 
# 
# 示例 3：
# 
# 
# 
# 输入：n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# 输出：0.00000
# 解释：节点 0 和 节点 2 之间不存在路径
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= n <= 10^4
# 0 <= start, end < n
# start != end
# 0 <= a, b < n
# a != b
# 0 <= succProb.length == edges.length <= 2*10^4
# 0 <= succProb[i] <= 1
# 每两个节点之间最多有一条边
# 
# 
#
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
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
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        g = [[] for _ in range(n)]
        for (x, y), p in zip(edges, succProb):
            g[x].append((y, p))
            g[y].append((x, p))
        q = [(-1, start_node)]
        vis = set()
        while q:
            p, x = heappop(q)
            if x in vis:
                continue 
            if x == end_node:
                return -p 
            vis.add(x)
            for y, py in g[x]:
                if y not in vis:
                    heappush(q, (p * py, y))
        return 0.0
            
        
# @lc code=end


#
# @lcpr case=start
# 3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.2]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.3]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1]]\n[0.5]\n0\n2\n
# @lcpr case=end

#

