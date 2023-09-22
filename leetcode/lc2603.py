#
# @lc app=leetcode.cn id=2603 lang=python3
# @lcpr version=21914
#
# [2603] 收集树中金币
#
# https://leetcode.cn/problems/collect-coins-in-a-tree/description/
#
# algorithms
# Hard (43.76%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    4.8K
# Total Submissions: 8.8K
# Testcase Example:  '[1,0,0,0,0,1]\n[[0,1],[1,2],[2,3],[3,4],[4,5]]'
#
# 给你一个 n 个节点的无向无根树，节点编号从 0 到 n - 1 。给你整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中
# edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。再给你一个长度为 n 的数组 coins ，其中 coins[i]
# 可能为 0 也可能为 1 ，1 表示节点 i 处有一个金币。
# 
# 一开始，你需要选择树中任意一个节点出发。你可以执行下述操作任意次：
# 
# 
# 收集距离当前节点距离为 2 以内的所有金币，或者
# 移动到树中一个相邻节点。
# 
# 
# 你需要收集树中所有的金币，并且回到出发节点，请你返回最少经过的边数。
# 
# 如果你多次经过一条边，每一次经过都会给答案加一。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]
# 输出：2
# 解释：从节点 2 出发，收集节点 0 处的金币，移动到节点 3 ，收集节点 5 处的金币，然后移动回节点 2 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：coins = [0,0,0,1,1,0,0,1], edges =
# [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]
# 输出：2
# 解释：从节点 0 出发，收集节点 4 和 3 处的金币，移动到节点 2 处，收集节点 7 处的金币，移动回节点 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == coins.length
# 1 <= n <= 3 * 10^4
# 0 <= coins[i] <= 1
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges 表示一棵合法的树。
# 
# 
#
from collections import Counter, defaultdict, deque
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
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [[] for _ in range(n)] 
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        le = n - 1 
        deg = [len(x) for x in g]
        q = deque([x for x in range(n) if deg[x] == 1 and not coins[x]])
        while q:
            x = q.popleft()
            le -= 1
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1 and coins[y] == 0:
                    q.append(y)
        q = deque([x for x in range(n) if deg[x] == 1 and coins[x]])
        le -= len(q)
        while q:
            x = q.popleft()
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1:
                    le -= 1
        return max(le * 2, 0)
# @lc code=end



#
# @lcpr case=start
# [1,0,0,0,0,1]\n[[0,1],[1,2],[2,3],[3,4],[4,5]]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,1,1,0,0,1]\n[[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]\n
# @lcpr case=end

#

