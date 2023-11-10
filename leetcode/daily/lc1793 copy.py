#
# @lc app=leetcode.cn id=1793 lang=python3
# @lcpr version=21914
#
# [1793] 好子数组的最大分数
#
# https://leetcode.cn/problems/maximum-score-of-a-good-subarray/description/
#
# algorithms
# Hard (45.79%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 13.3K
# Testcase Example:  '[1,4,3,7,4,5]\n3'
#
# 给你一个整数数组 nums （下标从 0 开始）和一个整数 k 。
# 
# 一个子数组 (i, j) 的 分数 定义为 min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) 。一个
# 好 子数组的两个端点下标需要满足 i <= k <= j 。
# 
# 请你返回 好 子数组的最大可能 分数 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,4,3,7,4,5], k = 3
# 输出：15
# 解释：最优子数组的左右端点下标是 (1, 5) ，分数为 min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15 。
# 
# 
# 示例 2：
# 
# 输入：nums = [5,5,4,5,4,1,1,1], k = 0
# 输出：20
# 解释：最优子数组的左右端点下标是 (0, 4) ，分数为 min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 2 * 10^4
# 0 <= k < nums.length
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
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        right = [n] * n
        st = []
        for i in range(n - 1, -1, -1):
            x = nums[i] 
            while st and x <= nums[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        st = []
        res = 0 
        
        for i, x in enumerate(nums):
            while st and x <= nums[st[-1]]:
                st.pop()
            if st:
                left = st[-1]
            else:
                left = -1 
            if right[i] > k and left < k:
                res = max(res, (right[i] - left - 1) * x) 
            st.append(i)
        return res  
# @lc code=end



#
# @lcpr case=start
# [1,4,3,7,4,5]\n3\n
# @lcpr case=end

# @lcpr case=start
# [5,5,4,5,4,1,1,1]\n0\n
# @lcpr case=end

#

