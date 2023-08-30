#
# @lc app=leetcode.cn id=493 lang=python3
# @lcpr version=21913
#
# [493] 翻转对
#
# https://leetcode.cn/problems/reverse-pairs/description/
#
# algorithms
# Hard (36.61%)
# Likes:    417
# Dislikes: 0
# Total Accepted:    41.7K
# Total Submissions: 113.8K
# Testcase Example:  '[1,3,2,3,1]'
#
# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
# 
# 你需要返回给定数组中的重要翻转对的数量。
# 
# 示例 1:
# 
# 输入: [1,3,2,3,1]
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [2,4,3,5,1]
# 输出: 3
# 
# 
# 注意:
# 
# 
# 给定数组的长度不会超过50000。
# 输入数组中的所有数字都在32位整数的表示范围内。
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
    def reversePairs(self, nums: List[int]) -> int:
        ls = SortedList()
        res = 0
        for x in nums[::-1]:
            res += ls.bisect_left(x // 2 + (x & 1))
            ls.add(x)
        return res 
# @lc code=end



#
# @lcpr case=start
# [1,3,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,3,5,1]\n
# @lcpr case=end

#

