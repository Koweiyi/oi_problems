#
# @lc app=leetcode.cn id=754 lang=python3
# @lcpr version=21913
#
# [754] 到达终点数字
#
# https://leetcode.cn/problems/reach-a-number/description/
#
# algorithms
# Medium (51.44%)
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
from math import sqrt
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def reachNumber(self, target: int) -> int:
        if target < 0:
            target = - target 
        l = 0
        r = target + 1
        while l + 1 < r:
            mid = (l + r) // 2 
            if mid * (mid + 1) // 2 >= target:
                r = mid 
            else:
                l = mid
        if r * (r + 1) == 2 * target:
            return r 
        if (r * (r + 1) // 2 - target) & 1:
            if ((r + 1) * (r + 2) // 2 - target) & 1:
                return r + 2
            return r + 1
        return r
     
    
        
# @lc code=end



#
# @lcpr case=start
# 46534543\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 6\n
# @lcpr case=end
# @lcpr case=start
# 7\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end
# @lcpr case=start
# 9\n
# @lcpr case=end
#

