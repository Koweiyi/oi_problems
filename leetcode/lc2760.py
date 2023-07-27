#
# @lc app=leetcode.cn id=2760 lang=python3
# @lcpr version=21909
#
# [2760] 最长奇偶子数组
#
# https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/description/
#
# algorithms
# Easy (37.26%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 13.6K
# Testcase Example:  '[3,2,5,4]\n5'
#
# 给你一个下标从 0 开始的整数数组 nums 和一个整数 threshold 。
# 
# 请你从 nums 的子数组中找出以下标 l 开头、下标 r 结尾 (0 <= l <= r < nums.length) 且满足以下条件的 最长子数组
# ：
# 
# 
# nums[l] % 2 == 0
# 对于范围 [l, r - 1] 内的所有下标 i ，nums[i] % 2 != nums[i + 1] % 2
# 对于范围 [l, r] 内的所有下标 i ，nums[i] <= threshold
# 
# 
# 以整数形式返回满足题目要求的最长子数组的长度。
# 
# 注意：子数组 是数组中的一个连续非空元素序列。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [3,2,5,4], threshold = 5
# 输出：3
# 解释：在这个示例中，我们选择从 l = 1 开始、到 r = 3 结束的子数组 => [2,5,4] ，满足上述条件。
# 因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。
# 
# 示例 2：
# 
# 输入：nums = [1,2], threshold = 2
# 输出：1
# 解释：
# 在这个示例中，我们选择从 l = 1 开始、到 r = 1 结束的子数组 => [2] 。
# 该子数组满足上述全部条件。可以证明 1 是满足题目要求的最大长度。
# 
# 
# 示例 3：
# 
# 输入：nums = [2,3,4,5], threshold = 4
# 输出：3
# 解释：
# 在这个示例中，我们选择从 l = 0 开始、到 r = 2 结束的子数组 => [2,3,4] 。 
# 该子数组满足上述全部条件。
# 因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 100 
# 1 <= nums[i] <= 100 
# 1 <= threshold <= 100
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
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        i = res = 0
        n = len(nums)
        while i < n:
            if nums[i] > threshold or nums[i] % 2:
                i += 1
                continue
            i0 = i 
            i += 1

            while i < n and nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
                i += 1
            res = max(res, i - i0)
        return res
# @lc code=end



#
# @lcpr case=start
# [3,2,5,4]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,5]\n4\n
# @lcpr case=end

#

