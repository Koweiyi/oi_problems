#
# @lc app=leetcode.cn id=815 lang=python3
# @lcpr version=21917
#
# [815] 公交路线
#
# https://leetcode.cn/problems/bus-routes/description/
#
# algorithms
# Hard (44.35%)
# Likes:    355
# Dislikes: 0
# Total Accepted:    38.3K
# Total Submissions: 86.5K
# Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
#
# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
# 
# 
# 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1
# -> ... 这样的车站路线行驶。
# 
# 
# 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
# 
# 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# 输出：2
# 解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。 
# 
# 
# 示例 2：
# 
# 输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 10^5
# routes[i] 中的所有值 互不相同
# sum(routes[i].length) <= 10^5
# 0 <= routes[i][j] < 10^6
# 0 <= source, target < 10^6
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
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0
        n = len(routes)
        g = [[] for _ in range(n)]
        mp = defaultdict(list)
        s = []
        st = set()
        ed = set()
        for i, r in enumerate(routes):
            for x in r :
                if x == source:
                    st.add(i)
                if x == target:
                    ed.add(i)
                for j in mp[x]:
                    g[i].append(j)
                    g[j].append(i)
                mp[x].append(i)
        
        q = [x for x in range(n) if x in st]
        vis = [False] * n
        for x in q:
            vis[x] = True 
        res = 1
        while q:
            tmp = q
            q = []
            for x in tmp:
                if x in ed:
                    return res 
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True 
                        q.append(y)
            res += 1 
        return -1 
                


        
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,7],[3,6,7]]\n1\n6\n
# @lcpr case=end

# @lcpr case=start
# [[7,12],[4,5,15],[6],[15,19],[9,12,13]]\n15\n12\n
# @lcpr case=end

# @lcpr case=start
# [[1,7],[3,5]]\n5\n5
# @lcpr case=end

# @lcpr case=start
# [[2],[2,8]]\n8\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[5,6],[4,5],[3,4],[2,3]]\n1\n6\n
# @lcpr case=end
#

