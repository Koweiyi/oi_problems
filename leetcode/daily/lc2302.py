#
# @lc app=leetcode.cn id=2302 lang=python3
# @lcpr version=21913
#
# [2302] 统计得分小于 K 的子数组数目
#
# https://leetcode.cn/problems/count-subarrays-with-score-less-than-k/description/
#
# algorithms
# Hard (51.13%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    5.6K
# Total Submissions: 11K
# Testcase Example:  '[2,1,4,3,5]\n10'
#
# 一个数组的 分数 定义为数组之和 乘以 数组的长度。
# 
# 
# 比方说，[1, 2, 3, 4, 5] 的分数为 (1 + 2 + 3 + 4 + 5) * 5 = 75 。
# 
# 
# 给你一个正整数数组 nums 和一个整数 k ，请你返回 nums 中分数 严格小于 k 的 非空整数子数组数目。
# 
# 子数组 是数组中的一个连续元素序列。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [2,1,4,3,5], k = 10
# 输出：6
# 解释：
# 有 6 个子数组的分数小于 10 ：
# - [2] 分数为 2 * 1 = 2 。
# - [1] 分数为 1 * 1 = 1 。
# - [4] 分数为 4 * 1 = 4 。
# - [3] 分数为 3 * 1 = 3 。 
# - [5] 分数为 5 * 1 = 5 。
# - [2,1] 分数为 (2 + 1) * 2 = 6 。
# 注意，子数组 [1,4] 和 [4,3,5] 不符合要求，因为它们的分数分别为 10 和 36，但我们要求子数组的分数严格小于 10 。
# 
# 示例 2：
# 
# 输入：nums = [1,1,1], k = 5
# 输出：5
# 解释：
# 除了 [1,1,1] 以外每个子数组分数都小于 5 。
# [1,1,1] 分数为 (1 + 1 + 1) * 3 = 9 ，大于 5 。
# 所以总共有 5 个子数组得分小于 5 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 1 <= k <= 10^15
# 
# 
#
from itertools import accumulate
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
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 滑窗 or 二分
        # 滑窗 296 ms
        # 二分 2572 ms 
        s = list(accumulate(nums, initial=0)) 
        # res = cur = 0 
        # l = 0 
        # for i, x in enumerate(nums):
        #     cur = (s[i + 1] - s[l]) * (i - l + 1)
        #     while cur >= k:
        #         l += 1
        #         cur = (s[i + 1] - s[l]) * (i - l + 1)
        #     res += i - l + 1 
        # return res 

        res = 0 
        for i in range(len(nums)):
            l, r = -1, i + 1
            while l + 1 < r :
                mid = (l + r) // 2 
                if (s[i + 1] - s[mid]) * (i - mid + 1) < k:
                    r = mid 
                else:
                    l = mid
            res += i - r + 1 
        return res  




# @lc code=end



#
# @lcpr case=start
# [2,1,4,3,5]\n10\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n5\n
# @lcpr case=end

#

