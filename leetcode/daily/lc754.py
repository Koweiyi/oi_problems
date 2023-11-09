#
# @lc app=leetcode.cn id=754 lang=python3
# @lcpr version=21913
#
# [754] 到达终点数字
#
# https://leetcode.cn/problems/reach-a-number/description/
#
# algorithms
# Medium (51.45%)
# Likes:    404
# Dislikes: 0
# Total Accepted:    37.1K
# Total Submissions: 72.1K
# Testcase Example:  '2'
#
# 在一根无限长的数轴上，你站在0的位置。终点在target的位置。
# 
# 你可以做一些数量的移动 numMoves :
# 
# 
# 每次你可以选择向左或向右移动。
# 第 i 次移动（从  i == 1 开始，到 i == numMoves ），在选择的方向上走 i 步。
# 
# 
# 给定整数 target ，返回 到达目标所需的 最小 移动次数(即最小 numMoves ) 。
# 
# 
# 
# 示例 1:
# 
# 输入: target = 2
# 输出: 3
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 -1 。
# 第三次移动，从 -1 到 2 。
# 
# 
# 示例 2:
# 
# 输入: target = 3
# 输出: 2
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 3 。
# 
# 
# 
# 
# 提示:
# 
# 
# -10^9 <= target <= 10^9
# target != 0
# 
# 
#
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate
from functools import cache
from math import ceil
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
    def reachNumber(self, target: int) -> int:
        # 昨晚上再宿舍电脑过了
        if target < 0:
            target = - target
        # 二分， 贪心
        # 或者直接算一个sqrt 
        l = 0
        r = target + 1
        while l + 1 < r:
            mid = (l + r) // 2 
            if mid * (mid + 1) >= target * 2:
                r = mid
            else:
                l = mid 
        if r * (r + 1) == target * 2 :
            return r 
        if (r * (r + 1) // 2 - target) & 1:
            if ((r + 1) * (r + 2) // 2 - target) & 1:
                return r + 2
            return r + 1
        return r  
        
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

