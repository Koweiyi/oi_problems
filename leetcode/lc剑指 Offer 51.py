#
# @lc app=leetcode.cn id=剑指 Offer 51 lang=python3
# @lcpr version=21913
#
# [剑指 Offer 51] 数组中的逆序对
#
# https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/description/
#
# LCOF
# Hard (49.50%)
# Likes:    1053
# Dislikes: 0
# Total Accepted:    205K
# Total Submissions: 414.1K
# Testcase Example:  '[7,5,6,4]'
#
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
# 
# 
# 
# 示例 1:
# 
# 输入: [7,5,6,4]
# 输出: 5
# 
# 
# 
# 限制：
# 
# 0 <= 数组长度 <= 50000
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
        for i, x in enumerate(nums):
            res += i - ls.bisect_left(x + 1)
            ls.add(x)
        return res 
# @lc code=end



#
# @lcpr case=start
# [7,5,6,4]\n
# @lcpr case=end

#

