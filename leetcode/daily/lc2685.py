#
# @lc app=leetcode.cn id=2685 lang=python3
# @lcpr version=21917
#
# [2685] 统计完全连通分量的数量
#
# https://leetcode.cn/problems/count-the-number-of-complete-components/description/
#
# algorithms
# Medium (67.92%)
# Likes:    16
# Dislikes: 0
# Total Accepted:    4.8K
# Total Submissions: 7K
# Testcase Example:  '6\n[[0,1],[0,2],[1,2],[3,4]]'
#
# 给你一个整数 n 。现有一个包含 n 个顶点的 无向 图，顶点按从 0 到 n - 1 编号。给你一个二维整数数组 edges 其中 edges[i] =
# [ai, bi] 表示顶点 ai 和 bi 之间存在一条 无向 边。
# 
# 返回图中 完全连通分量 的数量。
# 
# 如果在子图中任意两个顶点之间都存在路径，并且子图中没有任何一个顶点与子图外部的顶点共享边，则称其为 连通分量 。
# 
# 如果连通分量中每对节点之间都存在一条边，则称其为 完全连通分量 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# 输出：3
# 解释：如上图所示，可以看到此图所有分量都是完全连通分量。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# 输出：1
# 解释：包含节点 0、1 和 2 的分量是完全连通分量，因为每对节点之间都存在一条边。
# 包含节点 3 、4 和 5 的分量不是完全连通分量，因为节点 4 和 5 之间不存在边。
# 因此，在图中完全连接分量的数量是 1 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 50
# 0 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# 不存在重复的边
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
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        deg = [0] * n 
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1 
        vis = [False] * n 
        res = 0
        for i in range(n):
            cur = 0
            cnt = 0
            def dfs(x: int):
                nonlocal cur, cnt
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        cur += deg[y]
                        cnt += 1 
                        dfs(y)

            if not vis[i]:
                cur += deg[i]
                cnt += 1
                vis[i] = True 
                dfs(i)
                if cur == cnt * (cnt - 1) :
                    res += 1
        return res 
            
                
# @lc code=end 



#
# @lcpr case=start
# 6\n[[0,1],[0,2],[1,2],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[0,1],[0,2],[1,2],[3,4],[3,5]]\n
# @lcpr case=end

#

