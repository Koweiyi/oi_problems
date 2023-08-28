#
# @lc app=leetcode.cn id=1377 lang=python3
# @lcpr version=21913
#
# [1377] T 秒后青蛙的位置
#
# https://leetcode.cn/problems/frog-position-after-t-seconds/description/
#
# algorithms
# Hard (42.64%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 44K
# Testcase Example:  '7\n[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]\n2\n4'
#
# 给你一棵由 n 个顶点组成的无向树，顶点编号从 1 到 n。青蛙从 顶点 1 开始起跳。规则如下：
# 
# 
# 在一秒内，青蛙从它所在的当前顶点跳到另一个 未访问 过的顶点（如果它们直接相连）。
# 青蛙无法跳回已经访问过的顶点。
# 如果青蛙可以跳到多个不同顶点，那么它跳到其中任意一个顶点上的机率都相同。
# 如果青蛙不能跳到任何未访问过的顶点上，那么它每次跳跃都会停留在原地。
# 
# 
# 无向树的边用数组 edges 描述，其中 edges[i] = [ai, bi] 意味着存在一条直接连通 ai 和 bi 两个顶点的边。
# 
# 返回青蛙在 t 秒后位于目标顶点 target 上的概率。与实际答案相差不超过 10^-5 的结果将被视为正确答案。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
# 输出：0.16666666666666666 
# 解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，第 1 秒 有 1/3 的概率跳到顶点 2 ，然后第 2 秒 有 1/2 的概率跳到顶点
# 4，因此青蛙在 2 秒后位于顶点 4 的概率是 1/3 * 1/2 = 1/6 = 0.16666666666666666 。 
# 
# 
# 示例 2：
# 
# 
# 
# 输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
# 输出：0.3333333333333333
# 解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，有 1/3 = 0.3333333333333333 的概率能够 1 秒 后跳到顶点 7
# 。 
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 100
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ai, bi <= n
# 1 <= t <= 50
# 1 <= target <= n
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
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if len(edges) == 0:
            return int(target == 1) 
        # 一次dfs 求到目标节点的路径长度 length 
        # 第一次dfs存一下父亲节点， 就可以反向去推了， 不需要第二次dfs
        # 如果 t != length     return 0 如果 t == target 用乘法原理算出概率 
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x) 
        g[1].append(-1)
        parent = {1:-1}
        res = 1
        def dfs(x: int, c: int, pa: int):
            nonlocal res 
            if x == target:
                if t < c or t > c and len(g[x]) != 1:
                    res = 0
                else: 
                    while pa != -1:
                        res = res * (1 / (len(g[pa]) - 1))
                        pa = parent[pa]
                return 
            parent[x] = pa 
            for y in g[x]:
                if y != pa:
                    dfs(y, c + 1, x)
        dfs(1, 0, -1)
        return res         
# @lc code=end



#
# @lcpr case=start
# 7\n[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# 7\n[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]\n1\n7\n
# @lcpr case=end


# @lcpr case=start
# 8\n[[2,1],[3,2],[4,1],[5,1],[6,4],[7,1],[8,7]]\n7\n7\n
# @lcpr case=end
#

