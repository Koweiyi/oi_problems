#
# @lc app=leetcode.cn id=802 lang=python3
# @lcpr version=21917
#
# [802] 找到最终的安全状态
#
# https://leetcode.cn/problems/find-eventual-safe-states/description/
#
# algorithms
# Medium (59.16%)
# Likes:    412
# Dislikes: 0
# Total Accepted:    46.5K
# Total Submissions: 78.6K
# Testcase Example:  '[[1,2],[2,3],[5],[0],[5],[],[]]'
#
# 有一个有 n 个节点的有向图，节点按 0 到 n - 1 编号。图由一个 索引从 0 开始 的 2D 整数数组 graph表示， graph[i]是与节点
# i 相邻的节点的整数数组，这意味着从节点 i 到 graph[i]中的每个节点都有一条边。
# 
# 如果一个节点没有连出的有向边，则该节点是 终端节点 。如果从该节点开始的所有可能路径都通向 终端节点 ，则该节点为 安全节点 。
# 
# 返回一个由图中所有 安全节点 组成的数组作为答案。答案数组中的元素应当按 升序 排列。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# 输出：[2,4,5,6]
# 解释：示意图如上。
# 节点 5 和节点 6 是终端节点，因为它们都没有出边。
# 从节点 2、4、5 和 6 开始的所有路径都指向节点 5 或 6 。
# 
# 
# 示例 2：
# 
# 输入：graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# 输出：[4]
# 解释:
# 只有节点 4 是终端节点，从节点 4 开始的所有路径都通向节点 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == graph.length
# 1 <= n <= 10^4
# 0 <= graph[i].length <= n
# 0 <= graph[i][j] <= n - 1
# graph[i] 按严格递增顺序排列。
# 图中可能包含自环。
# 图中边的数目在范围 [1, 4 * 10^4] 内。
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
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 找环 就好了
        # 反图 拓扑排序 
        n = len(graph)
        rg = [[] for _ in range(n)]
        id = [len(graph[x]) for x in range(n)]
        for i in range(n):
            for y in graph[i]:
                rg[y].append(i) 
        
        # 对所有非终点的点反向进行遍历，标记所有能访问到的点，剩余没访问果的就是答案 
        q = [x for x in range(n) if id[x] == 0]
        res = []
        while q:
            tmp = q 
            q = []
            for x in tmp:
                res.append(x)
                for y in rg[x]:
                    id[y] -= 1 
                    if id[y] == 0:
                        q.append(y)
        return sorted(res)
# @lc code=end



#
# @lcpr case=start
# [[1,2],[2,3],[5],[0],[5],[],[]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[1,2],[3,4],[0,4],[]]\n
# @lcpr case=end

# @lcpr case=start
# [[],[0,2,3,4],[3],[4],[]]
# @lcpr case=end

#

