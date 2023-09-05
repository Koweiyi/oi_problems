#
# @lc app=leetcode.cn id=795 lang=python3
# @lcpr version=21913
#
# [795] 区间子数组个数
#
# https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/description/
#
# algorithms
# Medium (57.74%)
# Likes:    359
# Dislikes: 0
# Total Accepted:    36.4K
# Total Submissions: 63K
# Testcase Example:  '[2,1,4,3]\n2\n3'
#
# 给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right]
# 内的子数组，并返回满足条件的子数组的个数。
# 
# 生成的测试用例保证结果符合 32-bit 整数范围。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [2,1,4,3], left = 2, right = 3
# 输出：3
# 解释：满足条件的三个子数组：[2], [2, 1], [3]
# 
# 
# 示例 2：
# 
# 输入：nums = [2,9,2,5,6], left = 2, right = 8
# 输出：7
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= left <= right <= 10^9
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
    def numSubarrayBoundedMax(self, nums: List[int], l: int, r: int) -> int:
        #维护两个单调栈 算单个元素贡献值
        n = len(nums)
        left = [-1] * len(nums)
        st = []
        for i, x in enumerate(nums):
            while st and x >= nums[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1] # 比当前大
            st.append(i) 
        res = 0 
        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[i] > nums[st[-1]]:
                st.pop()
            right = st[-1] if st else n 
            if l <= nums[i] <= r:
                res += (i - left[i]) * (right - i) # 乘法原理 
            st.append(i)
        return res 

             

# @lc code=end



#
# @lcpr case=start
# [2,1,4,3]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,9,2,5,6]\n2\n8\n
# @lcpr case=end

#

