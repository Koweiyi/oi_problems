#
# @lc app=leetcode.cn id=924 lang=python3
# @lcpr version=21913
#
# [924] 尽量减少恶意软件的传播
#
# https://leetcode.cn/problems/minimize-malware-spread/description/
#
# algorithms
# Hard (35.80%)
# Likes:    88
# Dislikes: 0
# Total Accepted:    10.4K
# Total Submissions: 28.9K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]\n[0,1]'
#
# 给出了一个由 n 个节点组成的网络，用 n × n 个邻接矩阵图 graph 表示。在节点网络中，当 graph[i][j] = 1 时，表示节点 i
# 能够直接连接到另一个节点 j。 
# 
# 一些节点 initial
# 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。
# 
# 假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。
# 
# 如果从 initial 中移除某一节点能够最小化 M(initial)， 返回该节点。如果有多个节点满足条件，就返回索引最小的节点。
# 
# 请注意，如果某个节点已从受感染节点的列表 initial 中删除，它以后仍有可能因恶意软件传播而受到感染。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
# 输出：0
# 
# 
# 示例 2：
# 
# 输入：graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 
# n == graph.length
# n == graph[i].length
# 2 <= n <= 300
# graph[i][j] == 0 或 1.
# graph[i][j] == graph[j][i]
# graph[i][i] == 1
# 1 <= initial.length <= n
# 0 <= initial[i] <= n - 1
# initial 中所有整数均不重复
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
    def minMalwareSpread(self, g: List[List[int]], initial: List[int]) -> int:
        
        n = len(g)
        s = set(initial)
        mn = inf 
        res = -1
        for x in sorted(initial):
            s.remove(x) 
            vis = set()
            def dfs(i: int):
                for j in range(n):
                    if i != j and g[i][j] and j not in vis:
                        vis.add(j)
                        dfs(j)
            for i in range(n):
                if i in s and i not in vis:
                    vis.add(i)
                    dfs(i)
            if len(vis) < mn:
                mn = len(vis)
                res = x
            s.add(x)
        return res  
# @lc code=end



#
# @lcpr case=start
# [[1,1,0],[1,1,0],[0,0,1]]\n[0,1]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0],[0,1,0],[0,0,1]]\n[0,2]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1],[1,1,1],[1,1,1]]\n[1,2]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,1,1]]\n[3,1]\n
# @lcpr case=end
#

