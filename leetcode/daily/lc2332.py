#
# @lc app=leetcode.cn id=2332 lang=python3
# @lcpr version=21913
#
# [2332] 坐上公交的最晚时间
#
# https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/description/
#
# algorithms
# Medium (24.76%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 23.5K
# Testcase Example:  '[10,20]\n[2,17,18,19]\n2'
#
# 给你一个下标从 0 开始长度为 n 的整数数组 buses ，其中 buses[i] 表示第 i 辆公交车的出发时间。同时给你一个下标从 0 开始长度为
# m 的整数数组 passengers ，其中 passengers[j] 表示第 j
# 位乘客的到达时间。所有公交车出发的时间互不相同，所有乘客到达的时间也互不相同。
# 
# 给你一个整数 capacity ，表示每辆公交车 最多 能容纳的乘客数目。
# 
# 每位乘客都会搭乘下一辆有座位的公交车。如果你在 y 时刻到达，公交在 x 时刻出发，满足 y <= x  且公交没有满，那么你可以搭乘这一辆公交。最早
# 到达的乘客优先上车。
# 
# 返回你可以搭乘公交车的最晚到达公交站时间。你 不能 跟别的乘客同时刻到达。
# 
# 注意：数组 buses 和 passengers 不一定是有序的。
# 
# 
# 
# 示例 1：
# 
# 输入：buses = [10,20], passengers = [2,17,18,19], capacity = 2
# 输出：16
# 解释：
# 第 1 辆公交车载着第 1 位乘客。
# 第 2 辆公交车载着你和第 2 位乘客。
# 注意你不能跟其他乘客同一时间到达，所以你必须在第二位乘客之前到达。
# 
# 示例 2：
# 
# 输入：buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
# 输出：20
# 解释：
# 第 1 辆公交车载着第 4 位乘客。
# 第 2 辆公交车载着第 6 位和第 2 位乘客。
# 第 3 辆公交车载着第 1 位乘客和你。
# 
# 
# 
# 
# 提示：
# 
# 
# n == buses.length
# m == passengers.length
# 1 <= n, m, capacity <= 10^5
# 2 <= buses[i], passengers[i] <= 10^9
# buses 中的元素 互不相同 。
# passengers 中的元素 互不相同 。
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
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        cur = 0 
        c = 0 
        for t in buses:
            c = capacity
            while c and cur < len(passengers) and passengers[cur] <= t:
                c -= 1 
                cur += 1 
        cur -= 1 
        res = buses[-1] if c else passengers[cur]
        while cur >= 0 and passengers[cur] == res:
            cur -= 1
            res -= 1
        return res 

# @lc code=end



#
# @lcpr case=start
# [10,20]\n[2,17,18,19]\n2\n
# @lcpr case=end

# @lcpr case=start
# [20,30,10]\n[19,13,26,4,25,11,21]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2]\n[2]\n2\n
# @lcpr case=end
# @lcpr case=start
# [5]\n[7,8]\n1\n
# @lcpr case=end


# @lcpr case=start
# [18,8,3,12,9,2,7,13,20,5]\n[13,10,8,4,12,14,18,19,5,2,30,34]\n1
# @lcpr case=end

#

