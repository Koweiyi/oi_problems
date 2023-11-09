#
# @lc app=leetcode.cn id=787 lang=python3
# @lcpr version=21913
#
# [787] K 站中转内最便宜的航班
#
# https://leetcode.cn/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (39.71%)
# Likes:    604
# Dislikes: 0
# Total Accepted:    69K
# Total Submissions: 173.7K
# Testcase Example:  '4\n[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]\n0\n3\n1'
#
# 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei]
# ，表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。
# 
# 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的
# 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。
# 
# 
# 
# 示例 1：
# 
# 输入: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# 输出: 200
# 解释: 
# 城市航班图如下
# 
# 
# 从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。
# 
# 示例 2：
# 
# 输入: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# 输出: 500
# 解释: 
# 城市航班图如下
# 
# 
# 从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 10^4
# 航班没有重复，且不存在自环
# 0 <= src, dst, k < n
# src != dst
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
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    
        g = [[] for _ in range(n)]
        for f, t, p in flights:
            g[f].append((t, p))  

        q = [(src, 0)]
        s = set(q)
        step = 0 
        res = inf 
        while q and step <= k + 1:
            tmp = q 
            q = []
            for x, dis in tmp:
                if x == dst:
                    res = min(res, dis)
                else:
                    for y, p in g[x]:
                        if p + dis < res and (y, p + dis) not in s:
                            q.append((y, p + dis))
                            s.add((y, p + dis))
            step += 1
        return res if res < inf else -1 

            

# @lc code=end



#
# @lcpr case=start
# 3\n[[0,1,100],[1,2,100],[0,2]]\n0\n2\n1\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1,100],[1,2,100],[0,2]]\n0\n2\n0\n
# @lcpr case=end

#

