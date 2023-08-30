#
# @lc app=leetcode.cn id=995 lang=python3
# @lcpr version=21913
#
# [995] K 连续位的最小翻转次数
#
# https://leetcode.cn/problems/minimum-number-of-k-consecutive-bit-flips/description/
#
# algorithms
# Hard (53.94%)
# Likes:    270
# Dislikes: 0
# Total Accepted:    26.1K
# Total Submissions: 48.4K
# Testcase Example:  '[0,1,0]\n1'
#
# 给定一个二进制数组 nums 和一个整数 k 。
# 
# k位翻转 就是从 nums 中选择一个长度为 k 的 子数组 ，同时把子数组中的每一个 0 都改成 1 ，把子数组中的每一个 1 都改成 0 。
# 
# 返回数组中不存在 0 所需的最小 k位翻转 次数。如果不可能，则返回 -1 。
# 
# 子数组 是数组的 连续 部分。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [0,1,0], K = 1
# 输出：2
# 解释：先翻转 A[0]，然后翻转 A[2]。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,1,0], K = 2
# 输出：-1
# 解释：无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。
# 
# 
# 示例 3：
# 
# 输入：nums = [0,0,0,1,0,1,1,0], K = 3
# 输出：3
# 解释：
# 翻转 A[0],A[1],A[2]: A变成 [1,1,1,1,0,1,1,0]
# 翻转 A[4],A[5],A[6]: A变成 [1,1,1,1,1,0,0,0]
# 翻转 A[5],A[6],A[7]: A变成 [1,1,1,1,1,1,1,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= k <= nums.length
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 差分数组
        d = [0] * (n + 1)
        res = 0
        s = 0
        for i in range(len(nums) - k + 1):
            s += d[i]
            if s & 1 == nums[i]:
                res += 1
                s += 1 
                d[i + k] -= 1
        for j in range(len(nums) - k + 1, len(nums)):
            s += d[j]
            if s & 1 == nums[j]:
                return -1
        return res 

# @lc code=end



#
# @lcpr case=start
# [0,1,0]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,1,0]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,1,0,1,1,0]\n3\n
# @lcpr case=end

#

