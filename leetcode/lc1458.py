#
# @lc app=leetcode.cn id=1458 lang=python3
# @lcpr version=21913
#
# [1458] 两个子序列的最大点积
#
# https://leetcode.cn/problems/max-dot-product-of-two-subsequences/description/
#
# algorithms
# Hard (47.20%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    8.1K
# Total Submissions: 17.3K
# Testcase Example:  '[2,1,-2,5]\n[3,0,-6]'
#
# 给你两个数组 nums1 和 nums2 。
# 
# 请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。
# 
# 数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。比方说，[2,3,5] 是
# [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# 输出：18
# 解释：从 nums1 中得到子序列 [2,-2] ，从 nums2 中得到子序列 [3,-6] 。
# 它们的点积为 (2*3 + (-2)*(-6)) = 18 。
# 
# 示例 2：
# 
# 输入：nums1 = [3,-2], nums2 = [2,-6,7]
# 输出：21
# 解释：从 nums1 中得到子序列 [3] ，从 nums2 中得到子序列 [7] 。
# 它们的点积为 (3*7) = 21 。
# 
# 示例 3：
# 
# 输入：nums1 = [-1,-1], nums2 = [1,1]
# 输出：-1
# 解释：从 nums1 中得到子序列 [-1] ，从 nums2 中得到子序列 [1] 。
# 它们的点积为 -1 。
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums1.length, nums2.length <= 500
# -1000 <= nums1[i], nums2[i] <= 100
# 
# 
# 
# 
# 点积：
# 
# 定义 a = [a1, a2,…, an] 和 b = [b1, b2,…, bn] 的点积为：
# 
# 
# 
# 这里的 Σ 指示总和符号。
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
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # 右侧题目通过了，摸鱼一小会儿， 可以看看题目代码
        if all(x >= 0 for x in nums1) and all(x <= 0 for x in nums2):
            return min(nums1) * max(nums2)
        if all(x >= 0 for x in nums2) and all(x <= 0 for x in nums1):
            return max(nums1) * min(nums2)

        @cache
        def dfs(i: int, j: int) -> int :
            if i == 0 or j == 0 :
                return 0
            res = 0
            if nums1[i - 1] * nums2[j - 1] > 0:
                res = max(res, dfs(i - 1, j - 1) + nums1[i - 1] * nums2[j - 1])
            res = max(res, dfs(i, j - 1), dfs(i - 1, j))
            return res 
        return dfs(len(nums1), len(nums2))
# @lc code=end



#
# @lcpr case=start
# [2,1,-2,5]\n[3,0,-6]\n
# @lcpr case=end

# @lcpr case=start
# [3,-2]\n[2,-6,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1,-1]\n[1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,4,5]\n[-5,2,3]\n
# @lcpr case=end
#

