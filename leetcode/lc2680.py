#
# @lc app=leetcode.cn id=2680 lang=python3
# @lcpr version=21913
#
# [2680] 最大或值
#
# https://leetcode.cn/problems/maximum-or/description/
#
# algorithms
# Medium (42.75%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    3.1K
# Total Submissions: 7.3K
# Testcase Example:  '[12,9]\n1'
#
# 给你一个下标从 0 开始长度为 n 的整数数组 nums 和一个整数 k 。每一次操作中，你可以选择一个数并将它乘 2 。
# 
# 你最多可以进行 k 次操作，请你返回 nums[0] | nums[1] | ... | nums[n - 1] 的最大值。
# 
# a | b 表示两个整数 a 和 b 的 按位或 运算。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [12,9], k = 1
# 输出：30
# 解释：如果我们对下标为 1 的元素进行操作，新的数组为 [12,18] 。此时得到最优答案为 12 和 18 的按位或运算的结果，也就是 30 。
# 
# 
# 示例 2：
# 
# 输入：nums = [8,1,2], k = 2
# 输出：35
# 解释：如果我们对下标 0 处的元素进行操作，得到新数组 [32,1,2] 。此时得到最优答案为 32|1|2 = 35 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= 15
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
    def maximumOr(self, nums: List[int], k: int) -> int:
        # cnt = Counter()
        # res = 0 
        # for x in nums:
        #     for i in range(32):
        #         if x & (1 << i) != 0:
        #             cnt[i] += 1 
        # for x in nums:
        #     y = 0 
        #     for i in range(32):
        #         if x & (1 << i) != 0:
        #             cnt[i] -= 1
        #             y |= (1 << (i + k))
        #         if cnt[i]:
        #             y |= (1 << i)
        #         if x & (1 << i) != 0:
        #             cnt[i] += 1 
        #     res = max(res, y) 
        # return res  
        n = len(nums)
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] | nums[i]
        pre = 0 
        res = 0
        for i, x in enumerate(nums):
            res = max(res, pre | (x << k) | suf[i + 1])
            pre |= x 
        return res 
# @lc code=end



#
# @lcpr case=start
# [12,9]\n2\n
# @lcpr case=end

# @lcpr case=start
# [8,1,2]\n2\n
# @lcpr case=end

#

