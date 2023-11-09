#
# @lc app=leetcode.cn id=1802 lang=python3
# @lcpr version=21914
#
# [1802] 有界数组中指定下标处的最大值
#
# https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/description/
#
# algorithms
# Medium (38.09%)
# Likes:    197
# Dislikes: 0
# Total Accepted:    25.5K
# Total Submissions: 66.9K
# Testcase Example:  '4\n2\n6'
#
# 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
# 
# 
# nums.length == n
# nums[i] 是 正整数 ，其中 0 <= i < n
# abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
# nums 中所有元素之和不超过 maxSum
# nums[index] 的值被 最大化
# 
# 
# 返回你所构造的数组中的 nums[index] 。
# 
# 注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 4, index = 2,  maxSum = 6
# 输出：2
# 解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
# 
# 
# 示例 2：
# 
# 输入：n = 6, index = 1,  maxSum = 10
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= maxSum <= 10^9
# 0 <= index < n
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
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # 最大化某个值等于二分答案 
        # 本题存在数学解，但是不好算 
        def check(x: int) -> bool:
            pre = 0
            if index:
                if x - index > 0:
                    pre = (x - 1 + x - index) * (index) // 2
                else:
                    pre = (x) * (x - 1) // 2 + (index - (x - 1))
        
            if x - (n - index - 1) > 0:
                suf = (x + x - (n - index - 1)) * (n - index) // 2
            else:
                suf = x * (x + 1) // 2 + (n - index - x)
            return pre + suf > maxSum
        
        return bisect_left(range(10 ** 9 + 5), True, key=check) - 1
# @lc code=end



#
# @lcpr case=start
# 4\n2\n6\n
# @lcpr case=end

# @lcpr case=start
# 6\n1\n10\n
# @lcpr case=end

# @lcpr case=start
# 4\n0\n4\n
# @lcpr case=end
# @lcpr case=start
# 4\n3\n4\n
# @lcpr case=end
#

