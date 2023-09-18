#
# @lc app=leetcode.cn id=1124 lang=python3
# @lcpr version=21913
#
# [1124] 表现良好的最长时间段
#
# https://leetcode.cn/problems/longest-well-performing-interval/description/
#
# algorithms
# Medium (39.29%)
# Likes:    496
# Dislikes: 0
# Total Accepted:    43.4K
# Total Submissions: 110.4K
# Testcase Example:  '[9,9,6,0,6,6,9]'
#
# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
# 
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
# 
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
# 
# 请你返回「表现良好时间段」的最大长度。
# 
# 
# 
# 示例 1：
# 
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。
# 
# 示例 2：
# 
# 输入：hours = [6,6,6]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= hours.length <= 10^4
# 0 <= hours[i] <= 16
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
    def longestWPI(self, hours: List[int]) -> int:
        s = 0 
        mp = Counter()
        res = 0
        for i, x in enumerate(hours):
            if x > 8:
                s += 1 
            else:
                s -= 1 
            if s > 0:
                res = max(res, i + 1)
            else:
                if s - 1 in mp:
                    res = max(res, i - mp[s-1])
            if s not in mp:
                mp[s] = i 
        return res 
# @lc code=end



#
# @lcpr case=start
# [9,9,6,0,6,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [6,6,6]\n
# @lcpr case=end

#

