#
# @lc app=leetcode.cn id=2741 lang=python3
# @lcpr version=30104
#
# [2741] 特别的排列
#
# https://leetcode.cn/problems/special-permutations/description/
#
# algorithms
# Medium (36.18%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 11.9K
# Testcase Example:  '[2,3,6]'
#
# 给你一个下标从 0 开始的整数数组 nums ，它包含 n 个 互不相同 的正整数。如果 nums
# 的一个排列满足以下条件，我们称它是一个特别的排列：
# 
# 
# 对于 0 <= i < n - 1 的下标 i ，要么 nums[i] % nums[i+1] == 0 ，要么 nums[i+1] % nums[i]
# == 0 。
# 
# 
# 请你返回特别排列的总数目，由于答案可能很大，请将它对 10^9 + 7 取余 后返回。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [2,3,6]
# 输出：2
# 解释：[3,6,2] 和 [2,6,3] 是 nums 两个特别的排列。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,4,3]
# 输出：2
# 解释：[3,1,4] 和 [4,1,3] 是 nums 两个特别的排列。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 14
# 1 <= nums[i] <= 10^9
# 
# 
#


# @lcpr-template-start
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
# @lcpr-template-end
# @lc code=start
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        @cache
        def dfs(i, j):
            if i == 0:
                return 1 
            res = 0
            for k, x in enumerate(nums):
                if i >> k & 1 and (nums[j] % x == 0 or x % nums[j] == 0):
                    res += dfs(i ^ (1 << k), k)
            return res % mod 
        n = len(nums)
        return sum(dfs(((1 << n) - 1) ^ (1 << j), j) for j in range(n)) % mod
# @lc code=end



#
# @lcpr case=start
# [2,3,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,3]\n
# @lcpr case=end

#

