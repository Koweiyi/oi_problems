#
# @lc app=leetcode.cn id=327 lang=python3
# @lcpr version=21913
#
# [327] 区间和的个数
#
# https://leetcode.cn/problems/count-of-range-sum/description/
#
# algorithms
# Hard (40.57%)
# Likes:    557
# Dislikes: 0
# Total Accepted:    42.4K
# Total Submissions: 104.5K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# 给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和
# upper）之内的 区间和的个数 。
# 
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
# 
# 
# 示例 1：
# 
# 输入：nums = [-2,5,-1], lower = -2, upper = 2
# 输出：3
# 解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。
# 
# 
# 示例 2：
# 
# 输入：nums = [0], lower = 0, upper = 0
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# -10^5 <= lower <= upper <= 10^5
# 题目数据保证答案是一个 32 位 的整数
# 
# 
#
from itertools import accumulate
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
from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList()
        res = 0
        for x in list(accumulate(nums,initial=0)):
            l = sl.bisect_left(x - upper)
            r = sl.bisect_right(x - lower)
            res += r - l
            sl.add(x)
        return res 

# @lc code=end



#
# @lcpr case=start
# [-2,5,-1]\n-2\n2\n
# @lcpr case=end

# @lcpr case=start
# [0]\n0\n0\n
# @lcpr case=end

#

