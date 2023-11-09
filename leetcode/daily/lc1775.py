#
# @lc app=leetcode.cn id=1775 lang=python3
# @lcpr version=21801
#
# [1775] 通过最少操作次数使数组的和相等
#
# https://leetcode.cn/problems/equal-sum-arrays-with-minimum-number-of-operations/description/
#
# algorithms
# Medium (56.47%)
# Likes:    188
# Dislikes: 0
# Total Accepted:    25.2K
# Total Submissions: 44.6K
# Testcase Example:  '[1,2,3,4,5,6]\n[1,1,2,2,2,2]'
#
# 给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。
# 
# 每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。
# 
# 请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
# 输出：3
# 解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
# - 将 nums2[0] 变为 6 。 nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2] 。
# - 将 nums1[5] 变为 1 。 nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2] 。
# - 将 nums1[2] 变为 2 。 nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2] 。
# 
# 
# 示例 2：
# 
# 输入：nums1 = [1,1,1,1,1,1,1], nums2 = [6]
# 输出：-1
# 解释：没有办法减少 nums1 的和或者增加 nums2 的和使二者相等。
# 
# 
# 示例 3：
# 
# 输入：nums1 = [6,6], nums2 = [1]
# 输出：3
# 解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
# - 将 nums1[0] 变为 2 。 nums1 = [2,6], nums2 = [1] 。
# - 将 nums1[1] 变为 2 。 nums1 = [2,2], nums2 = [1] 。
# - 将 nums2[0] 变为 4 。 nums1 = [2,2], nums2 = [4] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums1.length, nums2.length <= 10^5
# 1 <= nums1[i], nums2[i] <= 6
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
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if sum(nums1) == sum(nums2):
            return 0 
        elif sum(nums1) > sum(nums2):
            return self.minOperations(nums2, nums1)
        cnt = Counter()
        for x in nums1:
            cnt[6 - x] += 1
        for x in nums2:
            cnt[x - 1] += 1
        dif = sum(nums2) - sum(nums1)
        res = 0 
        for x in range(5, 0, -1):
            if cnt[x] == 0:
                continue
            if cnt[x] * x >= dif:
                res += (dif + x - 1) // x 
                return res  
            dif -= cnt[x] * x 
            res += cnt[x] 
        return -1
            


# @lc code=end

# @lcpr-div-debug-arg-start
# funName=
# paramTypes= []
# returnType=
# @lcpr-div-debug-arg-end


#
# @lcpr case=start
# [1,2,3,4,5,6]\n[1,1,2,2,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1,1,1]\n[6]\n
# @lcpr case=end

# @lcpr case=start
# [6,6]\n[1]\n
# @lcpr case=end

#


