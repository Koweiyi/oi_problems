#
# @lc app=leetcode.cn id=315 lang=python3
# @lcpr version=21913
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode.cn/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (43.46%)
# Likes:    1004
# Dislikes: 0
# Total Accepted:    85.1K
# Total Submissions: 195.8K
# Testcase Example:  '[5,2,6,1]'
#
# 给你一个整数数组 nums ，按要求返回一个新数组 counts 。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [5,2,6,1]
# 输出：[2,1,1,0] 
# 解释：
# 5 的右侧有 2 个更小的元素 (2 和 1)
# 2 的右侧仅有 1 个更小的元素 (1)
# 6 的右侧有 1 个更小的元素 (1)
# 1 的右侧有 0 个更小的元素
# 
# 
# 示例 2：
# 
# 输入：nums = [-1]
# 输出：[0]
# 
# 
# 示例 3：
# 
# 输入：nums = [-1,-1]
# 输出：[0,0]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
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
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ls = SortedList()
        res = [0] * len(nums)
        for i,x in enumerate(nums[::-1]):
            res[-i - 1] = ls.bisect_left(x)
            ls.add(x)
        return res
# @lc code=end



#
# @lcpr case=start
# [5,2,6,1]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n
# @lcpr case=end

# @lcpr case=start
# [-1,-1]\n
# @lcpr case=end

#

