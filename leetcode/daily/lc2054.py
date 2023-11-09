#
# @lc app=leetcode.cn id=2054 lang=python3
# @lcpr version=21913
#
# [2054] 两个最好的不重叠活动
#
# https://leetcode.cn/problems/two-best-non-overlapping-events/description/
#
# algorithms
# Medium (38.92%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    5K
# Total Submissions: 12.8K
# Testcase Example:  '[[1,3,2],[4,5,2],[2,4,3]]'
#
# 给你一个下标从 0 开始的二维整数数组 events ，其中 events[i] = [startTimei, endTimei, valuei] 。第
# i 个活动开始于 startTimei ，结束于 endTimei ，如果你参加这个活动，那么你可以得到价值 valuei 。你 最多 可以参加
# 两个时间不重叠 活动，使得它们的价值之和 最大 。
# 
# 请你返回价值之和的 最大值 。
# 
# 注意，活动的开始时间和结束时间是 包括
# 在活动时间内的，也就是说，你不能参加两个活动且它们之一的开始时间等于另一个活动的结束时间。更具体的，如果你参加一个活动，且结束时间为 t
# ，那么下一个活动必须在 t + 1 或之后的时间开始。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 输入：events = [[1,3,2],[4,5,2],[2,4,3]]
# 输出：4
# 解释：选择绿色的活动 0 和 1 ，价值之和为 2 + 2 = 4 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：events = [[1,3,2],[4,5,2],[1,5,5]]
# 输出：5
# 解释：选择活动 2 ，价值和为 5 。
# 
# 
# 示例 3：
# 
# 
# 
# 输入：events = [[1,5,3],[1,5,1],[6,6,5]]
# 输出：8
# 解释：选择活动 0 和 2 ，价值之和为 3 + 5 = 8 。
# 
# 
# 
# 提示：
# 
# 
# 2 <= events.length <= 10^5
# events[i].length == 3
# 1 <= startTimei <= endTimei <= 10^9
# 1 <= valuei <= 10^6
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
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        dp = [[0] * 2 for _ in range(n + 1)]
        # 按照结束时间排序
        events.sort(key=lambda x:(x[1]))
        for i in range(n):
            dp[i + 1][0] = max(dp[i][0], events[i][2])
            l, r = -1, i
            while l + 1 < r:
                mid = (l + r) >> 1 
                if events[mid][1] >= events[i][0]:
                    r = mid 
                else:
                    l = mid
            dp[i + 1][1] = max(dp[i][1], dp[l + 1][0] + events[i][2])
        return max(dp[n])
# @lc code=end



#
# @lcpr case=start
# [[1,3,2],[4,5,2],[2,4,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,2],[4,5,2],[1,5,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,5,3],[1,5,1],[6,6,5]]\n
# @lcpr case=end

#

