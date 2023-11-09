#
# @lc app=leetcode.cn id=2398 lang=python3
# @lcpr version=21913
#
# [2398] 预算内的最多机器人数目
#
# https://leetcode.cn/problems/maximum-number-of-robots-within-budget/description/
#
# algorithms
# Hard (34.52%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    4.4K
# Total Submissions: 12.7K
# Testcase Example:  '[3,6,1,3,4]\n[2,1,3,4,5]\n25'
#
# 你有 n 个机器人，给你两个下标从 0 开始的整数数组 chargeTimes 和 runningCosts ，两者长度都为 n 。第 i
# 个机器人充电时间为 chargeTimes[i] 单位时间，花费 runningCosts[i] 单位时间运行。再给你一个整数 budget 。
# 
# 运行 k 个机器人 总开销 是 max(chargeTimes) + k * sum(runningCosts) ，其中 max(chargeTimes)
# 是这 k 个机器人中最大充电时间，sum(runningCosts) 是这 k 个机器人的运行时间之和。
# 
# 请你返回在 不超过 budget 的前提下，你 最多 可以 连续 运行的机器人数目为多少。
# 
# 
# 
# 示例 1：
# 
# 输入：chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
# 输出：3
# 解释：
# 可以在 budget 以内运行所有单个机器人或者连续运行 2 个机器人。
# 选择前 3 个机器人，可以得到答案最大值 3 。总开销是 max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 ，小于
# 25 。
# 可以看出无法在 budget 以内连续运行超过 3 个机器人，所以我们返回 3 。
# 
# 
# 示例 2：
# 
# 输入：chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19
# 输出：0
# 解释：即使运行任何一个单个机器人，还是会超出 budget，所以我们返回 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# chargeTimes.length == runningCosts.length == n
# 1 <= n <= 5 * 10^4
# 1 <= chargeTimes[i], runningCosts[i] <= 10^5
# 1 <= budget <= 10^15
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
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        # 两个问题 求区间最大值 倍增 + RMQ
        # 求区间和 前缀和 动态求就好了 
        # 
        

        # 倍增
        n = len(chargeTimes) 
        dp_max = [[0] * 22 for _ in range(n + 5)]
        log2 = [-1] * (n + 1)

        for i in range(1, n + 1):
            log2[i] = log2[i >> 1] + 1
        for i in range(n):
            dp_max[i][0] = chargeTimes[i]
        p = log2[n]
        for k in range(1, p + 1):
            # s + (1 << k) - 1 < n 
            for s in range(n + 1 - (1 << k)):
                dp_max[s][k] = max(dp_max[s][k - 1], dp_max[s + (1 << k)][k - 1])

        def query(l: int, r: int) -> int:
            if l > r:
                return 0
            k = log2[r - l + 1]
            return max(dp_max[l][k], dp_max[r - (1 << k) +1][k])
        

        l = 0 
        s = 0
        res = 0
        for i, x in enumerate(runningCosts):
            s += x 
            mx = query(l, i)
            while s * (i - l + 1) + mx > budget:
                s -= runningCosts[l]
                mx = query(l + 1, i)
                l += 1
            res = max(i - l + 1, res )
        return res 


# @lc code=end



#
# @lcpr case=start
# [3,6,1,3,4]\n[2,1,3,4,5]\n25\n
# @lcpr case=end

# @lcpr case=start
# [11,12,19]\n[10,8,7]\n19\n
# @lcpr case=end

#

