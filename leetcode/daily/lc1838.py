#
# @lc app=leetcode.cn id=1838 lang=python3
# @lcpr version=21913
#
# [1838] 最高频元素的频数
#
# https://leetcode.cn/problems/frequency-of-the-most-frequent-element/description/
#
# algorithms
# Medium (43.08%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    37K
# Total Submissions: 85.9K
# Testcase Example:  '[1,2,4]\n5'
#
# 元素的 频数 是该元素在一个数组中出现的次数。
# 
# 给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。
# 
# 执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,4], k = 5
# 输出：3
# 解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
# 4 是数组中最高频元素，频数是 3 。
# 
# 示例 2：
# 
# 输入：nums = [1,4,8,13], k = 5
# 输出：2
# 解释：存在多种最优解决方案：
# - 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
# - 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
# - 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
# 
# 
# 示例 3：
# 
# 输入：nums = [3,9,6], k = 2
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 1 <= k <= 10^5
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
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        s = 0 
        l = 0 
        res = 1
        for i in range(1, len(nums)):
            s += (nums[i] - nums[i - 1]) * (i - l)
            while s > k:
                s -= (nums[i] - nums[l])
                l += 1 
            res = max(res, i - l + 1)
        return res  
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,4,8,13]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,9,6]\n2\n
# @lcpr case=end

#

