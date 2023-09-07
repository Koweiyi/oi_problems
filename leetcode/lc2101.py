#
# @lc app=leetcode.cn id=2101 lang=python3
# @lcpr version=21913
#
# [2101] 引爆最多的炸弹
#
# https://leetcode.cn/problems/detonate-the-maximum-bombs/description/
#
# algorithms
# Medium (39.48%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 15.5K
# Testcase Example:  '[[2,1,3],[6,1,4]]'
#
# 给你一个炸弹列表。一个炸弹的 爆炸范围 定义为以炸弹为圆心的一个圆。
# 
# 炸弹用一个下标从 0 开始的二维整数数组 bombs 表示，其中 bombs[i] = [xi, yi, ri] 。xi 和 yi 表示第 i 个炸弹的
# X 和 Y 坐标，ri 表示爆炸范围的 半径 。
# 
# 你需要选择引爆 一个 炸弹。当这个炸弹被引爆时，所有 在它爆炸范围内的炸弹都会被引爆，这些炸弹会进一步将它们爆炸范围内的其他炸弹引爆。
# 
# 给你数组 bombs ，请你返回在引爆 一个 炸弹的前提下，最多 能引爆的炸弹数目。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：bombs = [[2,1,3],[6,1,4]]
# 输出：2
# 解释：
# 上图展示了 2 个炸弹的位置和爆炸范围。
# 如果我们引爆左边的炸弹，右边的炸弹不会被影响。
# 但如果我们引爆右边的炸弹，两个炸弹都会爆炸。
# 所以最多能引爆的炸弹数目是 max(1, 2) = 2 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：bombs = [[1,1,5],[10,10,5]]
# 输出：1
# 解释：
# 引爆任意一个炸弹都不会引爆另一个炸弹。所以最多能引爆的炸弹数目为 1 。
# 
# 
# 示例 3：
# 
# 
# 
# 输入：bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
# 输出：5
# 解释：
# 最佳引爆炸弹为炸弹 0 ，因为：
# - 炸弹 0 引爆炸弹 1 和 2 。红色圆表示炸弹 0 的爆炸范围。
# - 炸弹 2 引爆炸弹 3 。蓝色圆表示炸弹 2 的爆炸范围。
# - 炸弹 3 引爆炸弹 4 。绿色圆表示炸弹 3 的爆炸范围。
# 所以总共有 5 个炸弹被引爆。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= bombs.length <= 100
# bombs[i].length == 3
# 1 <= xi, yi, ri <= 10^5
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
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # 好像是有向边， 不能用并查集  。。。。。 
        # 麻了 
        n = len(bombs)
        g = [[] for _ in range(n)]

        def check(i, j):
            return abs(bombs[i][0] - bombs[j][0]) ** 2 + abs(bombs[i][1] - bombs[j][1]) ** 2 <= bombs[i][2] ** 2 
        for i in range(n):
            for j in range(n):
                if i != j and check(i, j):
                    g[i].append(j)
                    
        def dfs(x: int):
            for y in g[x]:
                if y not in s:
                    s.add(y)
                    dfs(y)
        res = 0 
        for i in range(n):
            s = set()
            s.add(i)
            dfs(i)
            res = max(res, len(s))
        return res 
        
        
# @lc code=end



#
# @lcpr case=start
# [[2,1,3],[6,1,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,5],[10,10,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]\n
# @lcpr case=end

#

