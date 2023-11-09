#
# @lc app=leetcode.cn id=1642 lang=python3
# @lcpr version=21917
#
# [1642] 可以到达的最远建筑
#
# https://leetcode.cn/problems/furthest-building-you-can-reach/description/
#
# algorithms
# Medium (45.39%)
# Likes:    126
# Dislikes: 0
# Total Accepted:    11.1K
# Total Submissions: 24.5K
# Testcase Example:  '[4,2,7,6,9,14,12]\n5\n1'
#
# 给你一个整数数组 heights ，表示建筑物的高度。另有一些砖块 bricks 和梯子 ladders 。
# 
# 你从建筑物 0 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。
# 
# 当从建筑物 i 移动到建筑物 i+1（下标 从 0 开始 ）时：
# 
# 
# 如果当前建筑物的高度 大于或等于 下一建筑物的高度，则不需要梯子或砖块
# 如果当前建筑的高度 小于 下一个建筑的高度，您可以使用 一架梯子 或 (h[i+1] - h[i]) 个砖块
# 
# 如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标 从 0 开始 ）。
# 
# 
# 
# 示例 1：
# 
# 输入：heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
# 输出：4
# 解释：从建筑物 0 出发，你可以按此方案完成旅程：
# - 不使用砖块或梯子到达建筑物 1 ，因为 4 >= 2
# - 使用 5 个砖块到达建筑物 2 。你必须使用砖块或梯子，因为 2 < 7
# - 不使用砖块或梯子到达建筑物 3 ，因为 7 >= 6
# - 使用唯一的梯子到达建筑物 4 。你必须使用砖块或梯子，因为 6 < 9
# 无法越过建筑物 4 ，因为没有更多砖块或梯子。
# 
# 
# 示例 2：
# 
# 输入：heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
# 输出：7
# 
# 
# 示例 3：
# 
# 输入：heights = [14,3,19,3], bricks = 17, ladders = 0
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= heights.length <= 10^5
# 1 <= heights[i] <= 10^6
# 0 <= bricks <= 10^9
# 0 <= ladders <= heights.length
# 
# 
#
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
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
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # 
        q1 = [] # 小顶堆  
        qs = 0 
        n = len(heights)
        i = 1
        while i < n:
            if heights[i] > heights[i - 1]:
                dif = heights[i] - heights[i - 1]
                heappush(q1, dif) 
                if len(q1) > ladders:
                    qs += heappop(q1)
                if qs > bricks:
                    break               
            i += 1
        return i - 1


# @lc code=end



#
# @lcpr case=start
# [4,2,7,6,9,14,12]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [4,12,2,7,3,18,20,3,19]\n10\n2\n
# @lcpr case=end

# @lcpr case=start
# [14,3,19,3]\n17\n0\n
# @lcpr case=end

#

