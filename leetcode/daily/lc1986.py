#
# @lc app=leetcode.cn id=1986 lang=python3
# @lcpr version=21917
#
# [1986] 完成任务的最少工作时间段
#
# https://leetcode.cn/problems/minimum-number-of-work-sessions-to-finish-the-tasks/description/
#
# algorithms
# Medium (33.59%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    7.1K
# Total Submissions: 21.1K
# Testcase Example:  '[1,2,3]\n3'
#
# 你被安排了 n 个任务。任务需要花费的时间用长度为 n 的整数数组 tasks 表示，第 i 个任务需要花费 tasks[i] 小时完成。一个 工作时间段
# 中，你可以 至多 连续工作 sessionTime 个小时，然后休息一会儿。
# 
# 你需要按照如下条件完成给定任务：
# 
# 
# 如果你在某一个时间段开始一个任务，你需要在 同一个 时间段完成它。
# 完成一个任务后，你可以 立马 开始一个新的任务。
# 你可以按 任意顺序 完成任务。
# 
# 
# 给你 tasks 和 sessionTime ，请你按照上述要求，返回完成所有任务所需要的 最少 数目的 工作时间段 。
# 
# 测试数据保证 sessionTime 大于等于 tasks[i] 中的 最大值 。
# 
# 
# 
# 示例 1：
# 
# 输入：tasks = [1,2,3], sessionTime = 3
# 输出：2
# 解释：你可以在两个工作时间段内完成所有任务。
# - 第一个工作时间段：完成第一和第二个任务，花费 1 + 2 = 3 小时。
# - 第二个工作时间段：完成第三个任务，花费 3 小时。
# 
# 
# 示例 2：
# 
# 输入：tasks = [3,1,3,1,1], sessionTime = 8
# 输出：2
# 解释：你可以在两个工作时间段内完成所有任务。
# - 第一个工作时间段：完成除了最后一个任务以外的所有任务，花费 3 + 1 + 3 + 1 = 8 小时。
# - 第二个工作时间段，完成最后一个任务，花费 1 小时。
# 
# 
# 示例 3：
# 
# 输入：tasks = [1,2,3,4,5], sessionTime = 15
# 输出：1
# 解释：你可以在一个工作时间段以内完成所有任务。
# 
# 
# 
# 
# 提示：
# 
# 
# n == tasks.length
# 1 <= n <= 14
# 1 <= tasks[i] <= 10
# max(tasks[i]) <= sessionTime <= 15
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
from heapq import heappush, heappop
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        # 状压dp 
        n = len(tasks)
        sm = []
        for i in range(1 << n):
            s = 0
            for j in range(n):
                if (i >> j) & 1:
                    s += tasks[j]
            sm.append(s)

        @cache 
        def dfs(s) -> int:
            if s == 0:
                return 0
            res = inf
            sub = s
            while sub:
                if sm[sub] <= sessionTime:
                    res = min(res, 1 + dfs(s ^ sub))
                sub = (sub - 1) & s
            return res 
        return dfs((1 << n) - 1)


            





            
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,1,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n15\n
# @lcpr case=end

#

