#
# @lc app=leetcode.cn id=2289 lang=python3
# @lcpr version=21913
#
# [2289] 使数组按非递减顺序排列
#
# https://leetcode.cn/problems/steps-to-make-array-non-decreasing/description/
#
# algorithms
# Medium (21.96%)
# Likes:    125
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 27.9K
# Testcase Example:  '[5,3,4,4,7,3,6,11,8,5,11]'
#
# 给你一个下标从 0 开始的整数数组 nums 。在一步操作中，移除所有满足 nums[i - 1] > nums[i] 的 nums[i] ，其中 0 <
# i < nums.length 。
# 
# 重复执行步骤，直到 nums 变为 非递减 数组，返回所需执行的操作数。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [5,3,4,4,7,3,6,11,8,5,11]
# 输出：3
# 解释：执行下述几个步骤：
# - 步骤 1 ：[5,3,4,4,7,3,6,11,8,5,11] 变为 [5,4,4,7,6,11,11]
# - 步骤 2 ：[5,4,4,7,6,11,11] 变为 [5,4,7,11,11]
# - 步骤 3 ：[5,4,7,11,11] 变为 [5,7,11,11]
# [5,7,11,11] 是一个非递减数组，因此，返回 3 。
# 
# 
# 示例 2：
# 
# 输入：nums = [4,5,7,7,13]
# 输出：0
# 解释：nums 已经是一个非递减数组，因此，返回 0 。
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
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        res = 0 
        st = []
        for i, x in enumerate(nums):
            cur = 0 
            while st and x >= nums[st[-1][0]]:
                cur = max(cur, st[-1][1])
                st.pop()
            if st:
                cur += 1
                # print(i, ": ", st, x, nums[st[-1]],x >= nums[st[-1]])
            res = max(res, cur)
            st.append((i, cur))
        return res 
# @lc code=end



#
# @lcpr case=start
# [5,3,4,4,7,3,6,11,8,5,11]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,7,7,13]\n
# @lcpr case=end

#

