#
# @lc app=leetcode.cn id=1814 lang=python3
# @lcpr version=21913
#
# [1814] 统计一个数组中好对子的数目
#
# https://leetcode.cn/problems/count-nice-pairs-in-an-array/description/
#
# algorithms
# Medium (47.10%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    25.6K
# Total Submissions: 54.3K
# Testcase Example:  '[42,11,1,97]'
#
# 给你一个数组 nums ，数组中只包含非负整数。定义 rev(x) 的值为将整数 x 各个数字位反转得到的结果。比方说 rev(123) = 321 ，
# rev(120) = 21 。我们称满足下面条件的下标对 (i, j) 是 好的 ：
# 
# 
# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# 
# 
# 请你返回好下标对的数目。由于结果可能会很大，请将结果对 10^9 + 7 取余 后返回。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [42,11,1,97]
# 输出：2
# 解释：两个坐标对为：
# ⁠- (0,3)：42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121 。
# ⁠- (1,2)：11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12 。
# 
# 
# 示例 2：
# 
# 输入：nums = [13,10,35,24,76]
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 
# 
#
from math import comb
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        cnt = Counter()
        for x in nums:
            cnt[x - int(str(x)[::-1])] += 1
        res = 0
        for k, v in cnt.items():
            res = (res + comb(v, 2)) % (10 ** 9 + 7)
        return res 

        
        
# @lc code=end



#
# @lcpr case=start
# [42,11,1,97]\n
# @lcpr case=end

# @lcpr case=start
# [13,10,35,24,76]\n
# @lcpr case=end

#

