#
# @lc app=leetcode.cn id=858 lang=python3
# @lcpr version=21913
#
# [858] 镜面反射
#
# https://leetcode.cn/problems/mirror-reflection/description/
#
# algorithms
# Medium (57.49%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 8.8K
# Testcase Example:  '2\n1'
#
# 有一个特殊的正方形房间，每面墙上都有一面镜子。除西南角以外，每个角落都放有一个接受器，编号为 0， 1，以及 2。
# 
# 正方形房间的墙壁长度为 p，一束激光从西南角射出，首先会与东墙相遇，入射点到接收器 0 的距离为 q 。
# 
# 返回光线最先遇到的接收器的编号（保证光线最终会遇到一个接收器）。
# 
# 
# 示例 1：
# 
# 输入：p = 2, q = 1
# 输出：2
# 解释：这条光线在第一次被反射回左边的墙时就遇到了接收器 2 。
# 
# 
# 示例 2：
# 
# 输入：p = 3, q = 1
# 输入：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= q <= p <= 1000
# 
# 
#
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate
from functools import cache
from math import gcd
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
    def mirrorReflection(self, p: int, q: int) -> int:

        # 难道是暴力搜索？？？ 
        # 只有 1000 * 4 个点 ，，，，每个点两种方向
        """
        终点有   (0, p, 1)
                (1, 0, -1)
                (1, p, 1)
        """
        # 暴力搜索
        # mp = { 
        #     (0, p, 1) : 2,
        #     (1, 0, -1): 0,
        #     (1, p, 1) : 1}
        # st = (0, 0, 1)
        # while st not in mp:
        #     a = st[0] ^ 1 
        #     b = st[1] + st[2] * q 
        #     c = st[2]
        #     if b > p:
        #         b = p - (b - p)
        #         c = -c
        #     elif b < 0:
        #         c = -c 
        #         b = -b 
        #     st = (a, b, c)
        # return mp[st]
    

        # 数学解法
        k = p // gcd(p, q)
        if k & 1 == 0:
            return 2 
        return k * q // p & 1
            


# @lc code=end



#
# @lcpr case=start
# 2\n1\n
# @lcpr case=end

#

