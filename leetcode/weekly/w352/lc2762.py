#
# @lc app=leetcode.cn id=2762 lang=python3
# @lcpr version=21909
#
# [2762] 不间断子数组
#
# https://leetcode.cn/problems/continuous-subarrays/description/
#
# algorithms
# Medium (47.20%)
# Likes:    19
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 8K
# Testcase Example:  '[5,4,2,4]'
#
# 给你一个下标从 0 开始的整数数组 nums 。nums 的一个子数组如果满足以下条件，那么它是 不间断 的：
# 
# 
# i，i + 1 ，...，j  表示子数组中的下标。对于所有满足 i <= i1, i2 <= j 的下标对，都有 0 <= |nums[i1] -
# nums[i2]| <= 2 。
# 
# 
# 请你返回 不间断 子数组的总数目。
# 
# 子数组是一个数组中一段连续 非空 的元素序列。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [5,4,2,4]
# 输出：8
# 解释：
# 大小为 1 的不间断子数组：[5], [4], [2], [4] 。
# 大小为 2 的不间断子数组：[5,4], [4,2], [2,4] 。
# 大小为 3 的不间断子数组：[4,2,4] 。
# 没有大小为 4 的不间断子数组。
# 不间断子数组的总数目为 4 + 3 + 1 = 8 。
# 除了这些以外，没有别的不间断子数组。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,2,3]
# 输出：6
# 解释：
# 大小为 1 的不间断子数组：[1], [2], [3] 。
# 大小为 2 的不间断子数组：[1,2], [2,3] 。
# 大小为 3 的不间断子数组：[1,2,3] 。
# 不间断子数组的总数目为 3 + 2 + 1 = 6 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
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
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = l = 0
        cnt = Counter()
        for r, x in enumerate(nums):
            cnt[nums[r]] += 1
            while(max(cnt) - min(cnt) > 2):
                cnt[nums[l]] -= 1
                if cnt[nums[l]] == 0:
                    del cnt[nums[l]]
                l += 1
            res += r - l + 1
        return res
# @lc code=end



#
# @lcpr case=start
# [5,4,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#
