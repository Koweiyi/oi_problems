#
# @lc app=leetcode.cn id=2150 lang=python3
# @lcpr version=21917
#
# [2150] 找出数组中的所有孤独数字
#
# https://leetcode.cn/problems/find-all-lonely-numbers-in-the-array/description/
#
# algorithms
# Medium (59.24%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    9.9K
# Total Submissions: 16.7K
# Testcase Example:  '[10,6,5,8]'
#
# 给你一个整数数组 nums 。如果数字 x 在数组中仅出现 一次 ，且没有 相邻 数字（即，x + 1 和 x - 1）出现在数组中，则认为数字 x 是
# 孤独数字 。
# 
# 返回 nums 中的 所有 孤独数字。你可以按 任何顺序 返回答案。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [10,6,5,8]
# 输出：[10,8]
# 解释：
# - 10 是一个孤独数字，因为它只出现一次，并且 9 和 11 没有在 nums 中出现。
# - 8 是一个孤独数字，因为它只出现一次，并且 7 和 9 没有在 nums 中出现。
# - 5 不是一个孤独数字，因为 6 出现在 nums 中，反之亦然。
# 因此，nums 中的孤独数字是 [10, 8] 。
# 注意，也可以返回 [8, 10] 。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,3,5,3]
# 输出：[1,5]
# 解释：
# - 1 是一个孤独数字，因为它只出现一次，并且 0 和 2 没有在 nums 中出现。
# - 5 是一个孤独数字，因为它只出现一次，并且 4 和 6 没有在 nums 中出现。
# - 3 不是一个孤独数字，因为它出现两次。
# 因此，nums 中的孤独数字是 [1, 5] 。
# 注意，也可以返回 [5, 1] 。
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^6
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
    def findLonely(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        return [x for x in nums if x - 1 not in s and x + 1 not in s and s[x] == 1]
    
# @lc code=end



#
# @lcpr case=start
# [10,6,5,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,3]\n
# @lcpr case=end

#

