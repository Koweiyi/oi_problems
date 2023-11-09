#
# @lc app=leetcode.cn id=805 lang=python3
# @lcpr version=21917
#
# [805] 数组的均值分割
#
# https://leetcode.cn/problems/split-array-with-same-average/description/
#
# algorithms
# Hard (42.83%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    22.2K
# Total Submissions: 51.9K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# 给定你一个整数数组 nums
# 
# 我们要将 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和 B 数组不为空，并且 average(A) ==
# average(B) 。
# 
# 如果可以完成则返回true ， 否则返回 false  。
# 
# 注意：对于数组 arr ,  average(arr) 是 arr 的所有元素的和除以 arr 长度。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [1,2,3,4,5,6,7,8]
# 输出: true
# 解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
# 
# 
# 示例 2:
# 
# 输入: nums = [3,1]
# 输出: false
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums.length <= 30
# 0 <= nums[i] <= 10^4
# 
# 
#
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate
from functools import cache, lru_cache
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
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # BUG 枚举A数组长度 变为子集和问题 
        # 事实上A， B是对称的 也就是说只需要枚举到 15
        # dp[i][k][m] 表示 前i个数中选择k个数和为m的可行性 
        n = len(nums)
        s = sum(nums)
        @cache
        def dfs(i, k, m):
            if i < k:
                return False
            if i == 0:
                return k == 0 and m == 0
            if  k == 0:
                return m == 0
            if dfs(i - 1, k, m):
                return True 
            if nums[i - 1] <= m:
                return dfs(i - 1, k - 1, m - nums[i - 1]) 
            return False
            
        res = False
        for i in range(1, n // 2 + 1):
            # m = s * (i // n) (s * i) 需要被 n 整除 
            if s * i % n:
                continue 
            m = s * i // n 
            # print(n, i, m)
            if dfs(n, i, m):
                res = True 
                break 
        dfs.cache_clear()
        return res 



# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7,8]\n
# @lcpr case=end

# @lcpr case=start
# [3,1]\n
# @lcpr case=end
# @lcpr case=start
# [2,0,7,0,6]
# @lcpr case=end
#

